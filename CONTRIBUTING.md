# Contributing

1. Install Python 3.8.
1. [Install Pipenv.](https://pipenv.pypa.io/en/latest/#install-pipenv-today)
1. Set up the environment:

   ```sh
   pipenv install
   ```

1. Start the Jupyter server:

   ```sh
   pipenv run jupyter notebook
   ```

## Slides

While the lecture notes can be viewed as a plain notebook, they are also [visible as slides](https://rise.readthedocs.io/en/stable/usage.html#running-a-slideshow).

## Notebook cleanup

To ensure that notebooks have the correct execution order and output, run them non-interactively.

```sh
./scripts/update.sh <file>.ipynb
```
