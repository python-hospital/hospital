# -*- coding: utf-8 -*-
"""Test suite around hospital's API."""
import unittest


class APITestCase(unittest.TestCase):
    """Check hospital's API."""
    def test_healthcheck_class(self):
        """``from hospital import HealthCheck works.``"""
        from hospital import HealthCheck  # NoQA
