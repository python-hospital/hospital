# -*- coding: utf-8 -*-
"""Healthchecks related to networking."""
from hospital import HealthCheck
from hospital.utils.networking import ping


def assert_ping(test_case, host, timeout=5):
    """Make ``test_case`` assert ``host`` responds to ping."""
    test_case.assertTrue(ping(host, timeout))


class PingHealthCheck(HealthCheck):
    host = 'localhost'

    def test_ping(self):
        """Ping "{host}"."""
        assert_ping(self, self.host)
    test_ping.__doc__ = test_ping.__doc__.format(host=host)
