from locators import cart_locators as locators
from pages.base_page import BasePage


class CartPage(BasePage):
    page_url = 'shop/cart/'


    def check_order_title_is(self, text):
        order_title = self.find_element(locators.cart_overview)
        assert order_title.text == text, f'{order_title.text} != {text}'


    def check_cart_message_is(self, text):
        cart_message = self.find_element(locators.cart_message)
        assert cart_message.text == text, f'{cart_message.text} is not equal to {text}'


    def check_cart_step_label(self, text):
        cart_step_label = self.find_element(locators.cart_step_label)
        assert cart_step_label.text == text, f'{cart_step_label.text} is not equal to {text}'
