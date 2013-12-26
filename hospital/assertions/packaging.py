# -*- coding: utf-8 -*-
"""Assertions related to Python packaging."""
from hospital.utils.packaging import supports_python_version


def assert_supported_python_version(distribution, version=None):
    """Assert that ``distribution`` claims support for Python ``version``.

    distribution
      Distribution object, as returned by ``pkg_resources.get_distribution()``.

    version
      Python version, as a string. If omitted or `None` (the default), the
      current Python version is retrieved from ``sys.version_info``.

    """
    assert supports_python_version(distribution, version) is True
