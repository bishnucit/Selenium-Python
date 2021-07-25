import time

from behave import *


@then(u'I change option of display to z to a')
def display_z_to_a(context):
    # use -> select z to a option for product display in inventory page
    za_option = context.driver.\
        find_element_by_xpath("//*[@id='header_container']/div[2]/div[2]/span/select/option[2]")
    za_option.click()
    time.sleep(2)


@then(u'I add product number "{value}" on the list to cart from inventory page')
def add_to_cart_product(context, value):
    # use -> add to cart the nth product in the list, if already added don't click
    click_nth_item_add_to_cart = context.driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div/div/div/div["
                                                                      + value + "]/div[2]/div[2]/button")
    if click_nth_item_add_to_cart.text != "REMOVE":
        click_nth_item_add_to_cart.click()
    time.sleep(2)


@then(u'I remove the product from cart')
def remove_product_from_cart_page(context):
    # use -> remove the product from cart page
    remove_from_cart_button = context.driver. \
        find_element_by_xpath("/html/body/div/div/div/div[2]/div/div[1]/div[3]/div[2]/div[2]/button")
    remove_from_cart_button.click()
    time.sleep(2)


@then(u'I can see the count of the cart icon to be "{value}"')
def get_cart_icon_count(context, value):
    # use -> remove the product from cart page
    cart_icon = context.driver.find_element_by_xpath("//*[@id='shopping_cart_container']/a/span")
    if int(cart_icon.text) == int(value):
        assert True
    else:
        assert False
    time.sleep(2)

# --no-capture  use no capture to see print statements
