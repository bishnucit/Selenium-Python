import time

import pytest

from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import CustomLogger
from utilities import ExcelUtils


class TestLogin002:
    baseURL = ReadConfig.getURL()
    path = ".//TestData/LoginData.xlsx"

    logger = CustomLogger.customerlogger()

    @pytest.mark.ddt
    @pytest.mark.smoke
    def test_login_ddt(self, setup):

        self.logger.info("****** TestLogin002 Started ******")
        self.logger.info("****** Importing setup ******")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.login = LoginPage(self.driver)

        # get data from Excel
        self.rows = ExcelUtils.getRowCount(self.path, 'Data')

        status = []
        for r in range(2, self.rows+1):
            self.username = ExcelUtils.readData(self.path, 'Data', r, 1)
            self.password = ExcelUtils.readData(self.path, 'Data', r, 2)
            self.expected = ExcelUtils.readData(self.path, 'Data', r, 3)

            self.login.setUserName(self.username)
            self.login.setPassWord(self.password)
            self.login.clickLogin()
            time.sleep(5)
            self.logger.info("****** Performing login ******")
            title = self.driver.title
            self.logger.info("****** Verifying title ******")
            if self.login.successLogin:
                if self.expected == "Pass":
                    self.logger.info("****** Success ******")
                    self.login.clickLogout()
                    status.append("Pass")

                    '''
                elif self.expected == "Fail":
                    self.logger.info("****** Failed inside pass ******")
                    self.login.clickLogout()
                    status.append("Fail")
                    '''
            else:
                if self.expected == "Fail":
                    self.logger.info("****** Passed ******")
                    status.append("Pass")

                elif self.expected == "Pass":
                    self.logger.info("****** Failed inside fail ******")
                    status.append("Fail")

        if "Fail" not in status:
            self.logger.info("****** Login DDT Passed ******")
            self.driver.close()
            assert True
        else:
            self.logger.info("****** Login DDT Failed ******")
            self.driver.close()
            assert False
        self.logger.info("****** TestLogin002 Completed ******")
        
