# -*- coding: utf-8 -*-
"""Utilities to discover and load health checks."""
import unittest


class HealthCheckLoader(unittest.TestLoader):
    """Encapsulate HealthCheck loading.

    This is a special TestLoader which makes sure instances are actually
    health checks.

    .. warning::

       Since this loader can be called with arguments provided by users (GET
       requests), **we have to make sure user input is safe**.
       As an example, we can't accept to load health checks from any callable,
       because this callable could be anything.

    """
    def is_health_check(self, value):
        """Return True if ``value`` is an health check.

        Tests ``is_healthcheck`` attribute of ``value``.

        """
        try:
            return value.is_healthcheck
        except AttributeError:
            return False

    def filter_suite(self, suite):
        """Return copy of TestSuite where only health checks remain."""
        if isinstance(suite, unittest.TestSuite):
            suite_copy = self.suiteClass()
            for sub in suite:
                if isinstance(sub, unittest.TestSuite):
                    suite_copy.addTest(self.filter_suite(sub))
                else:
                    if self.is_health_check(sub):
                        suite_copy.addTest(sub)
        elif self.is_health_check(suite):
            suite_copy = suite.copy()
        return suite_copy

    def loadTestsFromModule(self, module):
        suite_tree = super(HealthCheckLoader, self).loadTestsFromModule(module)
        return self.filter_suite(suite_tree)

    def loadTestsFromName(self, name, module=None):
        """Same as unittest.TestLoader.loadTestsFromName, but restricted
        to health test objects, i.e. no callable allowed."""
        parts = name.split('.')
        if module:
            parts.insert(0, module)
        name = '.'.join(parts)
        # First, retrieve a module.
        module_obj = None
        path_parts = []
        while parts:
            latest_part = parts.pop(0)
            path_parts.append(latest_part)
            path = '.'.join(path_parts)
            try:
                imported_obj = __import__(path, globals(), locals(), [], -1)
            except ImportError as module_exception:
                if not module_obj:
                    raise module_exception
                else:
                    path_parts.pop()  # Last part is not a module.
                    path = '.'.join(path_parts)
                    break
            else:
                if not module_obj:
                    module_obj = imported_obj
                else:
                    module_obj = getattr(module_obj, latest_part)
        # We got ``module_obj`` for ``path``.
        # Let's retrieve members.
        parts = name[len(path):].lstrip('.')
        if not parts:
            return self.loadTestsFromModule(module_obj)
        else:
            parts = parts.split('.')
        class_name = parts[0]
        try:
            class_obj = getattr(module_obj, class_name)
        except AttributeError:
            raise ImportError("Couldn't load '%s'" % name)
        if not self.is_health_check(class_obj):
            raise ImportError("'%s' is not a health check" % name)
        try:
            method_name = parts[1]
        except IndexError:
            return self.loadTestsFromTestCase(class_obj)
        else:
            try:
                getattr(class_obj, method_name)
            except AttributeError:
                raise AttributeError(
                    "'{0}' is not a health check method".format(name))
            return unittest.TestSuite([class_obj(method_name)])

    def loadTestsFromNames(self, names, module=None):
        raise NotImplementedError()
