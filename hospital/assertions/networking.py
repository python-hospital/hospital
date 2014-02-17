# -*- coding: utf-8 -*-
"""Assertions related to networking."""
from hospital.utils.networking import ping


def assert_ping(host, timeout=1, msg=None):
    """Assert ``host`` responds to ping within ``timeout``.

    >>> from hospital import assert_ping
    >>> assert_ping('hospital.readthedocs.org')

    """
    if msg is None:
        msg = "Failed to ping {host} within {timeout}.".format(
            host=host,
            timeout=timeout)
    assert ping(host, timeout) is True, msg
