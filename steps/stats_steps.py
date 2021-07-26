from behave import when, then


@when(u'The manager clicks the stat button')
def step_impl(context):
    context.manager_page.stats().click()


@then(u'Tables containing data should be displayed')
def step_impl(context):
    chart1 = context.manager_page.reimbursement_chart().get_attribute('style')
    chart2 = context.manager_page.rejected_chart().get_attribute('style')
    assert chart1 is not None and chart2 is not None
