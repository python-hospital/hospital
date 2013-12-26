# -*- coding: utf-8 -*-
"""Healthchecks: harmless tests (PROD compatible).

Health checks are meant to run on any live instance, such as a PROD
environment. They are part of the monitoring/supervision toolkit.

"""
import unittest


def is_healthcheck(obj):
    """Return ``True`` if ``obj`` is an healthcheck."""
    try:
        return obj.is_healthcheck is True
    except AttributeError:
        return False


def healthcheck(test):
    """Make test a healthcheck and return it.

    Basically sets ``is_healthcheck`` attribute to ``True``.

    Can be used as a function-decorator:

    >>> @healthcheck
    ... def test_dummy():
    ...     pass
    >>> is_healthcheck(test_dummy)
    True

    Can be used as a class-decorator:

    >>> import unittest
    >>> @healthcheck
    ... class DummyTestCase(unittest.TestCase):
    ...     pass
    >>> is_healthcheck(DummyTestCase)
    True

    Can be used to modify instance:

    >>> def test_noop():
    ...     pass
    >>> is_healthcheck(test_noop)
    False
    >>> healthcheck_noop = healthcheck(test_noop)
    >>> is_healthcheck(healthcheck_noop)
    True

    """
    setattr(test, 'is_healthcheck', True)
    return test


@healthcheck
class HealthCheck(unittest.TestCase):
    """Base class for health checks, extends unittest.TestCase."""
