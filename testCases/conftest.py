import pytest
from selenium import webdriver

@pytest.fixture
def setup(browser):
    if browser in ('chrome', 'Chrome'):
        driver = webdriver.Chrome()
    elif browser in ('firefox', 'Firefox'):
        driver = webdriver.Firefox()
    else :
        driver = webdriver.Firefox()

    driver.maximize_window()
    return driver

def pytest_addoption(parser): # will get value from CLI/hooks
    parser.addoption("--browser")

@pytest.fixture
def browser(request): # will return Browser value to setup method
    return request.config.getoption("--browser")

########## PyTest HTML Report ##########

# Hooks for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Abcdef'

# Hooks for Delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
