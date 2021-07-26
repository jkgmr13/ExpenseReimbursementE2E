from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class LoginPage:

    def __init__(self, web_driver: WebDriver):
        self.web_driver = web_driver

    def user_input(self) -> WebElement:
        element = self.web_driver.find_element_by_id('userName')
        return element

    def pass_input(self) -> WebElement:
        element = self.web_driver.find_element_by_id('passWord')
        return element

    def login_button(self) -> WebElement:
        element = self.web_driver.find_element_by_id('login')
        return element
