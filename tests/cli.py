# -*- coding: utf-8 -*-
"""Tests around :mod:`hospital.cli`."""
import unittest
import sys
try:
    from unittest import mock
except ImportError:
    import mock

from six.moves import StringIO

from hospital import cli


class CaptureStdStreams(object):
    def __init__(self):
        self.stdout = StringIO()
        self.stderr = StringIO()

    def __enter__(self):
        self.stdout_backup = sys.stdout
        setattr(sys, 'stdout', self.stdout)
        self.stderr_backup = sys.stderr
        setattr(sys, 'stderr', self.stderr)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.stdout = self.stdout.getvalue()
        self.stderr = self.stderr.getvalue()
        sys.stdout.close()
        sys.stderr.close()
        sys.stdout = self.stdout_backup
        sys.stderr = self.stderr_backup


class HealthCheckProgramTestCase(unittest.TestCase):
    """Tests around :class:`hospital.cli.HealthCheckProgram`."""
    @mock.patch('sys.exit')
    def test_output(self, exit_mock):
        """HealthCheckProgram runs healthchecks."""
        stream = StringIO()
        cli.main(
            args=['hospital.healthchecks.predictable'],
            stream=stream)
        output = stream.getvalue()
        self.assertTrue(output.startswith(
            '.s\n'
            '-------------------------------------'
            '---------------------------------\n'
            'Ran 2 tests in '))
        self.assertTrue(output.endswith('s\n\nOK (skipped=1)\n'))
        exit_mock.assert_called_once_with(0)

    @mock.patch('sys.exit')
    def test_discovery_module(self, exit_mock):
        """HealthCheckProgram discovers tests in package."""
        stream = StringIO()
        cli.main(
            args=['hospital.healthchecks'],
            stream=stream)
        output = stream.getvalue()
        self.assertTrue(output.startswith(
            '..s\n'
            '-------------------------------------'
            '---------------------------------\n'
            'Ran 3 tests in '))
        self.assertTrue(output.endswith('s\n\nOK (skipped=1)\n'))
        exit_mock.assert_called_once_with(0)

    @mock.patch('hospital.healthchecks.predictable'
                '.ForeverPassingHealthCheck.test_true')
    @mock.patch('sys.exit')
    def test_failure(self, exit_mock, healthcheck_mock):
        """HealthCheckProgram exits with code 1 on failure."""
        healthcheck_mock.side_effect = AssertionError
        stream = StringIO()
        cli.main(
            args=['hospital.healthchecks.predictable'],
            stream=stream)
        output = stream.getvalue()
        self.assertTrue(output.startswith('Fs\n'))
        self.assertIn('Ran 2 tests in ', output)
        self.assertTrue(output.endswith(
            's\n\nFAILED (failures=1, skipped=1)\n'))
        exit_mock.assert_called_once_with(1)
