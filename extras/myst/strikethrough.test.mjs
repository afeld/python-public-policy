import assert from "node:assert/strict";
import { test } from "node:test";

import { strikethrough } from "./strikethrough.mjs";

const text = (value) => ({ type: "text", value });
const del = (...children) => ({ type: "delete", children });
const paragraph = (...children) => ({ type: "paragraph", children });

const transform = (...children) => {
  const tree = paragraph(...children);
  strikethrough(tree);
  return tree.children;
};

test("strikes text between tildes", () => {
  assert.deepEqual(transform(text("a ~~b~~ c")), [
    text("a "),
    del(text("b")),
    text(" c"),
  ]);
});

test("strikes across sibling nodes, such as links", () => {
  const link = {
    type: "link",
    url: "https://example.com",
    children: [text("b")],
  };
  assert.deepEqual(transform(text("~~a "), link, text(" c~~")), [
    del(text("a "), link, text(" c")),
  ]);
});

test("strikes inside nested nodes", () => {
  assert.deepEqual(transform(paragraph(text("~~a~~"))), [
    paragraph(del(text("a"))),
  ]);
});

test("leaves inline code alone", () => {
  const code = { type: "inlineCode", value: "~~a~~" };
  assert.deepEqual(transform(code), [code]);
});

test("keeps unmatched tildes as text", () => {
  assert.deepEqual(transform(text("a ~~b")), [
    text("a "),
    text("~~"),
    text("b"),
  ]);
});
