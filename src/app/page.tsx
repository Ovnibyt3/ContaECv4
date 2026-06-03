'use client';

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
        <div className="text-center">
          <div className="inline-flex items-center justify-center w-16 h-16 rounded-2xl bg-primary/10 mb-4 animate-pulse">
            <svg
              className="w-8 h-8 text-primary"
              xmlns="http://www.w3.org/2000/svg"
              fill="none"
              viewBox="0 0 24 24"
              stroke="currentColor"
              strokeWidth={2}
            >
              <path
                strokeLinecap="round"
                strokeLinejoin="round"
                d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"
              />
            </svg>
          </div>
          <h1 className="text-xl font-bold text-foreground">ContaEC</h1>
          <p className="text-sm text-muted-foreground mt-1">Cargando...</p>
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
