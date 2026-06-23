from locators import desk_locators as locators
from pages.base_page import BasePage


class DeskPage(BasePage):
    page_url = 'shop/category/desk-1'


    def check_presence_of_customizable_desk_on_page(self, text):
        customizable_desk = self.find_element(locators.customizable_desk)
        assert customizable_desk.text == text, f'{customizable_desk} is not equal to {text}'


    def check_presence_of_corner_desk_left_sit_on_page(self, text):
        corner_desk_left_sit = self.find_element(locators.corner_desk_left_sit)
        assert corner_desk_left_sit.text == text, f'{corner_desk_left_sit} is not equal to {text}'


    def check_presence_of_acoustic_bloc_screens_on_page(self, text):
        acoustic_bloc_screens = self.find_element(locators.acoustic_bloc_screens)
        assert acoustic_bloc_screens.text == text, f'{acoustic_bloc_screens} is not equal to {text}'
