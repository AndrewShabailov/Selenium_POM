from pages.base_page import BasePage
from locators import office_design_software_locators as locators


class OfficeDesignSoftwarePage(BasePage):
    page_url = 'shop/furn-9999-office-design-software-7?category=9'


    def check_item_title_is(self, text):
        item_title = self.find_element(locators.item_title)
        assert item_title.text == text, f'{item_title} is not equal to {text}'


    def check_item_price_is(self, text):
        item_price = self.find_element(locators.item_price)
        assert item_price.text == text, f'{item_price} is not equal to {text}'


    def check_item_image_is_displayed(self):
        item_image = self.find_element(locators.item_image)
        assert item_image.is_displayed(), f'{item_image} is not displayed'
        item_image.screenshot('screenshot.png')
