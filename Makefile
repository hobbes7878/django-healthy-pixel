test:
	pytest -v

ship:
	python setup.py sdist bdist_wheel
	twine upload dist/* --skip-existing

dev:
	gulp --cwd pixel/staticapp/

database:
	dropdb pixel --if-exists
	createdb pixel
