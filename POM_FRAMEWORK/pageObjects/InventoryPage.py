class InventoryPage:

    option_selectAtoZ_xpath = "//*[@id='header_container']/div[2]/div[2]/span/select/option[1]"
    option_selectZtoA_xpath = "//*[@id='header_container']/div[2]/div[2]/span/select/option[2]"
    option_selectHtoL_xpath = "//*[@id='header_container']/div[2]/div[2]/span/select/option[3]"
    option_selectLtoH_xpath = "//*[@id='header_container']/div[2]/div[2]/span/select/option[4]"

    inventory_item_xpath_1_title = "/html/body/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[1]/a/div"
    inventory_item_xpath_2_title = "/html/body/div/div/div/div[2]/div/div/div/div[2]/div[2]/div[1]/a/div"
    inventory_item_xpath_3_title = "/html/body/div/div/div/div[2]/div/div/div/div[3]/div[2]/div[1]/a/div"
    inventory_item_xpath_4_title = "/html/body/div/div/div/div[2]/div/div/div/div[4]/div[2]/div[1]/a/div"
    inventory_item_xpath_5_title = "/html/body/div/div/div/div[2]/div/div/div/div[5]/div[2]/div[1]/a/div"
    inventory_item_xpath_6_title = "/html/body/div/div/div/div[2]/div/div/div/div[6]/div[2]/div[1]/a/div"

    inventory_item_xpath_1_desc = "/html/body/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[1]/div"
    inventory_item_xpath_2_desc = "/html/body/div/div/div/div[2]/div/div/div/div[2]/div[2]/div[1]/div"
    inventory_item_xpath_3_desc = "/html/body/div/div/div/div[2]/div/div/div/div[3]/div[2]/div[1]/div"
    inventory_item_xpath_4_desc = "/html/body/div/div/div/div[2]/div/div/div/div[4]/div[2]/div[1]/div"
    inventory_item_xpath_5_desc = "/html/body/div/div/div/div[2]/div/div/div/div[5]/div[2]/div[1]/div"
    inventory_item_xpath_6_desc = "/html/body/div/div/div/div[2]/div/div/div/div[6]/div[2]/div[1]/div"

    inventory_item_xpath_1_price = "/html/body/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[2]/div"
    inventory_item_xpath_2_price = "/html/body/div/div/div/div[2]/div/div/div/div[2]/div[2]/div[2]/div"
    inventory_item_xpath_3_price = "/html/body/div/div/div/div[2]/div/div/div/div[3]/div[2]/div[2]/div"
    inventory_item_xpath_4_price = "/html/body/div/div/div/div[2]/div/div/div/div[4]/div[2]/div[2]/div"
    inventory_item_xpath_5_price = "/html/body/div/div/div/div[2]/div/div/div/div[5]/div[2]/div[2]/div"
    inventory_item_xpath_6_price = "/html/body/div/div/div/div[2]/div/div/div/div[6]/div[2]/div[2]/div"

    inventory_item_xpath_1_image_link = "/html/body/div/div/div/div[2]/div/div/div/div[1]/div[1]/a/img"
    inventory_item_xpath_2_image_link = "/html/body/div/div/div/div[2]/div/div/div/div[2]/div[1]/a/img"
    inventory_item_xpath_3_image_link = "/html/body/div/div/div/div[2]/div/div/div/div[3]/div[1]/a/img"
    inventory_item_xpath_4_image_link = "/html/body/div/div/div/div[2]/div/div/div/div[4]/div[1]/a/img"
    inventory_item_xpath_5_image_link = "/html/body/div/div/div/div[2]/div/div/div/div[5]/div[1]/a/img"
    inventory_item_xpath_6_image_link = "/html/body/div/div/div/div[2]/div/div/div/div[6]/div[1]/a/img"

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

    def first_item_contents(self):
        item_one = []
        title = self.driver.find_element_by_xpath(self.inventory_item_xpath_1_title).text
        item_one.append(title)
        desc = self.driver.find_element_by_xpath(self.inventory_item_xpath_1_desc).text
        item_one.append(desc)
        price = self.driver.find_element_by_xpath(self.inventory_item_xpath_1_price).text
        item_one.append(price)
        src = self.driver.find_element_by_xpath(self.inventory_item_xpath_1_image_link).get_attribute("src")
        item_one.append(src)
        return item_one

    def second_item_contents(self):
        item_two = []
        title = self.driver.find_element_by_xpath(self.inventory_item_xpath_2_title).text
        item_two.append(title)
        desc = self.driver.find_element_by_xpath(self.inventory_item_xpath_2_desc).text
        item_two.append(desc)
        price = self.driver.find_element_by_xpath(self.inventory_item_xpath_2_price).text
        item_two.append(price)
        src = self.driver.find_element_by_xpath(self.inventory_item_xpath_2_image_link).get_attribute("src")
        item_two.append(src)
        return item_two

    def third_item_contents(self):
        item_three = []
        title = self.driver.find_element_by_xpath(self.inventory_item_xpath_3_title).text
        item_three.append(title)
        desc = self.driver.find_element_by_xpath(self.inventory_item_xpath_3_desc).text
        item_three.append(desc)
        price = self.driver.find_element_by_xpath(self.inventory_item_xpath_3_price).text
        item_three.append(price)
        src = self.driver.find_element_by_xpath(self.inventory_item_xpath_3_image_link).get_attribute("src")
        item_three.append(src)
        return item_three

    def fourth_item_contents(self):
        item_four = []
        title = self.driver.find_element_by_xpath(self.inventory_item_xpath_4_title).text
        item_four.append(title)
        desc = self.driver.find_element_by_xpath(self.inventory_item_xpath_4_desc).text
        item_four.append(desc)
        price = self.driver.find_element_by_xpath(self.inventory_item_xpath_4_price).text
        item_four.append(price)
        src = self.driver.find_element_by_xpath(self.inventory_item_xpath_4_image_link).get_attribute("src")
        item_four.append(src)
        return item_four

    def fifth_item_contents(self):
        item_fifth = []
        title = self.driver.find_element_by_xpath(self.inventory_item_xpath_5_title).text
        item_fifth.append(title)
        desc = self.driver.find_element_by_xpath(self.inventory_item_xpath_5_desc).text
        item_fifth.append(desc)
        price = self.driver.find_element_by_xpath(self.inventory_item_xpath_5_price).text
        item_fifth.append(price)
        src = self.driver.find_element_by_xpath(self.inventory_item_xpath_5_image_link).get_attribute("src")
        item_fifth.append(src)
        return item_fifth

    def sixth_item_contents(self):
        item_sixth = []
        title = self.driver.find_element_by_xpath(self.inventory_item_xpath_6_title).text
        item_sixth.append(title)
        desc = self.driver.find_element_by_xpath(self.inventory_item_xpath_6_desc).text
        item_sixth.append(desc)
        price = self.driver.find_element_by_xpath(self.inventory_item_xpath_6_price).text
        item_sixth.append(price)
        src = self.driver.find_element_by_xpath(self.inventory_item_xpath_6_image_link).get_attribute("src")
        item_sixth.append(src)
        return item_sixth
