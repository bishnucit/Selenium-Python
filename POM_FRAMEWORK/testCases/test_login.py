import pytest

from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import CustomLogger


class Test_001_Login:
    baseURL = ReadConfig.getURL()
    username = ReadConfig.getUname()
    password = ReadConfig.getPass()

    logger = CustomLogger.customerlogger()

    @pytest.mark.smoke
    @pytest.mark.sanity
    def test_welcome_page(self, setup):

        self.logger.info("****** Test_001_Login ******")
        self.logger.info("****** Importing setup ******")
        self.driver = setup
        self.driver.get(self.baseURL)
        title = self.driver.title
        self.logger.info("****** Verifying title ******")
        if title == "Swag Labs":
            self.logger.info("****** Success ******")
            self.driver.close()
            assert True
        else:
            self.logger.error("****** Failed ******")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_loginTitle.png")
            self.driver.close()
            assert False

    @pytest.mark.smoke
    @pytest.mark.sanity
    def test_login(self, setup):

        self.logger.info("****** Test_001_Login ******")
        self.logger.info("****** Importing setup ******")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.login = LoginPage(self.driver)
        self.login.setUserName(self.username)
        self.login.setPassWord(self.password)
        self.login.clickLogin()
        self.logger.info("****** Performing login ******")
        title = self.driver.title
        self.logger.info("****** Verifying title ******")
        if title == "Swag Labs":
            self.logger.info("****** Success ******")
            self.driver.close()
            assert True
        else:
            self.logger.error("****** Failed ******")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.driver.close()
            assert False
