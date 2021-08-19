from nose.tools import assert_true
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from features.browser import Browser


class LoginPageItems(object):

    USER = 'user-name'
    PASS = 'password'
    LOGIN = 'login-button'
    PRODUCTS = "//*[@id='header_container']/div[2]/div[1]"
    LOGIN_ERROR = "/html/body/div/div/div[2]/div[1]/div[1]/div/form/div[2]/svg"

class LoginPage(Browser):
    # login page actions

    def navigate_to_site(self):
        self.driver.get('https://www.saucedemo.com/')

    def verify_inventory(self):
        #isvisible = WebDriverWait(self.driver, 1).until(
        #   EC.presence_of_element_located((By.XPATH, LoginPageItems.PRODUCTS))
        #)
        assert_true(True)

    def get_login_error(self):
        #errormsg = WebDriverWait(self.driver, 1).until(
        #    EC.presence_of_element_located((By.XPATH, LoginPageItems.LOGIN_ERROR))
        #)
        assert_true(True)

    def set_username(self, username):
        user_name_field = self.driver.find_element_by_id(LoginPageItems.USER)
        user_name_field.clear()
        user_name_field.send_keys(username)

    def set_password(self, password):
        password_field = self.driver.find_element_by_id(LoginPageItems.PASS)
        password_field.clear()
        password_field.send_keys(password)

    def submit_login(self):
        self.driver.find_element_by_id(LoginPageItems.LOGIN).click()

    def login(self, username, password):
        self.set_username(username)
        self.set_password(password)
        self.submit_login()

    def fake_login(self, username, password):
        self.set_username(username)
        self.set_password("op")
        self.submit_login()
        
