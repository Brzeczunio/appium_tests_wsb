import pytest
from appium import webdriver as appiumdriver
from os import environ


def get_sauce_url(data_center):
    username = environ['SAUCE_USERNAME']
    access_key = environ['SAUCE_ACCESS_KEY']

    if data_center and data_center.lower() == 'eu':
        return 'https://' + username + ':' + access_key + '@ondemand.eu-central-1.saucelabs.com:443/wd/hub'
    else:
        return 'https://' + username + ':' + access_key + '@ondemand.us-west-1.saucelabs.com:443/wd/hub'


def pytest_addoption(parser):
    parser.addoption('--dc', action='store', default='eu', help='Set Sauce Labs Data Center (US or EU)')


def sauce_log_result(request, driver):
    sauce_result = 'failed' if request.node.rep_call.failed else 'passed'
    driver.execute_script('sauce:job-result={}'.format(sauce_result))


@pytest.fixture
def data_center(request):
    return request.config.getoption('--dc')


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()

    # set a report attribute for each phase of a call, which can
    # be "setup", "call", "teardown"
    setattr(item, "rep_" + rep.when, rep)


@pytest.fixture
def ios_driver(request, data_center):
    desired_caps = {
        'platformName': 'iOS',
        'platformVersion': '15.0',
        'deviceName': 'iPhone_XR_free',
        'appiumVersion': '1.22.1',
        'app': 'storage:857601cb-1104-409a-8cf5-1f799e271975',
        'project': 'First python appium project',
        'build': 'Python iOS',
        'name': request.node.name,
    }

    sauce_url = get_sauce_url(data_center)
    driver = appiumdriver.Remote(sauce_url, desired_capabilities=desired_caps)
    yield driver
    sauce_log_result(request, driver)
    driver.quit()


@pytest.fixture
def android_driver(request, data_center):
    desired_caps = {
        'platformName': 'Android',
        'platformVersion': '12.0',
        'deviceName': 'Android GoogleAPI Emulator',
        'automationName': 'UiAutomator2',
        'appiumVersion': '1.22.1',
        'app': 'storage:c1352f4a-2095-4c2f-be93-0decd358433b',
        'project': 'First python appium project',
        'build': 'Python Android',
        'name': request.node.name,
    }

    sauce_url = get_sauce_url(data_center)
    driver = appiumdriver.Remote(sauce_url, desired_capabilities=desired_caps)
    yield driver
    sauce_log_result(request, driver)
    driver.quit()