import pytest
from selenium import webdriver
from selenium.webdriver import chrome
from selenium.webdriver.chrome.service import Service as chrome_service
from selenium.webdriver.firefox.service import Service as firefox_service
from selenium.webdriver.edge.service import Service as edge_service


@pytest.fixture(scope='class', autouse=True)
def setup(browser, request):
    if browser.lower() == 'chrome':
        print('this is chrome')
        c_service = chrome_service('Drivers/chromedriver.exe')
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=c_service, options=options)
    elif browser.lower() == 'firefox':
        f_service = firefox_service('Drivers/geckodriver.exe')
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(service=f_service, options=options)
    elif browser.lower() == 'edge':
        e_service = edge_service('Drivers/msedgedriver.exe')
        options = webdriver.EdgeOptions()
        driver = webdriver.Edge(service=e_service, options=options)
    else:
        raise Exception('Invalid browser provided,Supported browsers are : Chrome,Firefox,Edge')
    driver.maximize_window()

    driver.get("http://automationpractice.com/")
    driver.implicitly_wait(10)
    request.cls.driver = driver
    yield
    # driver.quit()


def pytest_addoption(parser):
    parser.addoption("--browser", default='chrome')
    # parser.adoption("--env", default='qa')


@pytest.fixture(scope='session')
def browser(request):
    browser = request.config.getoption('--browser')
    return browser
