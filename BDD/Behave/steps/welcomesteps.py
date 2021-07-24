import time

from behave import *
from selenium import webdriver


@given('launch chrome browser')
def launch_browser(context):
    # use -> initializes the chrome browser
    context.driver = webdriver.Chrome()


@when('open test site')
def open_page(context):
    # use -> opens the site under test
    context.driver.get("https://www.saucedemo.com/")


@then('close browser')
def close_browser(context):
    # use -> closes the browser
    context.driver.close()


@then('verify that the webpage has some content')
def verify_content(context):
    # use -> verify image is visible, if visible assert test is passed
    status = context.driver.find_element_by_xpath("//*[@id='root']/div/div[2]/div[1]/div[2]").is_displayed()
    assert status is True


@given(u'open test site')
def open_page(context):
    # use -> opens the site under test in chrome, change here to perform on other browsers
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.saucedemo.com/")


@when(u'I enter valid username and password')
def enter_u_and_p(context):
    # use -> enter username password and click on login button
    username = context.driver.find_element_by_id("user-name")
    username.send_keys("standard_user")

    username = context.driver.find_element_by_id("password")
    username.send_keys("secret_sauce")

    login = context.driver.find_element_by_id("login-button")
    login.click()


@then(u'I am successfully logged in')
def verify_inventory_page(context):
    # use -> verification of inventory page if the top logo is displayed
    time.sleep(1)
    status = context.driver.find_element_by_xpath("//*[@id='header_container']/div[1]/div[2]/div").is_displayed()
    assert status is True


@when(u'I enter invalid username and password')
def enter_invalid_u_and_p(context):
    # use -> enters invalid credentials and clicks on login button
    username = context.driver.find_element_by_id("user-name")
    username.send_keys("standard_user1")

    username = context.driver.find_element_by_id("password")
    username.send_keys("secret_sauce1")

    login = context.driver.find_element_by_id("login-button")
    login.click()


@then(u'I can see the error message')
def verify_error(context):
    # use -> verifies if the error message after fail login is displayed or not
    time.sleep(1)
    status = context.driver.find_element_by_xpath("//*[@id='login_button_container']/div/form/div[3]/h3").is_displayed()
    assert status is True


@then(u'I logout and close browser')
def logout_and_quit(context):
    # use -> logs out the session and closes the browser after successful logout
    time.sleep(1)
    context.driver.find_element_by_xpath("//*[@id='react-burger-menu-btn']").click()
    time.sleep(1)
    context.driver.find_element_by_xpath("//*[@id='logout_sidebar_link']").click()
    time.sleep(1)
    status = context.driver.find_element_by_xpath("//*[@id='root']/div/div[2]/div[1]/div[2]").is_displayed()
    assert status is True
    context.driver.close()


@then(u'I click on the dropdown to select "{display}" option to see "{item}" first')
def select_option_to_display(context, display, item):
    # use -> clicks on dropdown and changes display option then clicks on the first product and verifies
    # if product is displayed or not.
    if display == "az":
        context.driver.find_element_by_xpath("//*[@id='header_container']/div[2]/div[2]/span/select/option[1]").click()
        time.sleep(1)
        context.driver.find_element_by_id(item).click()
        time.sleep(1)
        product1 = context.driver.find_element_by_xpath("//*[@id='inventory_item_container']/div/div/div[1]/img").\
            is_displayed()
        assert product1 is True
    elif display == "za":
        context.driver.find_element_by_xpath("//*[@id='header_container']/div[2]/div[2]/span/select/option[2]").click()
        time.sleep(1)
        context.driver.find_element_by_id(item).click()
        time.sleep(1)
        product2 = context.driver.find_element_by_xpath("//*[@id='inventory_item_container']/div/div/div[1]/img"). \
            is_displayed()
        assert product2 is True
    elif display == "lohi":
        context.driver.find_element_by_xpath("//*[@id='header_container']/div[2]/div[2]/span/select/option[3]").click()
        time.sleep(1)
        context.driver.find_element_by_id(item).click()
        time.sleep(1)
        product3 = context.driver.find_element_by_xpath("//*[@id='inventory_item_container']/div/div/div[1]/img"). \
            is_displayed()
        assert product3 is True
    elif display == "hilo":
        context.driver.find_element_by_xpath("//*[@id='header_container']/div[2]/div[2]/span/select/option[4]").click()
        time.sleep(1)
        context.driver.find_element_by_id(item).click()
        time.sleep(1)
        product4 = context.driver.find_element_by_xpath("//*[@id='inventory_item_container']/div/div/div[1]/img"). \
            is_displayed()
        assert product4 is True
    else:
        pass


@then(u'I click on the first product and can see the product detail page')
def product_detail_page(context):
    # use -> clicks on the first product of the page and visits the product detail page
    # we use here full xpath to get the first element of the list instead of xpath
    # we are using sleep to visually see the test case run else it wont be visible properly
    time.sleep(3)
    first_product = context.driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div/div/div/div[1]/div[1]/a/img')
    first_product.click()
    time.sleep(2)


@then(u'I navigate back to inventory page from product detail page')
def navigate_back(context):
    # use -> navigates back from product detail page to inventory page
    back_button = context.driver.find_element_by_xpath("//*[@id='back-to-products']")
    back_button.click()
    time.sleep(2)


@then(u'I change option of display to low to high')
def display_lo_to_hi(context):
    # use -> select low to high option for product display in inventory page
    lohi_option = context.driver.\
        find_element_by_xpath("//*[@id='header_container']/div[2]/div[2]/span/select/option[3]")
    lohi_option.click()
    time.sleep(2)


@then(u'I change option of display to high to low')
def display_hi_to_lo(context):
    # use -> select high to low option for product display in inventory page
    hilo_option = context.driver.\
        find_element_by_xpath("//*[@id='header_container']/div[2]/div[2]/span/select/option[4]")
    hilo_option.click()
    time.sleep(2)


@then(u'I add the product to cart')
def add_product_to_cart(context):
    # use -> adds the product to cart on the cart page
    # using full xpath to make the code generic
    add_to_cart = context.driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div/div/div[2]/button")
    add_to_cart.click()
    time.sleep(2)


@then(u'I click on the cart button')
def click_cart_button(context):
    # use -> navigates to cart page from inventory page
    add_to_cart = context.driver.find_element_by_xpath("//*[@id='shopping_cart_container']/a")
    add_to_cart.click()
    time.sleep(2)


@then(u'I verify "{value}" items are displaying in cart')
def verify_number_of_items_in_cart(context, value):
    # use -> verifies the number of items in cart with the passed value from the feature file
    cart_list = context.driver.find_element_by_css_selector("div.cart_list")
    total_items = cart_list.find_elements_by_css_selector("div.cart_item")
    items = len(total_items)
    if items == int(value):
        assert True
    else:
        assert False


@then(u'I go back to inventory page from cart page')
def step_impl(context):
    # use -> navigates to inventory page from cart page
    back_to_inventory = context.driver.find_element_by_xpath("//*[@id='continue-shopping']")
    back_to_inventory.click()
    time.sleep(2)


# --no-capture  use no capture to see print statements
