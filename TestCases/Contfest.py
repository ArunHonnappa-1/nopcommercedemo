from selenium import webdriver
import pytest


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    else:
        driver = webdriver.Ie()
    return driver

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


############HTML file######################

def pytest_configure(config):
    # config._metadata['Project Name'] = 'Nopcommerce'
    # config._metadata['Module Name'] = 'Customers'
    # config._metadata['Tester'] = 'Arun Honnappa'
    config._metadata['Project Name'] = 'Application'
    config._metadata['Module Name'] = 'Login'
    config._metadata['Tester'] = 'V'
    config._metadata['Package'] = 'python'


@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.Pop("Plugins", None)