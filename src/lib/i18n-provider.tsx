'use client';

import { NextIntlClientProvider, useMessages } from 'next-intl';

interface I18nProviderProps {
  children: React.ReactNode;
  locale: string;
}

/**
 * I18nProvider for next-intl
 *
 * Usage in layout.tsx:
 * ```tsx
 * import { I18nProvider } from '@/lib/i18n-provider';
 *
 * export default function RootLayout({ children, params }: { children: React.ReactNode; params: { locale: string } }) {
 *   return (
 *     <html lang={params.locale}>
 *       <body>
 *         <I18nProvider locale={params.locale}>
 *           {children}
 *         </I18nProvider>
 *       </body>
 *     </html>
 *   );
 * }
 * ```
 */
export function I18nProvider({ children, locale }: I18nProviderProps) {
  // Get messages for the current locale (loaded via getRequestConfig)
  const messages = useMessages();

  return (
    <NextIntlClientProvider
      locale={locale}
      messages={messages}
      timeZone="America/Guayaquil"
      // Optional: custom formatters
      // formats={{
      //   dateTime: { ... },
      //   number: { ... }
      // }}
    >
      {children}
    </NextIntlClientProvider>
  );
}

/**
 * Hook para usar en componentes cliente (alternativa a useTranslations)
 *
 * Para componentes servidor: importar useTranslations de 'next-intl/server'
 * Para componentes cliente: importar useTranslations de 'next-intl'
 */
export { useTranslations } from 'next-intl';