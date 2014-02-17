# -*- coding: utf-8 -*-
"""Assertions around HTTP resources."""
import requests


def assert_http_response(url, status_code=200, timeout=1, msg=None):
    """Assert that GET ``url`` returns ``status_code`` within ``timeout``.

    >>> from hospital import assert_http_response
    >>> assert_http_response('http://hospital.readthedocs.org', 200)

    Raises :class:`AssertionError` in case of failure.

    >>> assert_http_response('http://hospital.readthedocs.org', 401)
    ... # doctest: +ELLIPSIS
    Traceback (most recent call last):
        ...
    AssertionError: GET "..." returned 200 status code. Expected 401.

    Use ``timeout`` argument as a ceil for tolerable latency (in seconds).

    >>> assert_http_response('http://hospital.readthedocs.org', timeout=10)

    Default value for ``timeout`` is 1 second. This value was chosen with the
    idea that if you cannot get a response from external services within 1
    second, then there is a performance issue.

    """
    try:
        response = requests.get(url, timeout=timeout, stream=True)
    except requests.exceptions.RequestException as e:
        if msg is None:
            msg = "Failed to fetch URL {url}.\nException was: {exception}" \
                  .format(url=url, exception=e)
        raise AssertionError(msg)
    if msg is None:
        msg = 'GET "{url}" returned {real} status code. ' \
              'Expected {expected}.'.format(url=url,
                                            real=response.status_code,
                                            expected=status_code)
    assert response.status_code is status_code, msg
