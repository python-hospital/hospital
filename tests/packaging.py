# -*- coding: utf-8 -*-
"""Tests around Python packaging."""
import pkg_resources
import sys
import unittest

import hospital.packaging


class PythonVersionTestCase(unittest.TestCase):
    """Tests around Python version."""
    def setUp(self):
        """Setup working distribution."""
        self.distribution = pkg_resources.get_distribution('hospital')

    def test_supported_versions_declaration(self):
        """hospital distribution declares supported Python versions."""
        versions = hospital.packaging.get_supported_python_versions(
            self.distribution)
        self.assertTrue(versions)

    def test_environment_support(self):
        """hospital supports Python version used to run this test."""
        version = '{0!s}.{1!s}'.format(*sys.version_info[0:2])
        self.assertTrue(hospital.packaging.supports_python_version(
            self.distribution, version))
