#################################
hospital: healthchecks for Python
#################################

`hospital` makes it easy to setup and use health checks in Python.

Health checks are kind of tests applied to running applications and services.

**********
Quickstart
**********

Write health checks
===================

Write health checks just like you would write tests. The main difference is
their scope: they check "production" facts instead of mocks/fakes/dummies.

Health checks are special kind of tests. Use :func:`~hospital.core.healthcheck`
decorator to differenciate health checks from tests.

Just like tests, health checks can be simple functions that perform assertions:

.. code:: python

   import sys
   import hospital

   @hospital.healthcheck
   def test_python_version():
       """Python version >= 2."""
       assert sys.version_info[0] >= 2

You can reuse test libraries, like :mod:`unittest`:

.. code:: python

   import unittest
   import hospital

   @hospital.healthcheck
   class DocumentationHealthCheck(unittest.TestCase):
       """Check `hospital` online documentation."""
       def test_ping(self):
           """`hospital` documentation server responds to ping."""
           hostname = 'hospital.readthedocs.org'
           hospital.assert_ping(hostname)

       def test_http_200(self):
           """`hospital` online documentation returns HTTP 200."""
           url = 'http://hospital.readthedocs.org/en/0.1/'
	   hospital.assert_http_response(url, status_code=200)

`Hospital` provides a set of useful assertions and health check suites.

Run health checks
=================

Run health checks to make sure everything is ok. As an example, run health
checks after a deployment to verify configuration, services...

Health checks are tests having a ``is_healthcheck`` attribute which is
``True``. Let's use this feature to capture and run the tests.

With `nose` (here we run health checks of `hospital` project):

.. code:: sh

   nosetests --no-path-adjustment --all-modules --attr="is_healthcheck" hospital

.. tip::

   You may want to skip health checks when you run unit/functional/integration
   tests. With `nose`, it could be:

   .. code:: sh

      nosetests --no-path-adjustment --all-modules --attr="!is_healthcheck" hospital

Plug in supervision, monitoring
===============================

Include health checks in supervision/monitoring tools.

Diagnose
========

In case of incidents, use health checks to diagnose problems.


*********
Resources
*********

* Documentation: https://hospital.readthedocs.org
* IRC: ``#python-hospital`` on freenode
* Mailing-list: ``pythonhospital@librelist.com``,
  see archives at http://librelist.com/browser/pythonhospital/
* PyPI page: https://pypi.python.org/pypi/hospital
* Code repository: https://github.com/python-hospital/hospital
* Bugs & feature requests: https://github.com/python-hospital/hospital/issues
* Roadmap: https://github.com/python-hospital/hospital/issues/milestones
* Continuous integration: https://travis-ci.org/python-hospital/hospital
