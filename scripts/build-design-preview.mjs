import { spawn } from "node:child_process";
import { resolve } from "node:path";

const env = { ...process.env, EMDASH_RUNTIME: "node", TECHIES_PREVIEW: "1", TECHIES_DATA_DIR: resolve(".preview"), EMDASH_SITE_URL: "http://localhost:4333", SITE_URL: "http://localhost:4333", HOST: "127.0.0.1", PORT: "4333" };
function run(command, args) {
  return new Promise((resolve, reject) => {
    const child = spawn(command, args, { env, stdio: "inherit" });
    child.on("error", reject);
    child.on("exit", code => code === 0 ? resolve() : reject(new Error(`${command} exited ${code}`)));
  });
}
await run(process.execPath, ["node_modules/astro/bin/astro.mjs", "build"]);
const server = spawn(process.execPath, ["dist/server/entry.mjs"], { env, stdio: "inherit" });
let serverError;
server.on("error", error => { serverError = error; });
try {
  let ready = false;
  for (let attempt = 0; attempt < 30; attempt++) {
    if (serverError) throw serverError;
    if (server.exitCode !== null) throw new Error("Snapshot server stopped");
    try { ready = (await fetch("http://localhost:4333/posts")).ok; } catch {}
    if (ready) break;
    await new Promise(resolve => setTimeout(resolve, 500));
  }
  if (!ready) throw new Error("Snapshot server did not become ready");
  await run("python3", ["scripts/export-design-preview.py"]);
} finally {
  server.kill("SIGTERM");
}
