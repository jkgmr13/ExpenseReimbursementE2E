from behave import given, when, then
from selenium.webdriver.common.alert import Alert


@given(u'The employee has clicked the create button')
def step_impl(context):
    context.employee_page.create().click()


@when(u'The employee enters the amount')
def step_impl(context):
    context.employee_page.amount().send_keys('10')


@when(u'The employee enters the reason')
def step_impl(context):
    context.employee_page.reason().send_keys('To do end to end testing')


@when(u'The employee clicks the submit button')
def step_impl(context):
    context.employee_page.submit().click()


@then(u'A new request should be added to the view page')
def step_impl(context):
    context.employee_page.view().click()
    assert 'To do end to end testing' in context.employee_page.reimbursement_table().get_attribute('innerHTML')


@then(u'An alert should indicate required fields')
def step_impl(context):
    alert = Alert(context.driver)
    assert alert is not None
    alert.dismiss()

