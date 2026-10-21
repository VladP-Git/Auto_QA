# Задание 1: Проверка наличия текста в iframe, нужно:
# Открыть страницу и # Перейти по ссылке: https://bonigarcia.dev/selenium-webdriver-java/iframes.html.
# Проверить наличие текста
# Найти фрейм (iframe), в котором содержится искомый текст.
# Переключиться в этот iframe.
# Найти элемент, содержащий текст "semper posuere integer et senectus justo curabitur.".
# Убедиться, что текст отображается на странице.

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def browser():
    """Создаёт и закрывает браузер после теста."""
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_iframe_text(browser):
    browser.get("https://bonigarcia.dev/selenium-webdriver-java/iframes.html")


    iframe = browser.find_element(By.TAG_NAME, "iframe")
    browser.switch_to.frame(iframe)
    body = browser.find_element(By.TAG_NAME, "body")
    # print(body.text)
    assert 'Lorem ipsum dolor sit amet consectetur adipiscing elit habitant metus' in body.text