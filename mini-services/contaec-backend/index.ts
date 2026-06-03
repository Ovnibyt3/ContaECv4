import { spawn } from 'child_process';
import { createInterface } from 'readline';

const PORT = 8001;

console.log(`[ContaEC Backend] Starting on port ${PORT}...`);

const pythonPath = '/home/z/.venv/bin/python3';

const proc = spawn(pythonPath, [
  '-m', 'uvicorn', 'main:app',
  '--host', '0.0.0.0',
  '--port', String(PORT),
], {
  cwd: '/home/z/my-project/backend',
  stdio: ['ignore', 'pipe', 'pipe'],
  detached: false,
  env: { ...process.env, PYTHONUNBUFFERED: '1' },
});

proc.stdout?.on('data', (data: Buffer) => {
  const lines = data.toString().split('\n').filter(Boolean);
  lines.forEach(line => console.log(`[backend:out] ${line}`));
});

proc.stderr?.on('data', (data: Buffer) => {
  const lines = data.toString().split('\n').filter(Boolean);
  lines.forEach(line => console.log(`[backend:err] ${line}`));
});

proc.on('exit', (code, signal) => {
  console.log(`[ContaEC Backend] Process exited with code ${code}, signal ${signal}`);
  console.log(`[ContaEC Backend] Restarting in 3 seconds...`);
  setTimeout(() => {
    // Restart
    process.exit(1); // Let bun restart it via --hot
  }, 3000);
});

proc.on('error', (err) => {
  console.error(`[ContaEC Backend] Error: ${err.message}`);
});

// Keep the process alive
process.on('SIGINT', () => {
  proc.kill('SIGTERM');
  process.exit(0);
});

process.on('SIGTERM', () => {
  proc.kill('SIGTERM');
  process.exit(0);
});

console.log(`[ContaEC Backend] Service started, PID: ${proc.pid}`);
