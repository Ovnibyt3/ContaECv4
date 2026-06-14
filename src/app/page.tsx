'use client';

import Image from 'next/image';
import { useState, useEffect } from 'react';
import { ContaECLogin } from '@/components/contaec-login';
import { ContaECDashboard } from '@/components/contaec-dashboard';
import { ContaECAdmin } from '@/components/contaec-admin';
import { getMe, getUserCache, type User } from '@/lib/api';

type AppView = 'login' | 'dashboard' | 'admin';

export default function Home() {
  const [view, setView] = useState<AppView>('login');
  const [user, setUser] = useState<User | null>(null);
  const [initializing, setInitializing] = useState(true);

  // Check for existing session on mount
  useEffect(() => {
    async function checkAuth() {
      // First try cached user for instant UI
      const cached = getUserCache();
      if (cached) {
        setUser(cached as User);
        setView('dashboard');
        setInitializing(false);

        // Then verify with backend in background
        try {
          const freshUser = await getMe();
          setUser(freshUser);
        } catch {
          // Token invalid, logout
          setUser(null);
          setView('login');
        }
        return;
      }

      // No cached user, try backend
      try {
        const freshUser = await getMe();
        setUser(freshUser);
        setView('dashboard');
      } catch {
        setUser(null);
        setView('login');
      } finally {
        setInitializing(false);
      }
    }

    checkAuth();
  }, []);

  function handleAuthSuccess(authenticatedUser: User) {
    setUser(authenticatedUser);
    setView('dashboard');
  }

  function handleLogout() {
    setUser(null);
    setView('login');
  }

  function handleShowAdmin() {
    setView('admin');
  }

  function handleBackFromAdmin() {
    setView('dashboard');
  }

  // Loading screen while checking auth
  if (initializing) {
    return (
      <div className="min-h-screen flex items-center justify-center bg-background">
        <div className="text-center space-y-4">
          <Image
            src="/logo.svg"
            alt="ContaEC Logo"
            width={120}
            height={100}
            className="h-24 w-auto mx-auto"
            priority
          />
          <h1 className="text-2xl font-bold text-foreground">ContaEC</h1>
          <p className="text-sm text-muted-foreground">Cargando...</p>
        </div>
      </div>
    );
  }

  if (view === 'login' || !user) {
    return <ContaECLogin onAuthSuccess={handleAuthSuccess} />;
  }

  if (view === 'admin') {
    return <ContaECAdmin onBack={handleBackFromAdmin} />;
  }

  return (
    <ContaECDashboard
      user={user}
      onLogout={handleLogout}
      onShowAdmin={handleShowAdmin}
    />
  );
}
