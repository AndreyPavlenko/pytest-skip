import pytest

pytest_plugins = ["pytester"]


@pytest.fixture
def is_xdist_installed(pytestconfig: pytest.Config):
    return pytestconfig.pluginmanager.hasplugin("xdist")
