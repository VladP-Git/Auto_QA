import pytest
from selenium import webdriver
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


class TestInventory:

    @pytest.fixture(scope="class")
    def driver(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        yield driver
        driver.quit()

    @pytest.fixture(scope="class")
    def inventory_page(self, driver):
        return InventoryPage(driver)

    @pytest.fixture(scope="class", autouse=True)
    def login(self, driver):
        login_page = LoginPage(driver)
        login_page.success_login("standard_user", "secret_sauce")

    def test_items_amount(self, inventory_page):
        """Проверяет количество товаров на странице инвентаря."""
        assert inventory_page.get_items_amount() == 6, \
            "Количество товаров не совпадает."

    def test_all_items_are_displayed(self, inventory_page):
        """Проверяет, что все товары отображаются на странице."""
        assert inventory_page.all_items_are_displayed(), \
            "Не все товары отображаются."

    def test_all_items_names_are_displayed(self, inventory_page):
        """Проверяет отображение названий всех товаров."""
        assert inventory_page.all_items_names_are_displayed(), \
            "Не все названия товаров отображаются."

    def test_all_item_names_are_not_empty(self, inventory_page):
        """Проверяет, что названия товаров не пустые."""
        assert inventory_page.all_item_names_are_not_empty(), \
            "Есть товары с пустыми названиями."

    def test_all_item_names_contains_sauce_labs(self, inventory_page):
        """Проверяет, что названия всех товаров начинаются с 'Sauce Labs'."""
        assert inventory_page.all_item_names_contains_sauce_labs(), \
            "Не все товары начинаются с 'Sauce Labs'."
