from .core import is_healthcheck


def pytest_configure(config):
    """Register the "healthcheck" marker.
    """
    config_line = (
        "healthcheck: mark this test as a healthcheck. "
        "See also: http://pytest-ordering.readthedocs.org/"
    )
    config.addinivalue_line("markers", config_line)


def pytest_addoption(parser):
    parser.addoption(
        "--healthcheck",
        action="store_true",
        help="run healthchecks.")


def pytest_runtest_setup(item):
    import pytest  # Import here because python-hospital does not
                   # require py.test to be installed.
    if item.config.getoption("--healthcheck"):
        if "healthcheck" not in item.keywords:
            raise pytest.skip("not a health check")


def pytest_collection_modifyitems(session, config, items):
    for item in items:
        if is_healthcheck(item.function):
            item.add_marker('healthcheck')
