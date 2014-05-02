# Reference card for usual actions in development environment.
#
# For standard installation of hospital as a library, see INSTALL.
# For details about hospital's development environment, see CONTRIBUTING.rst.
#
PIP = pip
TOX = tox


.PHONY: help develop clean distclean maintainer-clean test test-app healthcheck sphinx readme documentation release


#: help - Display callable targets.
help:
	@echo "Reference card for usual actions in development environment."
	@echo "Here are available targets:"
	@egrep -o "^#: (.+)" [Mm]akefile  | sed 's/#: /* /'


#: develop - Install minimal development utilities such as tox.
develop:
	$(PIP) install tox
	$(PIP) install -e ./


#: clean - Basic cleanup, mostly temporary files.
clean:
	find . -name "*.pyc" -delete
	find . -name "__pycache__" -delete
	find . -name ".noseids" -delete


#: distclean - Remove local builds, such as *.egg-info.
distclean: clean
	rm -rf *.egg
	rm -rf *.egg-info


#: maintainer-clean - Remove almost everything that can be re-generated.
maintainer-clean: distclean
	rm -rf bin/
	rm -rf lib/
	rm -rf build/
	rm -rf dist/
	rm -rf .tox/


#: test - Run all test suite.
test:
	$(TOX)


#: test-app - Run unit tests.
test-app:
	$(TOX) -e py27,py33


#: healthcheck - Run hospital's own healthchecks.
healthcheck:
	$(TOX) -e healthcheck


#: sphinx - Build Sphinx documentation in var/docs/html
sphinx:
	$(TOX) -e sphinx


#: readme - Build standalone documentation files (README, CONTRIBUTING...).
readme:
	$(TOX) -e readme


#: documentation - Build standalone documentation files and Sphinx docs.
documentation: sphinx readme


#: release - Tag and push to PyPI.
release:
	$(TOX) -e release
