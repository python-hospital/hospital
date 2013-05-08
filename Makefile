# Makefile for development.
# See INSTALL and docs/contribute/index.txt for details.
SHELL = /bin/bash
ROOT_DIR = $(shell pwd)
BIN_DIR = $(ROOT_DIR)/bin
DATA_DIR = $(ROOT_DIR)/var
WGET = wget
PYTHON = $(shell which python)
PROJECT = $(shell $(PYTHON) -c "import setup; print setup.NAME")
BUILDOUT_CFG = $(ROOT_DIR)/etc/buildout.cfg
BUILDOUT_DIR = $(ROOT_DIR)/lib/buildout
BUILDOUT_VERSION = 1.7.1
BUILDOUT_BOOTSTRAP_URL = https://raw.github.com/buildout/buildout/$(BUILDOUT_VERSION)/bootstrap/bootstrap.py
BUILDOUT_BOOTSTRAP = $(BUILDOUT_DIR)/bootstrap.py
BUILDOUT_BOOTSTRAP_ARGS = -c $(BUILDOUT_CFG) --version=$(BUILDOUT_VERSION) --distribute buildout:directory=$(ROOT_DIR)
BUILDOUT = $(BIN_DIR)/buildout
BUILDOUT_ARGS = -N -c $(BUILDOUT_CFG) buildout:directory=$(ROOT_DIR)
NOSE = $(BIN_DIR)/nosetests


configure:
	# Configuration is stored in etc/ folder. Not generated yet.


develop: buildout


buildout:
	if [ ! -d $(BUILDOUT_DIR) ]; then mkdir -p $(BUILDOUT_DIR); fi
	if [ ! -f $(BUILDOUT_BOOTSTRAP) ]; then wget -O $(BUILDOUT_BOOTSTRAP) $(BUILDOUT_BOOTSTRAP_URL); fi
	if [ ! -x $(BUILDOUT) ]; then $(PYTHON) $(BUILDOUT_BOOTSTRAP) $(BUILDOUT_BOOTSTRAP_ARGS); fi
	$(BUILDOUT) $(BUILDOUT_ARGS)


clean:
	find $(ROOT_DIR)/ -name "*.pyc" -delete
	find $(ROOT_DIR)/ -name ".noseids" -delete


distclean: clean
	rm -rf $(ROOT_DIR)/*.egg-info


maintainer-clean: distclean
	rm -rf $(BIN_DIR)/
	rm -rf $(ROOT_DIR)/lib/


test: test-app test-documentation healthcheck


test-app:
	$(NOSE) --config=etc/nose.cfg --with-doctest --attr="!is_healthcheck" hospital tests


healthcheck:
	$(NOSE) --config=etc/nose.cfg --attr="is_healthcheck" hospital


test-documentation:
	$(NOSE) -c $(ROOT_DIR)/etc/nose.cfg sphinxcontrib.testbuild.tests
	rm $(ROOT_DIR)/.coverage


documentation: sphinx-apidoc sphinx-html


# Remove auto-generated API documentation files.
# Files will be restored during sphinx-build, if "autosummary_generate" option
# is set to True in Sphinx configuration file.
sphinx-apidoc-clean:
	find docs/api/ -type f \! -name "index.txt" -delete


sphinx-apidoc: sphinx-apidoc-clean
	$(BIN_DIR)/sphinx-apidoc --suffix txt --output-dir $(ROOT_DIR)/docs/api $(PROJECT)


sphinx-html:
	if [ ! -d docs/_static ]; then mkdir docs/_static; fi
	make --directory=docs clean html doctest


release:
	$(BIN_DIR)/fullrelease