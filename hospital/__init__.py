# -*- coding: utf-8 -*-
"""hospital provides supervision/monitoring utilities for Python projects."""
import pkg_resources


#: Module version, as defined in PEP-0396.
__version__ = pkg_resources.get_distribution(__package__).version


# API.
import hospital.healthcheck


#: Shortcut to :py:class:`hospital.healthcheck.HealthCheck`.
HealthCheck = hospital.healthcheck.HealthCheck
