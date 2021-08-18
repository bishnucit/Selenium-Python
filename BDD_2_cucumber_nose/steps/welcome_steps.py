from behave import *
from nose.tools import assert_true

@given('user is on the login page')
def step_impl(context):
    context.login_page.navigate_to_site()

@when('user enters valid username "{username}" and valid password "{password}"')
def step_impl(context, username, password):
    context.login_page.login(username, password)

# valid username and invalid password parameters are set in login.feature
@when('user enters valid username "{username}" and invalid password "{password}"')
def step_impl(context, username, password):
    context.login_page.login(username, password)

# if the user can access the account button and sign out then they are logged in
@then('the user is logged in')
def step_impl(context):
    context.inbox_page.logout()

# if the invalid password error appears an invalid password was entered
@then('the user is not logged in')
def step_impl(context):
    assert_true(context.login_page.get_login_error())
