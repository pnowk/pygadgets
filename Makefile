
build: 
	python setup.py sdist bdist_wheel

test: 
	python -m pytest -v -s ./tests

format:
	python -m black ./pygadgets
