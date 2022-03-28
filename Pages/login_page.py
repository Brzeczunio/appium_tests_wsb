from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as Wait


def open_login_page(driver):
    driver.get('mydemoapprn://login')


def login(driver, user_login, password):
    Wait(driver, 30).until(
        EC.visibility_of_element_located((MobileBy.ACCESSIBILITY_ID, 'Username input field'))).send_keys(user_login)
    Wait(driver, 30).until(
        EC.visibility_of_element_located((MobileBy.ACCESSIBILITY_ID, 'Password input field'))).send_keys(password)
    Wait(driver, 30).until(
        EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, 'Login button'))).click()
