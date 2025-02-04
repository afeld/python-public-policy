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
