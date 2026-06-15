// Serve uploaded files (logos, signatures) directly from backend/uploads/
import { NextRequest, NextResponse } from 'next/server';
import { readFile } from 'fs/promises';
import path from 'path';

export async function GET(
  request: NextRequest,
  { params }: { params: Promise<{ path: string[] }> }
) {
  const segments = (await params).path;
  if (!segments || segments.length === 0) {
    return new NextResponse('Not found', { status: 404 });
  }

  const filePath = path.join(
    process.cwd(),
    'backend',
    'uploads',
    ...segments
  );

  // Security: prevent path traversal
  const uploadsDir = path.join(process.cwd(), 'backend', 'uploads');
  if (!filePath.startsWith(uploadsDir)) {
    return new NextResponse('Forbidden', { status: 403 });
  }

  try {
    const file = await readFile(filePath);
    const ext = path.extname(filePath).toLowerCase();
    const mimeTypes: Record<string, string> = {
      '.png': 'image/png',
      '.jpg': 'image/jpeg',
      '.jpeg': 'image/jpeg',
      '.gif': 'image/gif',
      '.svg': 'image/svg+xml',
      '.webp': 'image/webp',
      '.p12': 'application/x-pkcs12',
      '.pfx': 'application/x-pkcs12',
    };
    const contentType = mimeTypes[ext] || 'application/octet-stream';

    return new NextResponse(file, {
      status: 200,
      headers: {
        'Content-Type': contentType,
        'Cache-Control': 'public, max-age=3600',
      },
    });
  } catch {
    return new NextResponse('File not found', { status: 404 });
  }
}
