# -*- coding: utf-8 -*-
"""Health checks for hospital project."""
from hospital import HealthCheck


class PredictableHealthCheck(HealthCheck):
    """Health check that give predictable results.

    Useful to check that health checks can be run, discovered, or to check
    their output.

    """
    def test_true(self):
        """Health checks are collected."""
        self.assertTrue(True)
