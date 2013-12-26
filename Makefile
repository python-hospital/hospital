# Makefile for development.
# See INSTALL and docs/contribute/index.txt for details.
SHELL = /bin/bash
ROOT_DIR = $(shell pwd)
BIN_DIR = $(ROOT_DIR)/bin
DATA_DIR = $(ROOT_DIR)/var
LIB_DIR = $(ROOT_DIR)/lib
VIRTUALENV_DIR = $(LIB_DIR)/virtualenv
PYTHON = $(shell which python)
PROJECT = $(shell $(PYTHON) -c "import setup; print setup.NAME")
PIP = $(BIN_DIR)/pip
NOSE = $(BIN_DIR)/nosetests
SPHINX_BUILD = $(BIN_DIR)/sphinx-build
TOX = $(BIN_DIR)/tox


configure:
	# Configuration is stored in etc/ folder. Not generated yet.


develop: directories virtualenv bin-dir dev-environment 


directories:
	mkdir -p $(LIB_DIR)
	mkdir -p $(DATA_DIR)
	mkdir -p $(ROOT_DIR)/docs/_static


virtualenv:
	if [ ! -d $(VIRTUALENV_DIR)/bin/ ]; then virtualenv $(VIRTUALENV_DIR); fi


dev-environment:
	$(PIP) install -r etc/dev-environment.txt


bin-dir:
	rm -rf $(BIN_DIR)
	ln -s $(VIRTUALENV_DIR)/bin $(BIN_DIR)


clean:
	find $(ROOT_DIR)/ -name "*.pyc" -delete
	find $(ROOT_DIR)/ -name "__pycache__" -delete
	find $(ROOT_DIR)/ -name ".noseids" -delete


distclean: clean
	rm -rf $(ROOT_DIR)/*.egg-info


maintainer-clean: distclean
	rm -rf $(BIN_DIR)/
	rm -rf $(ROOT_DIR)/lib/
	rm -rf $(ROOT_DIR)/build/
	rm -rf $(ROOT_DIR)/dist/
	rm -rf $(ROOT_DIR)/.tox/


test:
	$(TOX)


test-app:
	$(TOX) -e py27,py33


healthcheck:
	$(TOX) -e healthcheck


test-documentation:
	$(TOX) -e sphinx


sphinx:
	make --directory=docs clean html doctest


documentation: sphinx


release:
	$(BIN_DIR)/fullrelease
