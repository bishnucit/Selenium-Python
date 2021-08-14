import time

import pytest

from pageObjects.CheckoutPage import CheckoutPage
from pageObjects.InventoryPage import InventoryPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import CustomLogger
from pageObjects.LoginPage import LoginPage


class TestCheckout004:
    baseURL = ReadConfig.getURL()
    username = ReadConfig.getUname()
    password = ReadConfig.getPass()
    firstname = ReadConfig.getFirstName()
    lastname = ReadConfig.getLastName()
    postal = ReadConfig.getPostal()

    logger = CustomLogger.customerlogger()

    @pytest.mark.sanity
    def test_checkout_success(self, setup):

        self.logger.info("****** TestCheckout004_checkout_success Started ******")
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

        self.logger.info("****** Navigating to cart page ******")
        self.inventory.navigate_to_checkout()
        time.sleep(2)

        self.logger.info("****** Verifying Cart page ******")
        self.checkout_page = CheckoutPage(self.driver)
        self.logger.info("****** Verifying Cart page ******")
        if self.checkout_page.verify_cart_page():
            self.logger.info("****** Cart page is successfully opened ******")
            assert True
        else:
            self.logger.error("****** Cart page is not reachable ******")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_checkout_success.png")
            assert False

        self.logger.info("****** Navigating to Checkout page ******")
        self.checkout_page.checkout_items()
        time.sleep(2)

        self.logger.info("****** Verifying Information page ******")
        if self.checkout_page.verify_information_page():
            self.logger.info("****** Information page is successfully opened ******")
            assert True
        else:
            self.logger.error("****** Information page is not reachable ******")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_checkout_success.png")
            assert False

        self.logger.info("****** Entering customer information ******")
        self.checkout_page.set_firstname(self.firstname)
        time.sleep(1)
        self.checkout_page.set_lastname(self.lastname)
        time.sleep(1)
        self.checkout_page.set_postal(self.postal)
        time.sleep(1)

        self.logger.info("****** Continuing Checkout ******")
        self.checkout_page.continue_checkout()
        time.sleep(2)

        self.logger.info("****** Verifying Overview page ******")
        if self.checkout_page.verify_overview_page():
            self.logger.info("****** Overview page is successfully opened ******")
            assert True
        else:
            self.logger.error("****** Overview page is not reachable ******")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_checkout_success.png")
            assert False

        self.logger.info("****** Verifying Checkout details in overview page ******")
        if self.checkout_page.verify_checkout_details():
            self.logger.info("****** Checkout total is fine ******")
            assert True
        else:
            self.logger.error("****** Checkout total mismatch ******")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_checkout_success.png")
            assert False

        self.logger.info("****** Confirming purchase ******")
        self.checkout_page.confirm_checkout()
        time.sleep(2)

        self.logger.info("****** Verifying Thank you page ******")
        if self.checkout_page.verify_thankyou_page():
            self.logger.info("****** Checkout is completed ******")
            assert True
        else:
            self.logger.error("****** Checkout was unsuccessful ******")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_checkout_success.png")
            assert False

        self.logger.info("****** Logging out ******")
        self.login.clickLogout()
        time.sleep(2)
        self.logger.info("****** TestCheckout004_checkout_success Completed ******")
        self.driver.close()
