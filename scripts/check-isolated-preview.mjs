import assert from "node:assert/strict";
import { stat } from "node:fs/promises";
import { presentationRecaps } from "../src/utils/people.ts";

assert.deepEqual(presentationRecaps(null), [], "Missing member recaps do not crash the directory");

// Deliberately fixed to this local preview; this check never writes CMS content.
const origin = "http://localhost:4331";
assert.ok((await stat(".preview/techies.db")).size > 0, "Local preview database exists");
assert.ok((await stat(".preview/uploads")).isDirectory(), "Local media directory exists");
for (const path of ["/", "/events", "/people", "/posts", "/posts/roast-7"]) {
  const response = await fetch(`${origin}${path}`);
  assert.equal(response.status, 200, `${path}: renders`);
  const html = await response.text();
  assert.match(html, /<meta\s+[^>]*name="robots"[^>]*content="noindex, nofollow"/, `${path}: excluded from indexing`);
  assert.equal((html.match(/<h1(?:\s|>)/g) || []).length, 1, `${path}: one H1`);
  const links = [...html.matchAll(/<a\b[^>]*>([\s\S]*?)<\/a>/g)];
  for (const [, label] of links) assert.doesNotMatch(label.replace(/<[^>]+>/g, ""), /[↗→←↓]\s*$/, `${path}: plain link labels`);
  console.log(`PASS ${path}: renders, noindex, one H1, plain links`);
}
