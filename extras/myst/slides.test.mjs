import assert from "node:assert/strict";
import { test } from "node:test";

import { slidesFilename } from "./slides.mjs";

test("names the slides after the lecture", () => {
  assert.equal(
    slidesFilename("/repo/lecture_1.ipynb"),
    "lecture_1.slides.html",
  );
});

test("skips notebooks that aren't lectures", () => {
  for (const file of ["hw_2.ipynb", "lecture_1_exercise.ipynb", "index.md"]) {
    assert.equal(slidesFilename(file), null);
  }
});
