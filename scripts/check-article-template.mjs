import assert from "node:assert/strict";
import { articleTitle, articleOutline, headingId, withoutRepeatedLead } from "../src/utils/article.ts";
assert.equal(articleTitle("Roast My TechStack #7 · July 2, 2026 · Singapore"), "Roast My TechStack #7");
assert.equal(articleTitle("Community update · July 2, 2026"), "Community update · July 2, 2026");
const body = [
  { _type: "image", _key: "lead", asset: { _ref: "photo" } },
  { _type: "block", _key: "a", style: "h2", children: [{ text: "A builder" }], markDefs: [{ href: "/members#builder" }] },
  { _type: "block", _key: "b", style: "h2", children: [{ text: "A builder" }] },
  { _type: "block", _key: "c", style: "h3", children: [{ text: "Details" }] },
  { _type: "image", _key: "later", asset: { _ref: "photo" } },
];
const outline = articleOutline(body);
assert.equal(outline.length, 2);
assert.equal(outline[0].profile, "/members#builder");
assert.notEqual(outline[0].id, outline[1].id);
assert.equal(outline[0].id, headingId(body[1], 1));
assert.deepEqual(articleOutline(null), []);
const rendered = withoutRepeatedLead(body, "photo");
assert.equal(rendered.length, 4);
assert.equal(rendered.at(-1)._key, "later");
assert.equal(body.length, 5, "Stored body is not mutated");
assert.equal(withoutRepeatedLead(body, "unrelated"), body);
console.log("PASS: short imported titles, unique heading anchors, speaker source links, non-destructive lead suppression");
