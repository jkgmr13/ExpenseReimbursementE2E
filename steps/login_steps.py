from behave import given, when, then
from behave.runner import Context
from selenium.webdriver.common.alert import Alert


@given(u'The user is on the login page')
def login_page(context: Context):
    context.driver.get('C:\\Users\\jkgmr13\\PycharmProjects\\Project1FrontEnd\\login.html')


@when(u'The employee enters the correct username')
def enter_correct_user_name(context: Context):
    context.login_page.user_input().send_keys("Steve")


@when(u'The employee enters the correct password')
def step_impl(context: Context):
    context.login_page.pass_input().send_keys("Ochinang")


@when(u'The employee clicks the login button')
def step_impl(context: Context):
    context.login_page.login_button().click()


@then(u'The employee should be navigated to the employee page')
def step_impl(context: Context):
    assert context.driver.title == 'Employee'


@when(u'The employee enters the incorrect username')
def step_impl(context: Context):
    context.login_page.user_input().send_keys('steve')


@then(u'The user should see an invalid credentials alert')
def step_impl(context: Context):
    assert Alert(context.driver) is not None


@when(u'The manager enters the correct username')
def step_impl(context: Context):
    context.login_page.user_input().send_keys('jkgmr')


@when(u'The manager enters the correct password')
def step_impl(context: Context):
    context.login_page.pass_input().send_keys('13')


@when(u'The manager clicks the login button')
def step_impl(context: Context):
    context.login_page.login_button().click()


@then(u'The manager should be navigated to the manager page')
def step_impl(context: Context):
    assert context.driver.title == "Manager"


@when(u'The manager enters the incorrect username')
def step_impl(context: Context):
    context.login_page.user_input().send_keys('jkgm')
