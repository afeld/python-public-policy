$(() => {
  const inputEl = $("#url");
  const countEl = $('input[name="count"]');
  const downloadEl = $("#download");

  // https://getbootstrap.com/docs/4.0/components/buttons/#active-state
  const activeClasses = "active btn-primary";
  const disabledClasses = "disabled btn-secondary";

  const urlPattern = RegExp("^https://.*/([A-Za-z0-9]{4}-[A-Za-z0-9]{4})\\b.*");

  const enableDownload = (url) => {
    downloadEl
      .attr("href", url)
      .addClass(activeClasses)
      .removeClass(disabledClasses)
      .removeAttr("aria-disabled");
  };

  const disableDownload = () => {
    downloadEl
      .attr("href", "")
      .addClass(disabledClasses)
      .removeClass(activeClasses)
      .attr("aria-disabled", "true");
  };

  const updateDownload = () => {
    const inputText = inputEl.val();
    // https://support.socrata.com/hc/en-us/articles/202950258-What-is-a-Dataset-UID-or-a-Dataset-4x4-
    const matches = inputText.match(urlPattern);

    if (inputEl[0].checkValidity() && countEl[0].checkValidity() && matches) {
      // appears to be a Socrata URL
      const uid = matches[1];
      const inputUrl = new URL(inputText);
      const numRows = countEl.val();
      const newUrl = `https://${inputUrl.hostname}/resource/${uid}.csv?$limit=${numRows}`;
      enableDownload(newUrl);
    } else {
      disableDownload();
    }
  };

  // remove escaping that's unnecessary for HTML
  // https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/source#description
  const htmlPattern = urlPattern.source.replace(/\\\//g, "/");
  inputEl.attr("pattern", htmlPattern);

  $("input")
    .on("input", updateDownload)
    .blur((event) => {
      event.target.reportValidity();
    });

  updateDownload();
});
