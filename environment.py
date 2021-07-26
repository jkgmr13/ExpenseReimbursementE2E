from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

# Environment is like a config file for your cucumber tests
from selenium.webdriver.firefox.webdriver import WebDriver

from poms.employee_page import EmployeePage
from poms.login_page import LoginPage
from poms.manager_page import ManagerPage


def before_all(context):
    binary = FirefoxBinary('C:\\Program Files\\Mozilla Firefox\\firefox.exe')
    context.driver: WebDriver = webdriver.Firefox(firefox_binary=binary,
                                                  executable_path="C:\\Users\\jkgmr13\\Desktop\\drivers\\geckodriver"
                                                                  ".exe")
    context.login_page = LoginPage(context.driver)
    context.employee_page = EmployeePage(context.driver)
    context.manager_page = ManagerPage(context.driver)
    context.driver.implicitly_wait(10)


def after_all(context):
    context.driver.quit()
