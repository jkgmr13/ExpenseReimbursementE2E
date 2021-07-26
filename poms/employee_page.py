from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class EmployeePage:

    def __init__(self, web_driver: WebDriver):
        self.web_driver = web_driver

    def view(self) -> WebElement:
        element = self.web_driver.find_element_by_id('view')
        return element

    def create(self) -> WebElement:
        element = self.web_driver.find_element_by_id('create')
        return element

    def logout(self) -> WebElement:
        element = self.web_driver.find_element_by_id('logout')
        return element

    def reimbursement_table(self) -> WebElement:
        element = self.web_driver.find_element_by_id('reimbursementTable')
        return element

    def amount(self) -> WebElement:
        element = self.web_driver.find_element_by_id('amount')
        return element

    def reason(self) -> WebElement:
        element = self.web_driver.find_element_by_id('reason')
        return element
    
    def submit(self) -> WebElement:
        element = self.web_driver.find_element_by_id('rrSubmit')
        return element

    def file(self) -> WebElement:
        element = self.web_driver.find_element_by_id('myFile')
        return element



