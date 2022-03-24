FROM jupyter/minimal-notebook

USER root
RUN apt-get update && \
  apt-get install -y cloc
USER ${NB_UID}

COPY environment.lock.yml "/home/${NB_USER}"
# inspired by
# https://jupyter-docker-stacks.readthedocs.io/en/latest/using/recipes.html#slideshows-with-jupyter-and-rise
RUN mamba env update -f environment.lock.yml && \
  fix-permissions "${CONDA_DIR}" && \
  fix-permissions "/home/${NB_USER}"

# https://jupyter-docker-stacks.readthedocs.io/en/latest/using/common.html#switching-back-to-the-classic-notebook-or-using-a-different-startup-command
ENV DOCKER_STACKS_JUPYTER_CMD notebook
ENV NOTEBOOK_ARGS "--notebook-dir python-public-policy"
