# -*- coding: utf-8 -*-
"""Unit tests around :mod:`hospital.assertions.networking`."""
import unittest

from hospital.assertions import networking


class AssertPingTestCase(unittest.TestCase):
    """Tests around :func:`hospital.assertions.networking.assert_ping`."""
    def test_timeout_error(self):
        """assert_ping() fails if nothing received within timeout."""
        host = 'i-do-not-exist'
        timeout = 1
        # Make sure AssertionError is raised.
        with self.assertRaises(AssertionError) as context:
            networking.assert_ping(host, timeout=timeout)
        # Let's check exception's message contains important information.
        message = str(context.exception)
        self.assertIn(host, message)
        self.assertIn('ping', message)
        self.assertIn(str(timeout), message)

    def test_custom_msg(self):
        """assert_ping() accepts optional ``msg`` argument."""
        host = 'i-do-not-exist'
        timeout = 1
        msg = "Custom message."
        # Make sure AssertionError is raised.
        with self.assertRaises(AssertionError) as context:
            networking.assert_ping(host, timeout=timeout, msg=msg)
        # Let's check exception's message.
        self.assertEqual(context.exception.args[0], msg)
