from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from features.browser import Browser


class LoginPageElements(object):

    BODY = '#yDmH0d'
    USER = 'identifierId'
    USER_SUBMIT = '#identifierNext > content > span'
    PASS = '#password > div.aCsJod.oJeWuf > div > div.Xb9hP > input'
    SUBMIT = '#passwordNext > content > span'
    LOGIN_ERROR = '#password > div.LXRPh > div.dEOOab.RxsGPe'


class LoginPage(Browser):
    # login page actions

    def navigate_to_site(self):
        self.driver.get('https://www.saucedemo.com/')

    def get_page_title(self):
        return self.driver.title

   
