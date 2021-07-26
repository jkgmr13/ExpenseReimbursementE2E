from behave import when, then


@when(u'The employee clicks the logout button')
def step_impl(context):
    context.employee_page.logout().click()


@then(u'The employee should be redirected to the login page')
def step_impl(context):
    assert context.driver.title == 'Login'


@when(u'The manager clicks the logout button')
def step_impl(context):
    context.manager_page.logout().click()

@then(u'The manager should be redirected to the login page')
def step_impl(context):
    assert context.driver.title == 'Login'
