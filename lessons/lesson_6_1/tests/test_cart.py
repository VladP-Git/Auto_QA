import pytest
from selenium import webdriver

from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from pages.cart_page import CartPage
from user_data import StandardUser

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
        login_page.successful_login(StandardUser.username, StandardUser.password)
        backpack_price = inventory_page.get_item_price("Sauce Labs Backpack")
        inventory_page.add_item_to_cart("Sauce Labs Backpack")
        inventory_page.go_to_cart()
        cart_price =  cart_page.get_cart_item_price("Sauce Labs Backpack")
        assert backpack_price == cart_price








