import time

import pytest

from pageObjects.InventoryPage import InventoryPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import CustomLogger
from pageObjects.LoginPage import LoginPage


@pytest.mark.smoke
@pytest.mark.sanity
class Test_003_Inventory:
    baseURL = ReadConfig.getURL()
    username = ReadConfig.getUname()
    password = ReadConfig.getPass()

    logger = CustomLogger.customerlogger()

    def test_add_to_cart(self, setup):

        self.logger.info("****** Test_003_Inventory ******")
        self.logger.info("****** Importing setup ******")
        self.driver = setup
        self.driver.get(self.baseURL)

        self.login = LoginPage(self.driver)
        self.login.setUserName(self.username)
        self.login.setPassWord(self.password)
        self.login.clickLogin()
        self.logger.info("****** Login Successful ******")
        time.sleep(2)

        self.logger.info("****** Selecting option Name A to Z ******")
        self.inventory = InventoryPage(self.driver)
        self.inventory.selectAtoZ()
        self.logger.info("****** Adding to cart the first item of the list ******")
        self.inventory.add_to_cart_first_item()
        time.sleep(2)

        self.logger.info("****** Selecting option Name Z to A ******")
        self.inventory = InventoryPage(self.driver)
        self.inventory.selectZtoA()
        self.logger.info("****** Adding to cart the first item of the list ******")
        self.inventory.add_to_cart_first_item()
        time.sleep(2)

        self.logger.info("****** Selecting option Price L to H ******")
        self.inventory = InventoryPage(self.driver)
        self.inventory.selectLtoH()
        self.logger.info("****** Adding to cart the first item of the list ******")
        self.inventory.add_to_cart_first_item()
        time.sleep(2)

        self.logger.info("****** Selecting option Price H to L ******")
        self.inventory = InventoryPage(self.driver)
        self.inventory.selectHtoL()
        self.logger.info("****** Adding to cart the first item of the list ******")
        self.inventory.add_to_cart_first_item()
        time.sleep(2)

        cart_value = self.inventory.cart_value()
        if cart_value == 4:
            self.logger.info("****** Success ******")
            assert True
        else:
            self.logger.error("****** Failed - taking screenshot******")
            time.sleep(3)
            self.driver.save_screenshot(".\\Screenshots\\" + "test_add_to_cart.png")
            assert False

        self.logger.error("****** Logging out ******")
        self.login.clickLogout()
        time.sleep(2)
        self.driver.close()
