# -*- coding: utf-8 -*-
"""Predictable health checks, i.e. they always have the expected behaviour."""
import unittest

from hospital.core import healthcheck


@healthcheck
class ForeverPassingHealthCheck(unittest.TestCase):
    """Health check that forever passes.

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


@healthcheck
class ForeverSkippedHealthCheck(unittest.TestCase):
    """Healthcheck that is always skipped."""
    def test_skip(self):
        """Health checks can be skipped."""
        self.skipTest('This healthcheck is always skipped, just to make sure '
                      'healthchecks can be skipped.')
