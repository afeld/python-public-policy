[Inherits](https://nbconvert.readthedocs.io/en/latest/customizing.html) from [the `lab` template](https://github.com/jupyter/nbconvert/tree/master/share/jupyter/nbconvert/templates/lab). To use:

```sh
jupyter nbconvert --to html --TemplateExporter.extra_template_basedirs=scripts/templates --template ppp <file>.ipynb
```
