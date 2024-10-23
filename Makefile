lint:
	ruff format
	ruff check --fix

test:
	python -m pytest --cov

testpub:
	rm -fr dist
	pyproject-build
	twine upload --repository testpypi dist/*
