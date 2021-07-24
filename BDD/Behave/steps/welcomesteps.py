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

# --no-capture  use no capture to see print statements
