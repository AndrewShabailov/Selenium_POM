import pytest
from selenium import webdriver
from pages.cart_page import CartPage
from pages.desk_category_page import DeskPage
from pages.office_design_software_page import OfficeDesignSoftwarePage


@pytest.fixture
def driver():
    chrome_driver = webdriver.Chrome()
    return chrome_driver


@pytest.fixture
def cart_page(driver):
    return CartPage(driver)


@pytest.fixture
def desk_page(driver):
    return DeskPage(driver)


@pytest.fixture
def office_design_software_page(driver):
    return OfficeDesignSoftwarePage(driver)
