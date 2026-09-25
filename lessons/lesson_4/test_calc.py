import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import urls
import locators
import time


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


def test_slow_calculator(driver):
    # 1. Откройте страницу Slow Calculator
    driver.get(urls.URL_SLOW_CALCULATOR)

    # Инициализируем стандартное ожидание для элементов управления
    wait = WebDriverWait(driver, 10)

    # 2. В поле ввода по локатору #delay введите значение 45
    delay_field = wait.until(EC.visibility_of_element_located(locators.DELAY_INPUT))

    delay_field.clear()  # Очищаем дефолтную пятёрку
    delay_field.send_keys("4.5")  # Устанавливаем задержку в 4.5 секунд
    time.sleep(0.5)  # Небольшая пауза для фиксации значения в поле

    # Список кнопок для последовательного нажатия
    buttons_to_click = [
        locators.BTN_7,
        locators.BTN_PLUS,
        locators.BTN_8,
        locators.BTN_EQUAL
    ]

    # 3. Нажимаем кнопки по порядку с использованием JavaScript-клика
    for btn_locator in buttons_to_click:
        btn_element = wait.until(EC.presence_of_element_located(btn_locator))
        driver.execute_script("arguments[0].click();", btn_element)
        time.sleep(0.2)  # Пауза между нажатиями кнопок для симуляции реального ввода

    # 4. Проверяем (assert), что в окне отображается результат 15 через 45 секунд.
    # Создаем длинное ожидание на 55 секунд (45 секунд задержки + 10 секунд запас)
    long_wait = WebDriverWait(driver, 55)

    # Ждем появления точного текста "15" на дисплее калькулятора
    result_loaded = long_wait.until(
        EC.text_to_be_present_in_element(locators.CALC_SCREEN, "15")
    )

    # Финальная проверка истинности
    assert result_loaded, "Результат '15' не отобразился на экране калькулятора в течение заданного времени"
