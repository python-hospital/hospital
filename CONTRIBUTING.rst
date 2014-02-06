########################
Contributing to hospital
########################


***********
Fork, clone
***********

Clone `hospital` repository (adapt to use your own fork):

.. code:: sh

   git clone git@github.com:python-hospital/hospital.git
   cd hospital/


*************
Usual actions
*************

The :file:`Makefile` is the reference card for usual actions in development
environment:

* Install development toolkit with `pip`_: ``make develop``.

* Run tests with `tox`_: ``make test``.

* Build documentation: ``make documentation``. It builds `Sphinx`_
  documentation in :file:`var/docs/html/index.html`.

* Run `hospital`'s own healthchecks: ``make healthcheck``.

* Release `hospital` project with `zest.releaser`_: ``make release``.

* Cleanup local repository: ``make clean``, ``make distclean`` and
  ``make maintainer-clean``.


.. rubric:: Notes & references

.. target-notes::

.. _`pip`: https://pypi.python.org/pypi/pip/
.. _`tox`: https://pypi.python.org/pypi/tox/
.. _`Sphinx`: https://pypi.python.org/pypi/Sphinx/
.. _`zest.releaser`: https://pypi.python.org/pypi/zest.releaser/
