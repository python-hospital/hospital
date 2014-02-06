# Reference card for usual actions in development environment.
#
# For standard installation of hospital as a library, see INSTALL.
# For details about hospital's development environment, see CONTRIBUTING.rst.


develop:
	pip install tox Sphinx docutils zest.releaser
	pip install -e ./


clean:
	find . -name "*.pyc" -delete
	find . -name "__pycache__" -delete
	find . -name ".noseids" -delete


distclean: clean
	rm -rf *.egg-info


maintainer-clean: distclean
	rm -rf bin/
	rm -rf lib/
	rm -rf build/
	rm -rf dist/
	rm -rf .tox/


test:
	tox


test-app:
	tox -e py27,py33


healthcheck:
	tox -e healthcheck


test-documentation:
	tox -e sphinx


sphinx:
	mkdir -p var/docs
	make --directory=docs clean html


documentation: sphinx


release:
	fullrelease
