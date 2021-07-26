import time

from behave import given, when, then
from selenium.webdriver.common.alert import Alert


@given(u'The manager has clicked the view button')
def step_impl(context):
    context.manager_page.view().click()


@when(u'The manager clicks approve')
def step_impl(context):
    context.approve_length = len(context.manager_page.approve_buttons())
    context.manager_page.approve_buttons()[0].click()


@then(u'The approved request should be removed from the table')
def step_impl(context):
    assert len(context.manager_page.approve_buttons()) < context.approve_length


@then(u'The denied request should be removed from the table')
def step_impl(context):
    assert len(context.manager_page.deny_buttons()) < context.deny_length


@when(u'The manager clicks deny')
def step_impl(context):
    context.deny_length = len(context.manager_page.deny_buttons())
    context.manager_page.deny_buttons()[0].click()


@then(u'The manager should be prompted for a reason')
def step_impl(context):
    alert = Alert(context.driver)
    assert alert is not None


@when(u'The manger completes the prompt')
def step_impl(context):
    alert = Alert(context.driver)
    alert.send_keys("e2e test")
    alert.accept()
    time.sleep(1)

