install:
	poetry install
lint:
	poetry run flake8
build: 
	poetry build
publish: 
	poetry publish --dry-run
package-install: 
	pipx install --force dist/*.whl
linter:
	poetry run flake8 gendiff
tests:
	poetry run pytest -vv
make test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml tests