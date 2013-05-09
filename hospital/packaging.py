# -*- coding: utf-8 -*-
"""Healthchecks related to packaging."""
import pkg_resources

from hospital import HealthCheck
from hospital.utils.packaging import assert_supported_python_version


class DistributionHealthCheck(HealthCheck):
    """Several checks related to project's distribution.

    The simplest way to reuse this healthcheck is to inherit from it and
    customize the :py:attr:`distribution_name` attribute.

    """
    #: Distribution name.
    #: This is a class attribute in order to share it between test methods.
    distribution_name = 'hospital'

    #: Distribution instance.
    #: This is a class attribute in order to share it between test methods.
    #: It is to be populated by :py:meth:`get_distribution` during setup.
    distribution = None

    def get_distribution(self):
        """Return distribution instance from :py:attr:`distribution_name`."""
        return pkg_resources.get_distribution(self.distribution_name)

    def setUp(self):
        """Setup :py:attr:`distribution`."""
        self.distribution = self.get_distribution()

    def test_python_version(self):
        """Make sure project runs on supported Python version.

        This healthcheck focuses on compatibility of project within
        environments that actually use it, whereas unit tests take care of:

        * supported Python versions declaration (setup.py, setup.cfg).
        * project was developed within supported environment(s).

        """
        assert_supported_python_version(self, self.distribution)
