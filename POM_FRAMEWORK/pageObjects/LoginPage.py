import time


class LoginPage:
    textbox_username_id = "user-name"
    textbox_password_id = "password"
    button_login_xpath = "//*[@id='login-button']"
    menu_button_xpath = "//*[@id='react-burger-menu-btn']"
    menu_link_logout = "//*[@id='logout_sidebar_link']"

    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, username):
        self.driver.find_element_by_id(self.textbox_username_id).clear()
        self.driver.find_element_by_id(self.textbox_username_id).send_keys(username)

    def setPassWord(self, password):
        self.driver.find_element_by_id(self.textbox_password_id).clear()
        self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element_by_xpath(self.button_login_xpath).click()

    def clickLogout(self):
        self.driver.find_element_by_xpath(self.menu_button_xpath).click()
        time.sleep(2)
        self.driver.find_element_by_xpath(self.menu_link_logout).click()

    def successLogin(self):
        button = self.driver.find_element_by_xpath(self.menu_button_xpath)
        if button.is_displayed():
            return True
        else:

            return False

    """
        def random_generator():
            return ''.join(random.SystemRandom().choice(string.ascii_lowercase + string.digits) for _ in range(7))
            
        # returns 7 character words randomly.    
    
    
    """
