$(() => {
  const inputEl = $("#url");
  const countEl = $('input[name="count"]');
  const warningEl = $("#data-shortener-widget .warning");
  const downloadEl = $("#download");

  // https://getbootstrap.com/docs/4.0/components/buttons/#active-state
  const activeClasses = "active btn-primary";
  const disabledClasses = "disabled btn-secondary";

  const updateDownload = () => {
    const inputText = inputEl.val();

    // https://support.socrata.com/hc/en-us/articles/202950258-What-is-a-Dataset-UID-or-a-Dataset-4x4-
    const matches = inputText.match(
      /^https:\/\/.*\/([A-Za-z0-9]{4}-[A-Za-z0-9]{4})\b/
    );

    if (matches) {
      // appears to be a Socrata URL

      const uid = matches[1];
      const inputUrl = new URL(inputText);
      const numRows = countEl.val();
      const newUrl = `https://${inputUrl.hostname}/resource/${uid}.csv?$limit=${numRows}`;

      downloadEl.attr("href", newUrl);
      downloadEl
        .addClass(activeClasses)
        .removeClass(disabledClasses)
        .removeAttr("aria-disabled");

      warningEl.hide();
    } else {
      downloadEl.attr("href", "");
      downloadEl
        .addClass(disabledClasses)
        .removeClass(activeClasses)
        .attr("aria-disabled", "true");

      warningEl.show();
    }
  };

  inputEl.on("input", updateDownload);
  countEl.on("input", updateDownload);
  updateDownload();
});
