FROM jupyter/minimal-notebook

COPY environment.yml "/home/${NB_USER}"
# inspired by
# https://jupyter-docker-stacks.readthedocs.io/en/latest/using/recipes.html#slideshows-with-jupyter-and-rise
RUN mamba env update -n base -f environment.yml && \
  fix-permissions "${CONDA_DIR}" && \
  fix-permissions "/home/${NB_USER}"
