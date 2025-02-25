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

file := *.py *.ipynb

format:
	nbqa black $(file)

update_packages:
	# https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#updating-an-environment
	mamba env update --file extras/environment.yml --prune

	./extras/scripts/update_lectures.sh

	echo "Please update homework notebooks separately, in python-public-policy-assignments"
