import os
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def driver():
    """Фикстура для инициализации и закрытия браузера Firefox."""
    # Используем Firefox
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield drivery
    driver.quit()


def test_screenshot_payment_section(driver):
    """Тест открывает главную страницу, переходит к способам оплаты и делает скриншот."""
    # 1. Открываем сайт
    driver.get("https://itcareerhub.de/ru")
    time.sleep(2)  # Небольшая пауза для полной загрузки стилей

    # 2. Находим кнопку "Способы оплаты" в меню и кликаем
    payment_button = driver.find_element(By.LINK_TEXT, "Способы оплаты")
    payment_button.click()
    time.sleep(1)  # Ждем завершения плавной прокрутки к секции

    # 3. Находим саму секцию со способами оплаты
    # На странице этот блок имеет заголовок "Подберите подходящий способ оплаты обучения"
    payment_section = driver.find_element(
        By.XPATH, "//*[contains(text(), 'Подберите подходящий способ оплаты')]/.."
    )

    # Двигаем экран к секции, чтобы она гарантированно была видима
    driver.execute_script("arguments[0].scrollIntoView(true);", payment_section)
    time.sleep(1)

    # 4. Делаем скриншот именно этой секции страницы
    screenshot_path = "payment_section.png"
    payment_section.screenshot(screenshot_path)

    # Проверяем, что файл скриншота успешно создался
    assert os.path.exists(screenshot_path)
    print(f"\nСкриншот секции успешно сохранен: {os.path.abspath(screenshot_path)}")