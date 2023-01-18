// JupyterBook's Launch of JupyterHub functionality generates a nbgitpuller URL:
// https://jupyterbook.org/en/stable/interactive/launchbuttons.html#add-a-launch-on-jupyterhub-button
// This script switches that link to use the notebook URL in the synchronized repository.
window.addEventListener("load", () => {
  const launcher = document.querySelector(
    ".menu-dropdown-launch-buttons a[href*='git-pull']"
  );
  if (launcher) {
    // it's a page generated from a notebook

    const nbName = window.location.pathname.match(/\/(\w+)\.html/)[1];
    launcher.href = `https://padmgp-4506001-fall.rcnyu.org/user-redirect/notebooks/class_materials/${nbName}.ipynb`;
  }
});
