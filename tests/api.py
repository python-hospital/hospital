# -*- coding: utf-8 -*-
"""Test suite around :mod:`hospital.api` and deprecation plan."""
import unittest


def assert_module_attributes(module_path, attribute_names):
    """Assert imported ``module_path`` has ``attribute_names``."""
    module = __import__(module_path, globals(), locals(), '*')
    missing_attributes = []
    for attribute_name in attribute_names:
        if not hasattr(module, attribute_name):
            missing_attributes.append(attribute_name)
    if missing_attributes:
        raise AssertionError(
            'Missing attributes in "{module}": {attributes}'.format(
                module=module_path,
                attributes=', '.join(missing_attributes)))


class APITestCase(unittest.TestCase):
    """Check hospital's API."""
    def test_hospital_api(self):
        """API is exposed in `hospital` package.

        The goal of this test is to make sure that main items of project's API
        are easy to import... and prevent refactoring from breaking main API.

        If this test is broken by refactoring, a :class:`DeprecationWarning` or
        simimar should be raised.

        """
        api = [
            # Core.
            'HealthCheck',
            'healthcheck',
            'is_healthcheck',
            # Assertions.
            'assert_http_response',
            'assert_ping',
            'assert_supported_python_version',
            # HealthChecks.
            'DistributionHealthCheck',
            'ForeverPassingHealthCheck']
        assert_module_attributes('hospital', api)
