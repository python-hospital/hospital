# -*- coding: utf-8 -*-
"""Declaration of API shortcuts."""
from hospital.core import (HealthCheck,  # NoQA
                           healthcheck,
                           is_healthcheck)
# Assertions.
from hospital.assertions.http import assert_http_response  # NoQA
from hospital.assertions.networking import assert_ping  # NoQA
from hospital.assertions.packaging import (  # NoQA
    assert_supported_python_version)
# HealthChecks.
from hospital.healthchecks.packaging import DistributionHealthCheck  # NoQA
from hospital.healthchecks.predictable import ForeverPassingHealthCheck  # NoQA
