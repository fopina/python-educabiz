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

genmodel:
	datamodel-codegen  --input temp.json --input-file-type json --output tmp_model.py --allow-extra-fields --force-optional
