lint:
	ruff format
	ruff check --fix
	pyproject-pipenv --fix

lint-check:
	ruff format --diff
	ruff check
	pyproject-pipenv

test:
	python -m pytest --cov

testpub:
	rm -fr dist
	pyproject-build
	twine upload --repository testpypi dist/*
