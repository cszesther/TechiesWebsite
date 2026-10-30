import { mkdirSync } from "node:fs";
import { resolve } from "node:path";
import { spawn } from "node:child_process";

// Always use a project-local SQLite database and uploads. Never connect to D1/R2.
const dataDirectory = resolve(".preview");
mkdirSync(dataDirectory, { recursive: true });
const child = spawn(process.execPath, ["node_modules/astro/bin/astro.mjs", "dev", "--ignore-lock", "--host", "127.0.0.1", "--port", "4331"], {
  stdio: "inherit",
  env: {
    ...process.env,
    EMDASH_RUNTIME: "node",
    TECHIES_PREVIEW: "1",
    TECHIES_DATA_DIR: dataDirectory,
    EMDASH_SITE_URL: "http://localhost:4331",
    SITE_URL: "http://localhost:4331",
  },
});
child.on("error", error => { console.error(error.message); process.exitCode = 1; });
child.on("exit", (code, signal) => {
  if (signal) process.kill(process.pid, signal);
  else process.exitCode = code ?? 1;
});
for (const signal of ["SIGINT", "SIGTERM"]) process.on(signal, () => child.kill(signal));
