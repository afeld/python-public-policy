// MyST plugin that builds each lecture's slides with nbconvert and links to them from the top of its page. _static/styles.css moves the link into the page header as a button.
//
// MyST has no documented way for plugins to add build output, so this relies on its static folder, which ends up at /build/ on the site.
//
// https://mystmd.org/guide/plugins
// https://nbconvert.readthedocs.io/en/latest/usage.html#reveal-js-html-slideshow

import { execFileSync } from "node:child_process";
import { cpSync } from "node:fs";
import path from "node:path";

const OUTPUT_DIR = "_build/site/public";
// the slides reference media by its source path, unlike the site's pages
const MEDIA_DIR = "extras/img";

/** The slides' filename for a notebook, or null if it isn't a lecture. */
export function slidesFilename(file) {
  const name = path.basename(file);
  return /^lecture_\d\.ipynb$/.test(name)
    ? name.replace(/\.ipynb$/, ".slides.html")
    : null;
}

function buildSlides(file) {
  execFileSync(
    "jupyter",
    [
      "nbconvert",
      "--to=slides",
      "--SlidesExporter.reveal_scroll=True",
      `--output-dir=${OUTPUT_DIR}`,
      file,
    ],
    { stdio: "pipe" },
  );
  cpSync(MEDIA_DIR, path.join(OUTPUT_DIR, MEDIA_DIR), { recursive: true });
}

const transform = {
  name: "slides",
  doc: "Build slides for lectures and link to them",
  // after links are resolved, so that MyST leaves this one alone
  stage: "project",
  plugin: () => (tree, file) => {
    const filename = slidesFilename(file.path ?? "");
    if (!filename) {
      return;
    }
    buildSlides(file.path);

    tree.children.unshift({
      type: "block",
      class: "slides-link",
      children: [
        {
          type: "paragraph",
          children: [
            {
              type: "link",
              url: `/${filename}`,
              // served as a file rather than a page of the site, which has the theme add the base URL and /build
              static: true,
              children: [{ type: "text", value: "View as slides" }],
            },
          ],
        },
      ],
    });
  },
};

export default {
  name: "Slides",
  transforms: [transform],
};
