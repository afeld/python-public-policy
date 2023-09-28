# Data shortener widget

Paste in the URL of [a tabular dataset from the NYC Open Data Portal](https://data.cityofnewyork.us/browse?limitTo=datasets).

<p>
  <form>
    <div class="form-group">
      <input id="url" placeholder="https://data.cityofnewyork.us/..." style="width: 100%">
    </div>
    <div class="form-group">
      <label for="count">Max rows to download:</label>
      <input type="number" name="count" value="10000" required>
    </div>
  </form>
</p>
<p>
  <!-- https://getbootstrap.com/docs/4.0/components/buttons/ -->
  <a id="download" class="btn btn-secondary disabled" target="_blank" role="button" aria-disabled="true" data-proofer-ignore>Download</a>
</p>

```{note}
Under the hood, this tool uses the [SODA API](https://dev.socrata.com/docs/queries/limit.html), which we'll learn about in [Class 5](lecture_5.ipynb#example-311-requests-from-the-last-week). It works with any dataset from open data portals built on [Socrata](https://dev.socrata.com/). It won't work with non-tabular formats like Maps.
```
