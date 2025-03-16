browser := chrome

lab:
	jupyter lab --browser $(browser)

notebook:
	jupyter notebook --browser $(browser)

linkcheck:
	ruby ./extras/scripts/broken_links.rb

slides:
	jupyter nbconvert --to slides \
		--SlidesExporter.reveal_scroll=True \
		--ServePostProcessor.browser $(browser) \
		--post serve lecture_$(lec).ipynb

test:
	pytest

# overridden in update.sh
file := .

format:
	ruff format $(file)

update_packages:
	# https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#updating-an-environment
	mamba env update --file extras/environment.yml --prune

	./extras/scripts/update_lectures.sh

	echo "Please update homework notebooks separately, in python-public-policy-assignments"

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

	echo "Now upload extras/autograder.zip to Gradescope."
