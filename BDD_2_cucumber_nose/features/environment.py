from features.browser import Browser

def before_all(context):

    # user credentials
    username = 'standard_user'
    password = 'secret_sauce'

    context.browser = Browser()



def after_all(context):
    context.browser.close()
