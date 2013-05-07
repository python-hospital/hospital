# -*- coding: utf-8 -*-
"""Health checks for hospital project."""
import sys

import pkg_resources

from hospital import HealthCheck
from hospital.packaging import supports_python_version


class PythonVersionHealthCheck(HealthCheck):
    """Make sure hospital runs on supported Python version.

    .. note::

       An unit test makes sure ``hospital`` declares supported Python versions.
       Another unit test makes sure ``hospital`` supports ``hospital``'s own
       development environment.
       This healthcheck focuses on compatibility of ``hospital`` within
       environments that use it.

    """
    def test_python_version(self):
        """hospital supports environment's Python version."""
        distribution = pkg_resources.get_distribution('hospital')
        version = '{0!s}.{1!s}'.format(*sys.version_info[0:2])
        self.assertTrue(supports_python_version(distribution, version))
