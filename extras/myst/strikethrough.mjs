// MyST plugin that renders ~~tilde~~ strikethroughs, so that notebooks can use the syntax that also works in Colab. The MyST parser supports them through its strikethrough extension, but that's off by default and can't be turned on from myst.yml, so this converts the text that's left over after parsing.
//
// https://mystmd.org/guide/plugins

const MARKER = "~~";

/** Replaces text between markers with delete nodes, throughout the tree. */
export function strikethrough(node) {
  if (!node.children) {
    return;
  }
  node.children.forEach(strikethrough);

  const result = [];
  let struck = null;
  const add = (child) => (struck ? struck.children : result).push(child);

  for (const child of node.children) {
    if (child.type !== "text" || !child.value.includes(MARKER)) {
      add(child);
      continue;
    }
    // the parts at odd positions are the ones following a marker, so the state flips before they're added. Struck content can include sibling nodes, such as links.
    child.value.split(MARKER).forEach((part, i) => {
      if (i > 0) {
        if (struck) {
          result.push(struck);
          struck = null;
        } else {
          struck = { type: "delete", children: [] };
        }
      }
      if (part) {
        add({ type: "text", value: part });
      }
    });
  }

  if (struck) {
    // no closing marker, so it wasn't a strikethrough
    result.push({ type: "text", value: MARKER }, ...struck.children);
  }
  node.children = result;
}

const transform = {
  name: "strikethrough",
  doc: "Convert ~~tilde~~ strikethroughs to delete nodes",
  stage: "document",
  plugin: () => (tree) => strikethrough(tree),
};

export default {
  name: "Strikethrough",
  transforms: [transform],
};
