# -*- coding: utf-8 -*-
"""Tests around :mod:`hospital.wsgi`."""
import json
import unittest
try:
    from unittest import mock
except ImportError:  # Python 2 fallback.
    import mock

from hospital import wsgi


class HealthCheckAppTestCase(unittest.TestCase):
    """Tests around :class:`hospital.wsgi.HealthCheckApp`."""
    def test_response(self):
        """HealthCheckApp instance is a WSGI app that runs healthchecks."""
        app = wsgi.HealthCheckApp(names=['hospital.healthchecks.predictable'])
        environ = {}
        start_response = mock.Mock()
        response = app(environ, start_response)
        self.assertEqual(len(start_response.call_args[0]), 2)  # 2 args
        self.assertEqual(len(start_response.call_args[1]), 0)  # 0 kwargs
        status = start_response.call_args[0][0]
        headers = dict(start_response.call_args[0][1])
        self.assertEqual(status, '200 OK')
        self.assertEqual(headers['Content-Type'],
                         'application/json; charset=utf-8')
        self.assertTrue(int(headers['Content-Length']) > 0)
        report_data = json.loads(''.join(response))
        self.assertEqual(report_data['status'], 'pass')
        self.assertEqual(report_data['summary']['total'], 1)
        self.assertEqual(report_data['summary']['pass'], 1)
        self.assertEqual(report_data['summary']['fail'], 0)
        self.assertEqual(report_data['summary']['error'], 0)
        self.assertEqual(report_data['summary']['skip'], 0)
        self.assertEqual(report_data['summary']['expected_failure'], 0)
        self.assertEqual(report_data['summary']['unexpected_success'], 0)
