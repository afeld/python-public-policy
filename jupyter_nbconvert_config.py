"""nbconvert settings for slides, used by `make slides` and the myst-slides plugin."""

# some slides are too tall to fit, such as those with long outputs
c.SlidesExporter.reveal_scroll = True  # type: ignore[name-defined]  # noqa: F821
