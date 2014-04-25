# -*- coding: utf-8 -*-
"""Tests for :py:mod:`hospital.loading` module."""
import unittest
try:
    from unittest import mock
except ImportError:  # Python 2.x fallback.
    import mock

from hospital import HealthCheck
from hospital.loading import HealthCheckLoader


class HealthCheckLoaderTestCase(unittest.TestCase):
    """Tests around :py:class:`hospital.loading.HealthCheckLoader`."""
    def test_is_health_check(self):
        """HealthCheckLoader.is_health_check checks ``is_healthcheck`` attr."""
        loader = HealthCheckLoader()

        self.assertTrue(loader.is_healthcheck(mock.Mock(is_healthcheck=True)))

        class FakeHealthCheck(HealthCheck):
            def test_fake(self):
                pass
        self.assertTrue(loader.is_healthcheck(FakeHealthCheck('test_fake')))

        class FakeTestCase(unittest.TestCase):
            def test_fake(self):
                pass
        self.assertFalse(loader.is_healthcheck(FakeTestCase('test_fake')))
