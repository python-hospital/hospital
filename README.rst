#################################
hospital: healthchecks for Python
#################################

`hospital` is a Python framework to write health checks, smoke tests or
diagnoses around applications or services.


********
Abstract
********

Health checks are kind of tests, applied to running applications and services:

* write healtchecks just as you would write tests, using assertions;
* collect and run healthchecks with test runners;
* use healthchecks to validate deployments;
* plug healthchecks in supervision and monitoring tools;
* in case of incidents, use healthchecks to diagnose problems.


*******
Example
*******

In your project's root package, have a ``healthchecks`` package or module,
where you assert your (running) application or service is ok:

.. code:: python

   import unittest
   import hospital

   @hospital.healthcheck
   class DocumentationHealthCheck(unittest.TestCase):
       def test_http_200(self):
           url = 'http://hospital.readthedocs.org/en/0.6/'
           hospital.assert_http_response(url, status_code=200)

Then you can collect and run the healthchecks with command line or web
service. Here is an example with command line:

.. code:: console

   $ hospital-cli <YOUR-PACKAGE>.healthchecks


**************
Project status
**************

`hospital` is not full-featured yet. Some important features are in the
`roadmap <https://github.com/python-hospital/hospital/issues/milestones>`_.
See also `vision
<http://hospital.readthedocs.org/en/latest/about/vision.html>`_.

Of course, any ideas, feedback or help are welcome :)


*********
Resources
*********

* Documentation: https://hospital.readthedocs.org
* IRC: ``#python-hospital`` on freenode
* Mailing-list: ``pythonhospital@librelist.com``,
  see archives at http://librelist.com/browser/pythonhospital/
* PyPI page: https://pypi.python.org/pypi/hospital
* Code repository: https://github.com/python-hospital/hospital
* Continuous integration: https://travis-ci.org/python-hospital/hospital
* Bugs & feature requests: https://github.com/python-hospital/hospital/issues
* Changelog: https://hospital.readthedocs.org/en/latest/about/changelog.html
* Roadmap: https://github.com/python-hospital/hospital/milestones
