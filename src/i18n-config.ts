// i18n-config.ts
// Locale configuration for next-intl

export const locales = ['es', 'en', 'pt'] as const;
export type Locale = (typeof locales)[number];

export const localeNames: Record<Locale, string> = {
  es: 'Español (Ecuador)',
  en: 'English (US)',
  pt: 'Português (Brasil)'
};

export const defaultLocale: Locale = 'es';

// Fallback locale for missing translations
export const fallbackLocale: Locale = 'es';

// Helper to get locale from legacy codes (es_EC, en_US, pt_BR)
export function normalizeLocale(locale: string): Locale {
  const normalized = locale.split('_')[0].toLowerCase();
  if (normalized === 'es') return 'es';
  if (normalized === 'en') return 'en';
  if (normalized === 'pt') return 'pt';
  return defaultLocale;
}

// Helper to convert legacy codes to next-intl format
export function legacyToNextIntl(legacyCode: string): Locale {
  // Legacy: es_EC, en_US, pt_BR
  // next-intl: es, en, pt
  const map: Record<string, Locale> = {
    'es_EC': 'es',
    'en_US': 'en',
    'pt_BR': 'pt'
  };
  return map[legacyCode] || defaultLocale;
}

// Helper to convert next-intl to legacy format (for API calls, etc.)
export function nextIntlToLegacy(locale: Locale): string {
  const map: Record<Locale, string> = {
    es: 'es_EC',
    en: 'en_US',
    pt: 'pt_BR'
  };
  return map[locale];
}