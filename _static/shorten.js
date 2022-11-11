document.addEventListener("DOMContentLoaded", () => {
  document.getElementById("url").addEventListener("input", (event) => {
    const inputText = event.target.value;
    const outputEl = document.getElementById("url-result");

    // https://support.socrata.com/hc/en-us/articles/202950258-What-is-a-Dataset-UID-or-a-Dataset-4x4-
    const matches = inputText.match(
      /^https:\/\/.*\/([A-Za-z0-9]{4}-[A-Za-z0-9]{4})\b/
    );

    if (matches) {
      // appears to be a Socrata URL
      const uid = matches[1];
      const inputUrl = new URL(inputText);
      const numRows = 10000;
      const newUrl = `https://${inputUrl.hostname}/resource/${uid}.csv?$limit=${numRows}`;

      const msg = `Download first ${numRows.toLocaleString()} rows`;
      outputEl.innerHTML = `<a href="${newUrl}" class="btn btn-primary active" target="_blank">${msg}</a>`;
    } else {
      outputEl.innerHTML = "<em>Doesn't appear to be a valid dataset URL</em>";
    }
  });
});
