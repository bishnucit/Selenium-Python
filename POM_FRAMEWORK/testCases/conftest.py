import pytest
from selenium import webdriver


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
        return driver
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        return driver
    else:
        driver = webdriver.Chrome()
        return driver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


def pytest_configure(config):
    config._metadata['Project Name'] = 'PYTEST FRAMEWORK'
    config._metadata['Website Name'] = 'AUTOMATE THIS'
    config._metadata['Quality Checker'] = 'BISHNU'


@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
