# -*- coding: utf-8 -*-
"""Unit tests around :mod:`hospital.assertions.packaging`.

.. :py:currentmodule:: hospital.assertions.packaging

"""
import pkg_resources
import unittest

from hospital.assertions import packaging


class AssertSupportedPythonVersionTestCase(unittest.TestCase):
    """Tests around :func:`assert_supported_python_version`."""
    def test_custom_msg(self):
        """assert_ping() accepts optional ``msg`` argument."""
        distribution = pkg_resources.get_distribution('hospital')
        version = '2.6'
        msg = "Custom message."
        # Make sure AssertionError is raised.
        with self.assertRaises(AssertionError) as context:
            packaging.assert_supported_python_version(
                distribution,
                version,
                msg=msg)
        # Let's check exception's message.
        self.assertEqual(context.exception.args[0], msg)
