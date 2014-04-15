# -*- coding: utf-8 -*-
"""Utilities to discover and load health checks."""
import importlib
import inspect
import pkgutil
import unittest

from hospital.core import is_healthcheck


def is_package(module):
    """Return True if module object is a package.

    >>> import hospital
    >>> is_package(hospital)
    True
    >>> import hospital.api
    >>> is_package(hospital.api)
    False

    """
    return inspect.getmodulename(module.__file__) == '__init__'


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

    def loadTestsFromPackage(self, package):
        """Discover and load tests from modules in package."""
        tests = []
        packages = pkgutil.walk_packages(package.__path__)
        for (loader, module_name, is_pkg) in packages:
            full_name = '{}.{}'.format(package.__name__, module_name)
            tests.append(self.loadTestsFromName(full_name))
            if is_pkg:
                sub_package = importlib.import_module(full_name)
                tests.append(self.loadTestsFromPackage(sub_package))
        suite = self.suiteClass(tests)
        return self.filter_suite(suite)

    def discover(self, start_dir, pattern='*', top_level_dir=None):
        """Discover healthchecks in either a package, module or directory."""
        try:
            module = importlib.import_module(start_dir)
        except ImportError:
            # Maybe a filename.
            return super(HealthCheckLoader, self).discover(
                start_dir=start_dir,
                pattern=pattern,
                top_level_dir=top_level_dir)
        else:
            if is_package(module):
                return self.loadTestsFromPackage(module)
            else:
                return self.loadTestsFromModule(module)
