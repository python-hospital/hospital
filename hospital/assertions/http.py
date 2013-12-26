# -*- coding: utf-8 -*-
"""Assertions around HTTP resources."""
import requests


def assert_http_response(url, status_code=200, timeout=1):
    """Assert that GET ``url`` returns ``status_code`` within ``timeout``."""
    try:
        response = requests.get(url, timeout=timeout, stream=True)
    except requests.exceptions.RequestException as e:
        raise AssertionError(e)
    assert response.status_code is status_code
