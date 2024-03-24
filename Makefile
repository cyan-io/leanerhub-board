default: install

clean:
	rm -r -f build/ dist/ *.egg-info/

install:
	pip install .

dev:
	pip install -e .

wheel:
	python setup.py bdist_wheel

upload:
	python -m twine upload dist/*