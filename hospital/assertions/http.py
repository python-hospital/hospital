# -*- coding: utf-8 -*-
"""Assertions around HTTP resources."""
import requests


def assert_http_response(url, status_code=200, timeout=1):
    """Assert that GET ``url`` returns ``status_code`` within ``timeout``.

    >>> from hospital.assertions.http import assert_http_response
    >>> assert_http_response('http://hospital.readthedocs.org', 200)

    Raises :class:`AssertionError` in case of failure.

    >>> assert_http_response('http://hospital.readthedocs.org', 401)
    ... # Doctest: +ELLIPSIS
    Traceback (most recent call last):
        ...
    AssertionError

    Use ``timeout`` argument as a ceil for tolerable latency (in seconds).

    >>> try:
    ...     assert_http_response('http://hospital.readthedocs.org',
    ...                          timeout=0.001)
    ... except AssertionError:
    ...     pass

    """
    try:
        response = requests.get(url, timeout=timeout, stream=True)
    except requests.exceptions.RequestException as e:
        raise AssertionError(e)
    assert response.status_code is status_code
