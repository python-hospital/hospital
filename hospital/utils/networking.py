# -*- coding: utf-8 -*-
"""Utilities related to networking."""
import subprocess


def ping(host, timeout=30):
    """Return ``True`` if ``host`` responds to ping before ``timeout``."""
    command = ['ping', '-c', '1', '-q', '-W', str(timeout), host]
    try:
        process = subprocess.Popen(command,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE)
    except OSError:
        raise NotImplementedError("Couldn't run `ping` command.")
    return_code = process.wait()
    return return_code is 0
