lab:
	jupyter lab

notebook:
	jupyter notebook

linkcheck:
	ruby ./extras/scripts/broken_links.rb

slides:
	jupyter nbconvert --to slides \
		--SlidesExporter.reveal_scroll=True \
		--post serve lecture_$(lec).ipynb

test:
	pytest

# overridden in update.sh
file := .

format:
	ruff format $(file)

# the URL the site will be served from, e.g. https://python-public-policy.afeld.me/en/columbia/
site_url :=

site:
	$(if $(site_url),,$(error site_url is required))
	jupyter-book build --html --ci --strict
	# these point to the temporary server used for the build (http://localhost:3000), so let Read the Docs generate them instead
	rm -f _build/html/robots.txt _build/html/sitemap.xml _build/html/sitemap_style.xsl
	# generate redirects from old Jupyter Book 1 URLs
	uv run --with click --with pyyaml \
		https://raw.githubusercontent.com/jupyter-book/jb1-redirect-generator/d70ce6d7df9f2dfc83bb1d409336c0cc3e20697f/generate_redirects.py \
		--base-url "$(site_url)" \
		--output-dir _build/html \
		--myst-config myst.yml

# school can be columbia, nyu, or omitted for both
preview:
	./extras/scripts/preview.sh $(school)

setup:
	uv sync
	uv pip install --python .venv/bin/python \
		-r extras/autograder/source/requirements.txt

update_packages:
	uv sync --upgrade

	./extras/scripts/update_lectures.sh

	@echo "Please update homework notebooks separately, in python-public-policy-assignments"

# based on https://gradescope-autograders.readthedocs.io/en/latest/manual_docker/
autograde:
	mkdir -p ./extras/autograder/results ./extras/autograder/results

	docker run --rm \
		-v ./extras/autograder:/autograder \
		gradescope/autograder-base \
		/bin/bash -c "/autograder/source/setup.sh && /autograder/source/run_autograder"

	cat ./extras/autograder/results/results.json

build_autograder:
	# https://stackoverflow.com/a/17351814/358804
	git archive -o ./extras/autograder.zip HEAD:./extras/autograder/source

	@echo "Now upload extras/autograder.zip to Gradescope."

build_dir := _build

clean:
	rm -rf $(build_dir)
