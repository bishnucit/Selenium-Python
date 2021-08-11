class InventoryPage:

    option_selectAtoZ_xpath = "//*[@id='header_container']/div[2]/div[2]/span/select/option[1]"
    option_selectZtoA_xpath = "//*[@id='header_container']/div[2]/div[2]/span/select/option[2]"
    option_selectHtoL_xpath = "//*[@id='header_container']/div[2]/div[2]/span/select/option[3]"
    option_selectLtoH_xpath = "//*[@id='header_container']/div[2]/div[2]/span/select/option[4]"

    add_to_cart_first_item_xpath = "/html/body/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[2]/button"

    cart_icon_xpath = "//*[@id='shopping_cart_container']/a/span"

    def __init__(self, driver):
        self.driver = driver

    def selectAtoZ(self):
        self.driver.find_element_by_xpath(self.option_selectAtoZ_xpath).click()

    def selectZtoA(self):
        self.driver.find_element_by_xpath(self.option_selectZtoA_xpath).click()

    def selectLtoH(self):
        self.driver.find_element_by_xpath(self.option_selectHtoL_xpath).click()

    def selectHtoL(self):
        self.driver.find_element_by_xpath(self.option_selectLtoH_xpath).click()

    def add_to_cart_first_item(self):
        self.driver.find_element_by_xpath(self.add_to_cart_first_item_xpath).click()

    def cart_value(self):
        value = self.driver.find_element_by_xpath(self.cart_icon_xpath).text
        return int(value)
