# -*- coding: utf-8 -*-
"""Predictable health check, i.e. they always have the expected behaviour."""
from hospital import HealthCheck


class PredictableHealthCheck(HealthCheck):
    """Health check that give predictable results.

    Useful to check that health checks can be run, discovered, or to check
    their output.

    As an example, once you have setup your environment, you should be able to
    collect this health check and run it sucessfully, or it would mean there is
    something wrong with your setup... Configuration of health check discovery
    could be the cause.

    """
    def test_true(self):
        """Health checks are collected."""
        self.assertTrue(True)
