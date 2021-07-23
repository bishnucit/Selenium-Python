import time

from behave import *
from selenium import webdriver


@given('launch chrome browser')
def launch_browser(context):
    context.driver = webdriver.Chrome()


@when('open test site')
def open_page(context):
    context.driver.get("https://www.saucedemo.com/")


@then('verify that the webpage has some content')
def verify_content(context):
    status = context.driver.find_element_by_xpath("//*[@id='root']/div/div[2]/div[1]/div[2]").is_displayed()
    assert status is True


@given(u'open test site')
def open_page(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.saucedemo.com/")


@when(u'I enter valid username and password')
def enter_u_and_p(context):
    username = context.driver.find_element_by_id("user-name")
    username.send_keys("standard_user")

    username = context.driver.find_element_by_id("password")
    username.send_keys("secret_sauce")

    login = context.driver.find_element_by_id("login-button")
    login.click()


@then(u'I am successfully logged in')
def verify_inventory_page(context):
    time.sleep(1)
    status = context.driver.find_element_by_xpath("//*[@id='header_container']/div[1]/div[2]/div").is_displayed()
    assert status is True


@when(u'I enter invalid username and password')
def enter_invalid_u_and_p(context):
    username = context.driver.find_element_by_id("user-name")
    username.send_keys("standard_user1")

    username = context.driver.find_element_by_id("password")
    username.send_keys("secret_sauce1")

    login = context.driver.find_element_by_id("login-button")
    login.click()


@then(u'I can see the error message')
def verify_error(context):
    time.sleep(1)
    status = context.driver.find_element_by_xpath("//*[@id='login_button_container']/div/form/div[3]/h3").is_displayed()
    assert status is True


@then(u'I logout and close browser')
def logout_and_quit(context):
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


@then(u'It should display the "{item}" first on the list')
def verify_error(context, item):
    print(item)


@then('close browser')
def close_browser(context):
    context.driver.close()
