import pytest
from selenium import webdriver

from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from pages.cart_page import CartPage


class TestCart:
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

    @pytest.fixture(scope="class")
    def login_page(self, driver):
        return LoginPage(driver)

    @pytest.fixture(scope="class")
    def cart_page(self, driver):
        return CartPage(driver)


    def test_backpack_cost(self, login_page, inventory_page, cart_page):
        """Проверяет, что цена товара в корзине совпадает с ценой на странице инвентаря."""

        # 1. Авторизуемся с валидными учетными данными.
        login_page.success_login("standard_user", "secret_sauce")

        # 2. Запоминаем цену товара "Sauce Labs Backpack" на странице инвентаря.
        backpack_price = inventory_page.get_item_price("Sauce Labs Backpack")

        # 3. Добавляем товар "Sauce Labs Backpack" в корзину.
        inventory_page.add_item_to_cart("Sauce Labs Backpack")

        # 4. Переходим в корзину.
        inventory_page.go_to_cart()

        # 5. Получаем цену товара в корзине.
        cart_price = cart_page.get_cart_item_price("Sauce Labs Backpack")

        # 6. Проверяем, что цена товара в корзине совпадает с ценой на странице инвентаря.
        assert backpack_price == cart_price, (
            "Цена товара в корзине не совпадает с ценой на странице инвентаря."
        )




