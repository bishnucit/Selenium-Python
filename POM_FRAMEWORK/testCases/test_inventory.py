import time

import pytest

from pageObjects.InventoryPage import InventoryPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import CustomLogger
from pageObjects.LoginPage import LoginPage
from utilities import ExcelUtils

@pytest.mark.smoke
class Test_003_Inventory:
    baseURL = ReadConfig.getURL()
    username = ReadConfig.getUname()
    password = ReadConfig.getPass()
    path = ".//TestData/InventoryData.xlsx"

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
            self.logger.info("****** Success - Count of items matches expected result ******")
            assert True
        else:
            self.logger.error("****** Failed - taking screenshot******")
            time.sleep(3)
            self.driver.save_screenshot(".\\Screenshots\\" + "test_add_to_cart.png")
            assert False

        self.logger.info("****** Logging out ******")
        self.login.clickLogout()
        time.sleep(2)
        self.driver.close()

    @pytest.mark.sanity
    def test_inventory_contents(self, setup):

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

        self.logger.info("****** Fetching list data ******")
        content_one = self.inventory.first_item_contents()
        content_one_new = [s.replace("$", "") for s in content_one]
        content_two = self.inventory.second_item_contents()
        content_two_new = [s.replace("$", "") for s in content_two]
        content_three = self.inventory.third_item_contents()
        content_three_new = [s.replace("$", "") for s in content_three]
        content_four = self.inventory.fourth_item_contents()
        content_four_new = [s.replace("$", "") for s in content_four]
        content_five = self.inventory.fifth_item_contents()
        content_five_new = [s.replace("$", "") for s in content_five]
        content_six = self.inventory.sixth_item_contents()
        content_six_new = [s.replace("$", "") for s in content_six]
        self.logger.info("****** Fetching from website completed ******")

        # get data from Excel
        self.rows = ExcelUtils.getRowCount(self.path, 'NameAtoZ')

        self.logger.info("****** Fetching data from Excel file ******")
        big_list = []
        for r in range(2, self.rows + 1):
            content_from_excel = []
            self.item_name = ExcelUtils.readData(self.path, 'NameAtoZ', r, 1)
            content_from_excel.append(self.item_name)
            self.item_desc = ExcelUtils.readData(self.path, 'NameAtoZ', r, 2)
            content_from_excel.append(self.item_desc)
            self.item_price = ExcelUtils.readData(self.path, 'NameAtoZ', r, 3)
            content_from_excel.append(self.item_price)
            self.item_link = ExcelUtils.readData(self.path, 'NameAtoZ', r, 4)
            content_from_excel.append(self.item_link)
            big_list.append(content_from_excel)
        self.logger.info("****** Fetching from excel completed ******")

        self.logger.info("****** Cleaning list to convert all to string ******")
        big_list_one = [str(s) for s in big_list[0]]
        big_list_two = [str(s) for s in big_list[1]]
        big_list_three = [str(s) for s in big_list[2]]
        big_list_four = [str(s) for s in big_list[3]]
        big_list_five = [str(s) for s in big_list[4]]
        big_list_six = [str(s) for s in big_list[5]]

        if big_list_one == content_one_new:
            assert True
            self.logger.info("******First Data fetched from website matched with Excel ******")
        else:
            assert False
            self.logger.error("******First Data fetched from website mismatched with Excel ******")

        if big_list_two == content_two_new:
            assert True
            self.logger.info("******Second Data fetched from website matched with Excel ******")
        else:
            assert False
            self.logger.error("******Second Data fetched from website mismatched with Excel ******")

        if big_list_three == content_three_new:
            assert True
            self.logger.info("******Third Data fetched from website matched with Excel ******")
        else:
            assert False
            self.logger.error("******Third Data fetched from website mismatched with Excel ******")

        if big_list_four == content_four_new:
            assert True
            self.logger.info("******Fourth Data fetched from website matched with Excel ******")
        else:
            assert False
            self.logger.error("******Fourth Data fetched from website mismatched with Excel ******")

        if big_list_five == content_five_new:
            assert True
            self.logger.info("******Fifth Data fetched from website matched with Excel ******")
        else:
            assert False
            self.logger.error("******Fifth Data fetched from website mismatched with Excel ******")

        if big_list_six == content_six_new:
            assert True
            self.logger.info("******Sixth Data fetched from website matched with Excel ******")
        else:
            assert False
            self.logger.error("******Sixth Data fetched from website mismatched with Excel ******")

        self.driver.close()
