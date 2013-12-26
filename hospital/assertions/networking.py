# -*- coding: utf-8 -*-
"""Assertions related to networking."""
from hospital.utils.networking import ping


def assert_ping(host, timeout=1):
    """Assert ``host`` responds to ping within ``timeout``."""
    assert ping(host, timeout) is True
