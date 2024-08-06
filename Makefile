install:
	poetry install
lint:
	poetry run flake8 scripts
build: 
	poetry build
publish: 
	poetry publish --dry-run
package-install: 
	pipx install --force dist/*.whl