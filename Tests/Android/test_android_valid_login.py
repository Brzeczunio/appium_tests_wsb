from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Pages import login_page


def test_correct_login(android_driver):
    login_page.open_login_page(android_driver)
    login_page.login(android_driver, 'bob@example.com', '10203040')
    assert Wait(android_driver, 30).until(
        EC.visibility_of_element_located((MobileBy.XPATH, "//android.view.ViewGroup[@content-desc=\"container header\"]/android.widget.TextView"))).is_displayed()

