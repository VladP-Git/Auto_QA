import pytest
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def browser():
    """Фикстура для инициализации браузера.
    Создаёт и автоматически закрывает браузер после окончания теста.
    """
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_iframe_text(browser):
    """Задание 1: Проверка текста в iframe с динамическим ожиданием загрузки."""
    browser.get("https://bonigarcia.dev/selenium-webdriver-java/iframes.html")

    # Находим фрейм и переключаемся в него
    iframe = browser.find_element(By.TAG_NAME, "iframe")
    browser.switch_to.frame(iframe)

    # УМНОЕ ОЖИДАНИЕ: Ждем до 10 секунд, пока элемент body появится в DOM-дереве фрейма.
    wait = WebDriverWait(browser, 10)
    body = wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

    # Небольшая страховка: ждем, пока текст внутри body перестанет быть пустым
    wait.until(lambda d: body.text != "")

    expected_text = 'Lorem ipsum dolor sit amet consectetur adipiscing elit habitant metus'
    assert expected_text in body.text, f"Текст не совпал. Текущий текст в iframe: '{body.text}'"
