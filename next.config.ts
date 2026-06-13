import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  output: "standalone",
  typescript: {
    ignoreBuildErrors: false,
  },
  reactStrictMode: true,
  async rewrites() {
    return {
      backend: {
        source: '/api/:path*',
        destination: 'http://localhost:8000/api/:path*',
      },
      backendV1: {
        source: '/v1/:path*',
        destination: 'http://localhost:8000/v1/:path*',
      },
    };
  },
};

export default nextConfig;