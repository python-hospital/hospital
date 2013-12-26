# -*- coding: utf-8 -*-
"""Healthchecks: harmless tests (PROD compatible).

Health checks are meant to run on any live instance, such as a PROD
environment. They are part of the monitoring/supervision toolkit.

"""
import unittest


def healthcheck(test):
    """Make test a healthcheck and return it.

    Basically sets ``is_healthcheck`` attribute to ``True``.

    """
    is_healthcheck = property(
        fget=lambda obj: True,
        doc="""Custom attribute that identifies health checks.

            Allows easier selection of tests you want to run.
            See also `nose's attrib plugin`_ or `unittest's skip feature`_.

            .. _`nose's attrib plugin`:
               http://nose.readthedocs.org/en/latest/plugins/attrib.html
            .. _`unittest's skip feature`:
               http://docs.python.org/2/library/unittest.html#skipping-tests-and-expected-failures  # NoQA

            """
    )
    setattr(test, 'is_healthcheck', is_healthcheck)
    return test


@healthcheck
class HealthCheck(unittest.TestCase):
    """Base class for health checks, extends unittest.TestCase."""
