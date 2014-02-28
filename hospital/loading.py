# -*- coding: utf-8 -*-
"""Utilities to discover and load health checks."""
import os
import unittest
import sys

from hospital.core import is_healthcheck


class HealthCheckLoader(unittest.TestLoader):
    """Encapsulate HealthCheck loading.

    This is a special TestLoader which makes sure instances are actually
    health checks.

    """
    def is_healthcheck(self, value):
        """Return True if ``value`` is an health check.

        Default implementation uses :func:`hospital.core.is_healthcheck`.

        """
        return is_healthcheck(value)

    def filter_suite(self, suite):
        """Return copy of TestSuite where only health checks remain."""
        if isinstance(suite, unittest.TestSuite):
            suite_copy = self.suiteClass()
            for sub in suite:
                if isinstance(sub, unittest.TestSuite):
                    suite_copy.addTest(self.filter_suite(sub))
                else:
                    if self.is_healthcheck(sub):
                        suite_copy.addTest(sub)
        elif self.is_healthcheck(suite):
            suite_copy = suite.copy()
        return suite_copy

    def loadTestsFromTestCase(self, testCaseClass):
        """Load healthchecks from TestCase.

        Combines :meth:`unittest.TestLoader.loadTestsFromTestCase` and
        :meth:`filter_suite`.

        """
        suite = super(HealthCheckLoader, self).loadTestsFromTestCase(
            testCaseClass)
        return self.filter_suite(suite)

    def loadTestsFromModule(self, module, *args, **kwargs):
        """Load healthchecks from module.

        Combines :meth:`unittest.TestLoader.loadTestsFromModule` and
        :meth:`filter_suite`.

        """
        suite = super(HealthCheckLoader, self).loadTestsFromModule(
            module, *args, **kwargs)
        return self.filter_suite(suite)

    def loadTestsFromName(self, name, module=None):
        """Load healthchecks from name.

        Combines :meth:`unittest.TestLoader.loadTestsFromName` and
        :meth:`filter_suite`.

        """
        suite = super(HealthCheckLoader, self).loadTestsFromName(name, module)
        return self.filter_suite(suite)

    def loadTestsFromNames(self, names, module=None):
        """Load healthchecks from names.

        Combines :meth:`unittest.TestLoader.loadTestsFromNames` and
        :meth:`filter_suite`.

        """
        suite = super(HealthCheckLoader, self).loadTestsFromNames(names,
                                                                  module)
        return self.filter_suite(suite)

    def discover(self, start_dir, pattern='*', top_level_dir=None):
        try:
            __import__(start_dir)
        except ImportError:
            # Maybe a filename.
            return super(HealthCheckLoader, self).discover(
                start_dir=start_dir,
                pattern=pattern,
                top_level_dir=top_level_dir)
        else:
            start_module = sys.modules[start_dir]
            if os.path.basename(start_module.__file__).startswith('__init__.'):
                return super(HealthCheckLoader, self).discover(
                    start_dir=os.path.dirname(start_module.__file__),
                    pattern=pattern,
                    top_level_dir=None)
            else:  # It is a single module.
                return self.loadTestsFromModule(start_module)
