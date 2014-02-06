# -*- coding: utf-8 -*-
"""Hospital is a framework to write health checks around running services."""
import pkg_resources


#: Module version, as defined in PEP-0396.
__version__ = pkg_resources.get_distribution(__package__).version


# API shortcuts.
from hospital.api import *  # NoQA
