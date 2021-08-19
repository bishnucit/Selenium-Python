from behave import *


@given(u'user is on login page')
def step_checklogin(context):
    context.login_page.navigate_to_site()

@when(u'I enter valid username "{username}" and password "{password}"')
def enter_correct_details(context, username, password):
    context.login_page.login(username, password)

@then(u'I am successfully logged in')
def verify_login(context):
    context.login_page.verify_inventory()

@when(u'I enter invalid username "{username}" and password "{password}"')
def enter_incorrect_details(context, username, password):
    context.login_page.fake_login(username, password)

@then(u'I am not logged in and i can see an error message')
def verify_error(context):
    context.login_page.get_login_error()
