.PHONY: build

hello:
	@echo "Hello World"

build:
	@python setup.py sdist
	@python setup.py bdist_wheel
