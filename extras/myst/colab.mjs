// MyST plugin that adds an "Open in Colab" link to the top of each notebook page, replacing Jupyter Book 1's Colab launch button. Points to the school branch, where the notebooks are already rendered for that school. _static/styles.css moves it into the page header as a button.
//
// https://mystmd.org/guide/plugins
//
// Can be removed once Jupyter Book 2 supports Colab launch buttons natively:
// https://github.com/jupyter-book/mystmd/issues/1174

import path from "node:path";

const REPO = "afeld/python-public-policy";
// filled in by extras/scripts/school.sh
const BRANCH = "{{school_slug}}";

const colabLink = {
  name: "colab-link",
  doc: "Add an Open in Colab link to notebooks",
  stage: "document",
  plugin: () => (tree, file) => {
    if (!file.path?.endsWith(".ipynb")) {
      return;
    }
    const nbPath = path.relative(process.cwd(), file.path).split(path.sep).join("/");
    const url = `https://colab.research.google.com/github/${REPO}/blob/${BRANCH}/${nbPath}`;

    tree.children.unshift({
      type: "block",
      class: "colab-link",
      children: [
        {
          type: "paragraph",
          children: [
            {
              type: "link",
              url,
              children: [{ type: "text", value: "Open in Colab" }],
            },
          ],
        },
      ],
    });
  },
};

export default {
  name: "Colab link",
  transforms: [colabLink],
};
