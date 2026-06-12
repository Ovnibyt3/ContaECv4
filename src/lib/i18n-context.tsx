'use client';

import { createContext, useContext, useState, useEffect, useCallback, type ReactNode } from 'react';
import { getLocale, setLocale, t as translate, LOCALES, getLocaleLabel } from './i18n';
import type { Locale } from './i18n';

interface I18nContextValue {
  locale: Locale;
  setLocale: (locale: Locale) => void;
  t: (key: string, params?: Record<string, string | number>) => string;
  locales: typeof LOCALES;
  getLocaleLabel: (locale: Locale) => string;
}

const I18nContext = createContext<I18nContextValue | null>(null);

export function I18nProvider({ children }: { children: ReactNode }) {
  const [locale, setLocaleState] = useState<Locale>(() => {
    if (typeof window === 'undefined') return 'es_EC';
    return getLocale();
  });

  useEffect(() => {
    // Listen for storage changes (e.g., from other tabs or settings page)
    const handler = (e: StorageEvent) => {
      if (e.key === 'contaec_locale' && e.newValue && e.newValue in ({} as Record<string, string>)) {
        // Import translations lazily to validate
        const translations: Record<string, unknown> = { es_EC: {}, en_US: {}, pt_BR: {} };
        if (e.newValue in translations) {
          setLocaleState(e.newValue as Locale);
        }
      }
    };
    window.addEventListener('storage', handler);
    return () => window.removeEventListener('storage', handler);
  }, []);

  const changeLocale = useCallback((newLocale: Locale) => {
    setLocale(newLocale);
    setLocaleState(newLocale);
  }, []);

  const t = useCallback(
    (key: string, params?: Record<string, string | number>) => {
      return translate(key, params);
    },
    // eslint-disable-next-line react-hooks/exhaustive-deps
    [locale]
  );

  return (
    <I18nContext.Provider
      value={{
        locale,
        setLocale: changeLocale,
        t,
        locales: LOCALES,
        getLocaleLabel,
      }}
    >
      {children}
    </I18nContext.Provider>
  );
}

export function useI18n() {
  const ctx = useContext(I18nContext);
  if (!ctx) {
    throw new Error('useI18n must be used within an I18nProvider');
  }
  return ctx;
}
