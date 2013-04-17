# -*- coding: utf-8 -*-
"""Health checks for hospital project."""
import sys

import pkg_resources

from hospital import HealthCheck


class PythonVersionHealthCheck(HealthCheck):
    """Make sure hospital runs on supported Python version.

    .. note::

       An unit test makes sure hospital declares supported Python versions.

    """
    def test_python_version(self):
        """hospital supports environment's Python version."""
        supported_versions = ['2.7']
        current_version = '{0!s}.{1!s}'.format(*sys.version_info[0:2])
        self.assertTrue(current_version in supported_versions)
