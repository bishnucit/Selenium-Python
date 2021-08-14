class CheckoutPage:

    cart_text_xpath = "/html/body/div/div/div/div[1]/div[2]/span"

    checkout_button_xpath = "/html/body/div/div/div/div[2]/div/div[2]/button[2]"

    information_text_xpath = "/html/body/div/div/div/div[1]/div[2]/span"

    textbox_firstname_id = "first-name"
    textbox_lastname_id = "last-name"
    textbox_postal_id = "postal-code"

    continue_button_xpath = "/html/body/div/div/div/div[2]/div/form/div[2]/input"

    overview_page_xpath = "/html/body/div/div/div/div[1]/div[2]/span"

    checkout_total_xpath = "/html/body/div/div/div/div[2]/div/div[2]/div[7]"

    confirm_checkout_xpath = "/html/body/div/div/div/div[2]/div/div[2]/div[8]/button[2]"

    thankyou_page_xpath = "/html/body/div/div/div/div[2]/img"

    def __init__(self, driver):

        self.driver = driver

    def checkout_items(self):
        self.driver.find_element_by_xpath(self.checkout_button_xpath).click()

    def set_firstname(self, firstname):
        self.driver.find_element_by_id(self.textbox_firstname_id).clear()
        self.driver.find_element_by_id(self.textbox_firstname_id).send_keys(firstname)

    def set_lastname(self, lastname):
        self.driver.find_element_by_id(self.textbox_lastname_id).clear()
        self.driver.find_element_by_id(self.textbox_lastname_id).send_keys(lastname)

    def set_postal(self, postal):
        self.driver.find_element_by_id(self.textbox_postal_id).clear()
        self.driver.find_element_by_id(self.textbox_postal_id).send_keys(postal)

    def continue_checkout(self):
        self.driver.find_element_by_xpath(self.continue_button_xpath).click()

    def verify_cart_page(self):
        if self.driver.find_element_by_xpath(self.cart_text_xpath).is_displayed():
            return True
        else:
            return False

    def verify_information_page(self):
        if self.driver.find_element_by_xpath(self.information_text_xpath).is_displayed():
            return True
        else:
            return False

    def verify_overview_page(self):
        if self.driver.find_element_by_xpath(self.overview_page_xpath).is_displayed():
            return True
        else:
            return False

    def verify_checkout_details(self):
        total = self.driver.find_element_by_xpath(self.checkout_total_xpath).text
        if "112.28" in str(total):
            return True
        else:
            return False

    def confirm_checkout(self):
        self.driver.find_element_by_xpath(self.confirm_checkout_xpath).click()

    def verify_thankyou_page(self):
        if self.driver.find_element_by_xpath(self.thankyou_page_xpath).is_displayed():
            return True
        else:
            return False
