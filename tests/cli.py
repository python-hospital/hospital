# -*- coding: utf-8 -*-
"""Tests around :mod:`hospital.cli`."""
import unittest
import sys

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
    def test_output(self):
        """HealthCheckProgram runs healthchecks."""
        stream = StringIO()
        cli.main(
            args=['hospital.healthchecks.predictable'],
            stream=stream)
        output = stream.getvalue()
        self.assertTrue(output.startswith(
            '.\n'
            '-------------------------------------'
            '---------------------------------\n'
            'Ran 1 test in '))
        self.assertTrue(output.endswith('s\n\nOK\n'))

    def test_discovery_module(self):
        """HealthCheckProgram discovers tests in package."""
        stream = StringIO()
        cli.main(
            args=['hospital.healthchecks'],
            stream=stream)
        output = stream.getvalue()
        self.assertTrue(output.startswith(
            '..\n'
            '-------------------------------------'
            '---------------------------------\n'
            'Ran 2 tests in '))
        self.assertTrue(output.endswith('s\n\nOK\n'))
