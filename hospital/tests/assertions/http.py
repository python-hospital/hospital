# -*- coding: utf-8 -*-
"""Unit tests around :mod:`hospital.assertions.http`."""
import unittest

from hospital.assertions import http


class AssertHttpResponseTestCase(unittest.TestCase):
    """Tests around :func:`hospital.assertions.http.assert_http_response`."""
    def test_timeout_error(self):
        """assert_http_response() fails if nothing received within timeout."""
        url = 'http://hospital.readthedocs.org'
        timeout = 0.0001
        # Make sure AssertionError is raised.
        with self.assertRaises(AssertionError) as context:
            http.assert_http_response(url, timeout=timeout)
        # Let's check exception's message contains important information.
        message = str(context.exception)
        self.assertIn(url, message)
        self.assertIn('timed out', message)
        self.assertIn('timeout', message)
        self.assertIn(str(timeout), message)
