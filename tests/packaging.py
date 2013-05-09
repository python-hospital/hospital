# -*- coding: utf-8 -*-
"""Tests around Python packaging."""
import pkg_resources
import unittest

from hospital.utils.packaging import (assert_supported_python_version,
                                      get_supported_python_versions)


class PythonVersionTestCase(unittest.TestCase):
    """Tests around Python version."""
    def setUp(self):
        """Setup working distribution."""
        self.distribution = pkg_resources.get_distribution('hospital')

    def test_supported_versions_declaration(self):
        """hospital distribution declares supported Python versions."""
        versions = get_supported_python_versions(self.distribution)
        self.assertTrue(versions)

    def test_environment_support(self):
        """hospital claims support for Python version used to run this test."""
        assert_supported_python_version(self, self.distribution)
