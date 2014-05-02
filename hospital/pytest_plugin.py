from hospital.core import is_healthcheck


def pytest_configure(config):
    register_healthcheck_marker(config)


def pytest_collection_modifyitems(session, config, items):
    for item in items:
        if is_healthcheck(item.cls) or is_healthcheck(item.function):
            item.add_marker("healthcheck")


def register_healthcheck_marker(config):
    """Register the "healthcheck" marker.
    """
    config_line = (
        "healthcheck: mark this test as a healthcheck. "
        "See also: http://pytest-ordering.readthedocs.org/"
    )
    config.addinivalue_line("markers", config_line)
