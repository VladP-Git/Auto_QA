import pytest
from selenium import webdriver

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


class TestCheckout:
    @pytest.fixture(scope="class")
    def driver(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        yield driver
        driver.quit()

    @pytest.fixture(scope="class")
    def login_page(self, driver):
        return LoginPage(driver)

    @pytest.fixture(scope="class")
    def inventory_page(self, driver):
        return InventoryPage(driver)

    @pytest.fixture(scope="class")
    def cart_page(self, driver):
        return CartPage(driver)

    @pytest.fixture(scope="class")
    def checkout_page(self, driver):
        return CheckoutPage(driver)

    def test_checkout_total_price(
            self,
            login_page,
            inventory_page,
            cart_page,
            checkout_page
    ):
        print("Шаг 1: Авторизация")
        login_page.success_login("standard_user", "secret_sauce")

        print("Шаг 2: Добавление товаров")
        inventory_page.add_item_to_cart("Sauce Labs Backpack")
        inventory_page.add_item_to_cart("Sauce Labs Bolt T-Shirt")
        inventory_page.add_item_to_cart("Sauce Labs Onesie")

        print("Шаг 3: Переход в корзину")
        inventory_page.go_to_cart()

        print("Шаг 4: Checkout")
        cart_page.proceed_to_checkout()

        print("Шаг 5: Заполнение формы")
        checkout_page.fill_checkout_form("John", "Doe", "12345")

        print("Шаг 6: Чтение итоговой суммы")
        total_price = checkout_page.get_total_price()

        assert total_price == "$58.29", (
            f"Итоговая сумма неверна: {total_price}"
        )