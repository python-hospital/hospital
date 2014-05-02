from hospital.core import is_healthcheck


def pytest_configure(config):
    register_healthcheck_marker(config)
    setup_healthcheck_flag(config)


def pytest_collection_modifyitems(session, config, items):
    for item in items:
        if is_healthcheck(item.cls) or is_healthcheck(item.function):
            item.add_marker("healthcheck")


def pytest_addoption(parser):
    parser.addoption(
        "--healthcheck",
        action="store_true",
        help="run healthchecks.")


def register_healthcheck_marker(config):
    """Register the "healthcheck" marker.
    """
    config_line = (
        "healthcheck: mark this test as a healthcheck. "
        "See also: http://pytest-ordering.readthedocs.org/"
    )
    config.addinivalue_line("markers", config_line)


def setup_healthcheck_flag(config):
    """Implements the `--healthcheck` flag.
    `--healthcheck` flag is equivalent to `-m healthcheck`.
    """
    if config.getoption("healthcheck"):
        # TODO: I didn't see a public API for this, but maybe I
        # missed something.
        setattr(config.option, "markexpr", "healthcheck")
