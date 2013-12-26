#################################
hospital: healthchecks for Python
#################################

``hospital`` makes it easy to setup and use health checks in Python.

Health checks are kind of tests applied to running applications and services.

**********
Quickstart
**********

Write health checks
===================

During development, inherit from :py:class:`hospital.HealthCheck` and write
health checks as you would write tests, i.e. using assertions:

.. code:: python

   import hospital

   class DocumentationHealthCheck(hospital.HealthCheck):
       """Check `hospital` online documentation."""
       def test_ping(self):
           """`hospital` documentation server responds to ping."""
           hostname = 'hospital.readthedocs.org'
           hospital.assert_ping(hostname)

       def test_http_200(self):
           """`hospital` online documentation returns HTTP 200."""
           url = 'http://hospital.readthedocs.org/en/0.1/'
	   hospital.assert_http_response(url, status_code=200)

.. note::

   :class:`~hospital.healthcheck.HealthCheck` is a subclass of
   :class:`unittest.TestCase` with an
   :attr:`~hospital.healthcheck.HealthCheck.is_healthcheck` attribute.

Run health checks
=================

After a deployment, run health checks to make sure everything went fine.

With nose (here we run health checks of hospital project):

.. code:: sh

   nosetests --no-path-adjustment --all-modules --attr="is_healthcheck"  hospital

.. note::

   Some third-party projects expose health checks on HTTP service, returning
   an HTTP 200 in case of success, or an HTTP 500 in case of any failure.
   See :doc:`about/alternatives`.


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
* PyPI page: https://pypi.python.org/pypi/hospital
* Code repository: https://github.com/python-hospital/hospital
* Bugtracker: https://github.com/python-hospital/hospital/issues
* Continuous integration: https://travis-ci.org/python-hospital/hospital
