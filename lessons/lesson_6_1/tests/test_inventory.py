import pytest
from selenium import webdriver
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from tests.base_test import BaseTest

ITEMS_AMOUNT = 6


class TestInventory(BaseTest):


    #@pytest.fixture(scope='class')
    #def driver(self):
    #    driver = webdriver.Chrome()
    #    driver.maximize_window()
    #    driver.get("https://www.saucedemo.com/")
    #    yield driver
    #    driver.quit()

    @pytest.fixture(scope='class')
    def inventory_page(self, driver):
        return InventoryPage(driver)


    @pytest.fixture(scope='class', autouse=True)
    def login_page(self, driver):
        login_page = LoginPage(driver)
        login_page.successful_login('standard_user', 'secret_sauce')



    def test_items_amount(self, inventory_page):
        assert inventory_page.get_items_amount() == ITEMS_AMOUNT, 'кол-во товаров некорректное'


    def test_all_items_are_displayed(self, inventory_page):
        assert inventory_page.all_items_are_displayed()

    def test_all_items_names_are_displayed(self, inventory_page):
        assert inventory_page.all_items_name_are_displayed()


    def test_all_item_names_are_not_empty(self, inventory_page):
        assert inventory_page.all_items_names_are_not_empty()

    def test_all_item_names_contains_sauce_labs(self, inventory_page):
        assert inventory_page.all_items_names_contains_sauce_labs(), 'не все названия начинаются с sauce labs'










