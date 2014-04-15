# -*- coding: utf-8 -*-
"""Tests for :py:mod:`hospital.loading` module."""
import os
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

    def test_discovery_by_python_path(self):
        """HealthCheckLoader discovers healthchecks in Python packages."""
        loader = HealthCheckLoader()
        suite = loader.discover('hospital.healthchecks.predictable')
        self.assertEqual(suite.countTestCases(), 1)

    def test_discovery_of_module_by_python_path_in_stdlib(self):
        """HealthCheckLoader can scan locations in stdlib."""
        for location in ['datetime', 'xml']:  # A module and a package.
            loader = HealthCheckLoader()
            suite = loader.discover(location)
            self.assertEqual(suite.countTestCases(), 0)

    def test_discovery_of_module_by_python_path_outside_project(self):
        """HealthCheckLoader can scan locations outside working directory."""
        original_dir = os.getcwd()
        try:
            # Move to a place that is not parent of
            # 'hospital.healthchecks.predictable'.
            os.chdir(os.path.dirname(__file__))
            loader = HealthCheckLoader()
            suite = loader.discover('hospital')
            self.assertTrue(suite.countTestCases() > 0)
        finally:
            os.chdir(original_dir)
