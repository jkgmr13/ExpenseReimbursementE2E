from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class ManagerPage:

    def __init__(self, web_driver: WebDriver):
        self.web_driver = web_driver

    def view(self) -> WebElement:
        element = self.web_driver.find_element_by_id('view')
        return element

    def stats(self) -> WebElement:
        element = self.web_driver.find_element_by_id('stats')
        return element

    def logout(self) -> WebElement:
        element = self.web_driver.find_element_by_id('logout')
        return element

    def reimbursement_table(self) -> WebElement:
        element = self.web_driver.find_element_by_id('reimbursementTable')
        return element

    def table_button(self) -> WebElement:
        element = self.web_driver.find_element_by_id('tableButton')
        return element

    def approve_buttons(self) -> list[WebElement]:
        elements = self.web_driver.find_elements_by_class_name('approveButtons')
        return elements

    def deny_buttons(self) -> list[WebElement]:
        elements = self.web_driver.find_elements_by_class_name('denyButtons')
        return elements

    def reimbursement_chart(self) -> WebElement:
        element = self.web_driver.find_element_by_id('myChart1')
        return element

    def rejected_chart(self) -> WebElement:
        element = self.web_driver.find_element_by_id('myChart2')
        return element
