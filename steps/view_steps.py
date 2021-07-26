from behave import given, when, then
from behave.runner import Context


@given(u'The employee is logged in')
def step_impl(context: Context):
    context.driver.get('C:\\Users\\jkgmr13\\PycharmProjects\\Project1FrontEnd\\login.html')
    context.login_page.user_input().send_keys("Steve")
    context.login_page.pass_input().send_keys("Ochinang")
    context.login_page.login_button().click()


@given(u'The manager is logged in')
def step_impl(context: Context):
    context.driver.get('C:\\Users\\jkgmr13\\PycharmProjects\\Project1FrontEnd\\login.html')
    context.login_page.user_input().send_keys('jkgmr')
    context.login_page.pass_input().send_keys('13')
    context.login_page.login_button().click()


@when(u'The employee clicks the view button')
def step_impl(context: Context):
    context.employee_page.view().click()


@then(u'Their reimbursements should be displayed')
def step_impl(context: Context):
    assert context.employee_page.reimbursement_table() is not None


@when(u'The manager clicks the view button')
def step_impl(context: Context):
    context.manager_page.view().click()


@then(u'All pending reimbursements should be displayed')
def step_impl(context: Context):
    assert context.manager_page.reimbursement_table() is not None


@then(u'All past reimbursements should be displayed')
def step_impl(context: Context):
    table_button = context.manager_page.table_button().get_attribute('name')
    assert 'past' == table_button


@when(u'The manager clicks the past button')
def step_impl(context):
    context.manager_page.table_button().click()
