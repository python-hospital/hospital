# -*- coding: utf-8 -*-
"""Tests around Python packaging."""
import unittest


class PythonVersionTestCase(unittest.TestCase):
    """Tests around Python version."""
    def test_supported_versions_declaration(self):
        """hospital package declares supported Python versions."""
