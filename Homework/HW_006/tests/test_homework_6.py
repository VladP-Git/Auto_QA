import pytest
import time
from selenium import webdriver

# ИСПРАВЛЕНО: Так как pytest.ini уже видит текущую папку, импортируем напрямую!
from Homework.HW_006.pages.login_page import LoginPage
from Homework.HW_006.pages.inventory_page import InventoryPage
from Homework.HW_006.pages.cart_page import CartPage
from Homework.HW_006.pages.checkout_page import CheckoutPage
from Homework.HW_006.user_data import StandardUser


def test_saucedemo_full_purchase_flow(driver):
    """Домашнее задание 6: Сквозной сценарий покупки 3-х товаров с проверкой Total."""

    # Инициализация объектов страниц
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    # Список товаров из задания
    items_to_buy = [
        "Sauce Labs Backpack",
        "Sauce Labs Bolt T-Shirt",
        "Sauce Labs Onesie"
    ]

    # 1 & 2. Открываем сайт и авторизуемся
    login_page.open()
    login_page.successful_login(StandardUser.username, StandardUser.password)

    # 3. Добавляем указанные товары в корзину
    for item in items_to_buy:
        inventory_page.add_item_to_cart(item)

    # 4. Переходим в корзину
    inventory_page.go_to_cart()

    # 5. Нажимаем Checkout
    cart_page.proceed_to_checkout()

    # 6. Заполняем форму своими данными
    checkout_page.fill_checkout_form(
        first_name="Ivan",
        last_name="Ivanov",
        postal_code="123456"
    )

    # 7. Читаем со страницы итоговую стоимость (Total)
    total_price_text = checkout_page.get_total_price()

    # 8 & 9. Закрытие браузера произойдет автоматически фикстурой driver.
    # Проверяем, что итоговая сумма равна $58.29
    expected_total = "$58.29"
    assert expected_total in total_price_text, f"Ожидалась сумма {expected_total}, но на странице отображено: '{total_price_text}'"
