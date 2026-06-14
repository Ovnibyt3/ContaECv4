import type { MetadataRoute } from 'next';

export default function manifest(): MetadataRoute.Manifest {
  return {
    name: 'ContaEC - Contabilidad y Facturacion Electronica Ecuador',
    short_name: 'ContaEC',
    description:
      'Sistema de contabilidad y facturacion electronica para Ecuador. Cumpla con las normativas del SRI de manera simple y eficiente.',
    start_url: '/',
    display: 'standalone',
    background_color: '#ffffff',
    theme_color: '#0b3b75',
    icons: [
      {
        src: '/logo.svg',
        sizes: 'any',
        type: 'image/svg+xml',
        purpose: 'any maskable',
      },
    ],
  };
}
