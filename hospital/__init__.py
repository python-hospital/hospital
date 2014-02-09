# -*- coding: utf-8 -*-
"""Hospital is a framework to write health checks around running services.

Health checks are meant to run on any live instance, such as a PROD
environment. They are part of the monitoring/supervision toolkit.

"""
import pkg_resources


#: Module version, as defined in PEP-0396.
__version__ = pkg_resources.get_distribution(__package__).version


# API shortcuts.
from hospital.api import *  # NoQA
