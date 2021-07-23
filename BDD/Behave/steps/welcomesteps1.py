import time

from behave import *
from selenium import webdriver


@given('launch chrome browser')
def launchbrowser(context):
    context.driver = webdriver.Chrome()


@when('open test site')
def openpage(context):
    context.driver.get("https://www.saucedemo.com/")


@then('verify that the webpage has some content')
def verifycontent(context):
    status = context.driver.find_element_by_xpath("//*[@id='root']/div/div[2]/div[1]/div[2]").is_displayed()
    assert status is True


@given(u'open test site')
def openpage(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.saucedemo.com/")


@when(u'I enter valid username and password')
def enteruandp(context):
    username = context.driver.find_element_by_id("user-name")
    username.send_keys("standard_user")

    username = context.driver.find_element_by_id("password")
    username.send_keys("secret_sauce")

    login = context.driver.find_element_by_id("login-button")
    login.click()


@then(u'I am successfully logged in')
def verifyinventorypage(context):
    time.sleep(5)
    status = context.driver.find_element_by_xpath("//*[@id='header_container']/div[1]/div[2]/div").is_displayed()
    assert status is True


@when(u'I enter invalid username and password')
def enterinvaliduandp(context):
    username = context.driver.find_element_by_id("user-name")
    username.send_keys("standard_user1")

    username = context.driver.find_element_by_id("password")
    username.send_keys("secret_sauce1")

    login = context.driver.find_element_by_id("login-button")
    login.click()


@then(u'I can see the error message')
def verifyerror(context):
    time.sleep(2)
    status = context.driver.find_element_by_xpath("//*[@id='login_button_container']/div/form/div[3]/h3").is_displayed()
    assert status is True

    
@then(u'I logout and close browser')
def verifyerror(context):
    time.sleep(2)
    context.driver.find_element_by_xpath("//*[@id='react-burger-menu-btn']").click()
    time.sleep(1)
    context.driver.find_element_by_xpath("//*[@id='logout_sidebar_link']").click()
    time.sleep(1)
    status = context.driver.find_element_by_xpath("//*[@id='root']/div/div[2]/div[1]/div[2]").is_displayed()
    assert status is True
    context.driver.close()


@then('close browser')
def closebrowser(context):
    context.driver.close()
