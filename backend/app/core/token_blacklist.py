"""
ContaEC - Token Blacklist / Revocation Service
In-memory token revocation list with automatic cleanup of expired tokens.
Supports JWT token revocation and refresh token rotation tracking.
"""
import logging
import time
from typing import Optional

logger = logging.getLogger(__name__)


class TokenBlacklist:
    """
    In-memory token blacklist for JWT revocation.
    
    Stores revoked token JTI (JWT ID) with their expiration timestamp.
    Automatically cleans up expired entries to prevent memory leaks.
    
    For production with multiple workers, replace with Redis-backed implementation.
    """

    def __init__(self):
        # Dict[jti, expire_timestamp] - stores revoked JTIs with their expiry
        self._revoked: dict[str, float] = {}
        # Dict[old_jti, new_jti] - tracks refresh token rotation (old -> new)
        self._refresh_rotations: dict[str, str] = {}
        # Set of reused refresh JTIs (potential token replay attacks)
        self._reused_refresh: set[str] = set()

    def revoke_token(self, jti: str, exp_timestamp: float) -> None:
        """
        Add a token JTI to the revocation list.
        
        Args:
            jti: JWT ID of the token to revoke
            exp_timestamp: Expiration timestamp of the token (for auto-cleanup)
        """
        self._revoked[jti] = exp_timestamp
        logger.info(f"Token revoked: jti={jti}")

    def is_revoked(self, jti: str) -> bool:
        """
        Check if a token JTI has been revoked.
        
        Args:
            jti: JWT ID to check
            
        Returns:
            True if the token is revoked, False otherwise
        """
        return jti in self._revoked

    def register_refresh_rotation(self, old_jti: str, new_jti: str) -> None:
        """
        Register a refresh token rotation (old JTI -> new JTI).
        When a refresh token is used, the old one should be tracked
        to detect replay attacks.
        
        Args:
            old_jti: JTI of the old refresh token
            new_jti: JTI of the new refresh token
        """
        self._refresh_rotations[old_jti] = new_jti
        logger.debug(f"Refresh rotation registered: {old_jti[:8]}... -> {new_jti[:8]}...")

    def check_refresh_reuse(self, jti: str) -> bool:
        """
        Check if a refresh token JTI has been reused (potential replay attack).
        If a previously rotated refresh token is used again, it indicates
        a token replay attack and ALL tokens in the rotation chain should be revoked.
        
        Args:
            jti: JTI of the refresh token being used
            
        Returns:
            True if this JTI was already rotated (reused), False otherwise
        """
        if jti in self._refresh_rotations:
            # This token was already used to get a new refresh token - REUSE DETECTED!
            self._reused_refresh.add(jti)
            logger.warning(
                f"SECURITY: Refresh token reuse detected! jti={jti[:8]}... "
                "All tokens in this chain should be revoked."
            )
            return True
        return jti in self._reused_refresh

    def revoke_refresh_chain(self, jti: str, exp_timestamp: float) -> list[str]:
        """
        Revoke an entire refresh token chain starting from a reused token.
        This is called when a replay attack is detected - all tokens
        derived from the compromised chain are revoked.
        
        Args:
            jti: JTI of the reused refresh token
            exp_timestamp: Expiration timestamp to use for revocation
            
        Returns:
            List of all revoked JTIs in the chain
        """
        revoked_chain = [jti]
        self._revoked[jti] = exp_timestamp

        # Walk the rotation chain forward
        current = jti
        while current in self._refresh_rotations:
            next_jti = self._refresh_rotations[current]
            self._revoked[next_jti] = exp_timestamp
            revoked_chain.append(next_jti)
            current = next_jti

        logger.warning(
            f"SECURITY: Revoked {len(revoked_chain)} tokens in refresh chain "
            f"starting from jti={jti[:8]}..."
        )
        return revoked_chain

    def cleanup_expired(self) -> int:
        """
        Remove expired entries from the revocation list.
        Should be called periodically to prevent memory leaks.
        
        Returns:
            Number of entries removed
        """
        now = time.time()
        expired_jtis = [
            jti for jti, exp in self._revoked.items()
            if exp < now
        ]
        for jti in expired_jtis:
            del self._revoked[jti]

        # Also clean up rotation tracking for expired tokens
        expired_rotations = [
            old_jti for old_jti, new_jti in self._refresh_rotations.items()
            if old_jti in expired_jtis or new_jti in expired_jtis
        ]
        for old_jti in expired_rotations:
            del self._refresh_rotations[old_jti]

        # Clean up reuse tracking
        self._reused_refresh -= set(expired_jtis)

        if expired_jtis:
            logger.debug(f"Cleaned up {len(expired_jtis)} expired token revocations")

        return len(expired_jtis)

    @property
    def revoked_count(self) -> int:
        """Number of currently revoked tokens"""
        return len(self._revoked)

    @property
    def rotation_count(self) -> int:
        """Number of tracked refresh token rotations"""
        return len(self._refresh_rotations)


# Global singleton instance
_token_blacklist: Optional[TokenBlacklist] = None


def get_token_blacklist() -> TokenBlacklist:
    """Get the global token blacklist instance"""
    global _token_blacklist
    if _token_blacklist is None:
        _token_blacklist = TokenBlacklist()
    return _token_blacklist
