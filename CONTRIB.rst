########################
Contributing to hospital
########################


*********************
Setup DEV environment
*********************

Here is the recipe to setup and use default development environment:

* Install prerequisites:

  * Python version 2.7 and 3.3 (both versions are tested)
  * Git
  * virtualenv
  * make

* Clone `hospital` repository (may be your fork):

  .. code:: sh

     git clone git@github.com:python-hospital/hospital.git
     cd hospital/

* Bootstrap development environment:

  .. code:: sh

     make develop

* Run tests:

  .. code:: sh

     make test

.. note::

   The :file:`Makefile` is the reference card for common actions in development
   environment.
