# -*- coding: utf-8 -*-
"""Assertions related to Python packaging."""
from hospital.utils.packaging import python_runtime_version
from hospital.utils.packaging import supports_python_version


def assert_supported_python_version(distribution, version=None, msg=None):
    """Assert that ``distribution`` claims support for Python ``version``.

    Typically used to check theorical compatibility between runtime Python
    version and installed Python software.

    distribution
      Distribution object, as returned by ``pkg_resources.get_distribution()``.

      >>> from hospital import assert_supported_python_version
      >>> import pkg_resources
      >>> hospital_dist = pkg_resources.get_distribution('hospital')
      >>> assert_supported_python_version(hospital_dist)

    version
      Python version, as a string. If omitted or `None` (the default), the
      current Python version is retrieved from ``sys.version_info``.

      As an example, `hospital` claims support for Python 2.7 and 3.3, but not
      for version 2.6.

      >>> assert_supported_python_version(hospital_dist, version='2.7')
      >>> assert_supported_python_version(hospital_dist, version='3.3')
      >>> try:
      ...     assert_supported_python_version(hospital_dist, version='2.6')
      ... except AssertionError:
      ...     pass

    See also :class:`~hospital.healthchecks.packaging.DistributionHealthCheck`.

    """
    if version is None:
        version = python_runtime_version()
    if msg is None:
        msg = "Python distribution of {distribution} does not claim support " \
              "of Python version {version}".format(distribution=distribution,
                                                   version=version)
    assert supports_python_version(distribution, version) is True, msg
