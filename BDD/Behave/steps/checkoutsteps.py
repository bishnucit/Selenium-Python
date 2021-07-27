import time

from behave import *


@given(u'I am at checkout page')
def perform_add_cart(context):
    # use -> performing many steps to add product in cart and then navigate to checkout page
    context.execute_steps(u'''
        Given open test site
        When I enter valid username and password
        Then I add product number "6" on the list to cart from inventory page
        Then I change option of display to z to a
        Then I add product number "6" on the list to cart from inventory page
        Then I change option of display to low to high
        Then I add product number "6" on the list to cart from inventory page
        Then I change option of display to high to low
        Then I add product number "6" on the list to cart from inventory page
        Then I click on the cart button
    ''')

    click_checkout = context.driver.find_element_by_xpath("//*[@id='checkout']")
    click_checkout.click()
    time.sleep(2)


@when(u'I click on Continue button without entering any text')
def click_continue_at_checkout(context):
    # use -> click continue button
    click_checkout = context.driver.find_element_by_xpath("//*[@id='continue']")
    click_checkout.click()
    time.sleep(2)


@then(u'I can see error message')
def verify_error_message(context):
    # use -> verify error message
    click_check = context.driver.find_element_by_xpath("//*[@id='checkout_info_container']/div/form/div[1]/div[4]/h3")
    assert click_check.is_displayed()
    time.sleep(2)


@then(u'If i click on cancel, it takes me back to previous page')
def navigate_back_to_cart_page(context):
    # use -> navigate back to cart page from checkout page by clicking cancel
    click_check = context.driver.find_element_by_xpath("//*[@id='cancel']")
    click_check.click()
    time.sleep(2)
    cart_title = context.driver.find_element_by_xpath("//*[@id='header_container']/div[2]/span")
    assert cart_title.is_displayed()
    time.sleep(2)


@then(u'I click on Checkout button again and i am at checkout page')
def navigate_to_checkout_page(context):
    # use -> navigate from cart to checkout page
    click_checkout = context.driver.find_element_by_xpath("//*[@id='checkout']")
    click_checkout.click()
    time.sleep(2)


@then(u'If i enter First Name, Last name, Zip code and click on Continue button')
def step_impl(context):
    # use -> enter name (first/last) and zipcode, click on continue button
    first_name = context.driver.find_element_by_id("first-name")
    first_name.send_keys("Test")
    last_name = context.driver.find_element_by_id("last-name")
    last_name.send_keys("user")
    postal_code = context.driver.find_element_by_id("postal-code")
    postal_code.send_keys("560095")
    continue_button = context.driver.find_element_by_id("continue")
    continue_button.click()
    time.sleep(2)


@then(u'I am navigated to finish checkout page')
def verify_checkout(context):
    # use -> verify finish checkout page
    final_checkout = context.driver.find_element_by_xpath("//*[@id='header_container']/div[2]/span")
    assert final_checkout.is_displayed()
    time.sleep(2)


@then(u'I click on cancel, it takes me to inventory page')
def step_impl(context):
    # use -> cancel checkout and goto inventory page
    cancel_button = context.driver.find_element_by_id("cancel")
    cancel_button.click()
    time.sleep(2)
    inventory_page = context.driver.find_element_by_xpath("//*[@id='header_container']/div[2]/span")
    assert inventory_page.is_displayed()
