
build: 
	python setup.py sdist bdist_wheel

test: 
	python -m pytest -v ./tests
