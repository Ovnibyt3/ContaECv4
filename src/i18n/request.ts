import { getRequestConfig } from 'next-intl/server';
import type { Locale } from '../i18n-config';

export default getRequestConfig(async ({ locale }) => ({
  // Loads the `messages/[locale].json` file
  messages: (await import(`../../messages/${locale}.json`)).default,

  // Optional: configure namespace for component-level translations
  // This allows splitting large translation files
  // namespaces: ['common', 'navigation', 'dashboard', 'invoice', 'accounting', 'hr', 'crm'],
  // defaultNamespace: 'common',

  // Timezone for date formatting
  timeZone: 'America/Guayaquil',

  // Custom formatters for locale-specific formatting
  formats: {
    dateTime: {
      short: {
        day: '2-digit',
        month: '2-digit',
        year: 'numeric'
      },
      long: {
        day: '2-digit',
        month: 'long',
        year: 'numeric',
        hour: '2-digit',
        minute: '2-digit'
      }
    },
    number: {
      currency: {
        style: 'currency',
        currency: 'USD',
        minimumFractionDigits: 2,
        maximumFractionDigits: 2
      }
    }
  }
}));