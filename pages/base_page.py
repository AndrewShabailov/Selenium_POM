from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    base_url = 'http://testshop.qa-practice.com/'
    page_url = None


    def __init__(self, driver: WebDriver):
        self.driver = driver


    def open_page(self):
        if self.page_url:
            self.driver.get(f'{self.base_url}{self.page_url}')
        else:
            raise NotImplementedError('Page not opened')

    def find_element(self, locator: tuple, timeout: int = 5):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )


    def find_elements(self, locator: tuple, timeout: int = 5):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_all_elements_located(locator)
        )
