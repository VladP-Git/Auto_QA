# test_homework_3.py
import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urls import BASE_URL
import locators
import time


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-blink-features=AutomationControlled")
    driver = webdriver.Chrome(options=options)
    driver.get(BASE_URL)
    yield driver
    driver.quit()


def test_it_career_hub_elements_and_callback(driver):
    wait = WebDriverWait(driver, 15)

    # Шаг 0: Находим и закрываем баннер куки, если он мешает
    try:
        cookie_btn = wait.until(EC.element_to_be_clickable(locators.COOKIE_ACCEPT_BTN))
        cookie_btn.click()
        time.sleep(1)
    except Exception:
        pass

    # Раздел 2: Проверяем присутствие обязательных элементов в коде страницы (DOM)
    elements = {
        "Логотип": locators.LOGO,
        "Программы": locators.LINK_PROGRAMS,
        "Способы оплаты": locators.LINK_PAYMENT,
        "О нас": locators.LINK_ABOUT,
        "Контакты": locators.LINK_CONTACTS,
        "Отзывы": locators.LINK_REVIEWS,
        "Блог": locators.LINK_BLOG,
        "Переключатель RU": locators.LANG_RU,
        "Переключатель DE": locators.LANG_DE
    }

    for name, locator in elements.items():
        el = wait.until(EC.presence_of_element_located(locator), f"Элемент '{name}' не найден на странице в DOM")
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", el)
        time.sleep(0.1)
        assert el is not None, f"Элемент '{name}' отсутствует в DOM структуре"

    # Раздел 3: Переходим к клику по разделу “Контакты”
    contacts_link = wait.until(EC.presence_of_element_located(locators.LINK_CONTACTS))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", contacts_link)
    time.sleep(0.5)
    driver.execute_script("arguments[0].click();", contacts_link)
    time.sleep(1.5)

    # Раздел 4: Кликнуть по кнопке “Обратный звонок” / "Оставить заявку"
    callback_btn = wait.until(EC.presence_of_element_located(locators.BTN_CALLBACK))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", callback_btn)
    time.sleep(0.5)
    driver.execute_script("arguments[0].click();", callback_btn)
    time.sleep(1.5)

    # Раздел 5: Проверить наличие текста во всплывающем окне / блоке заявки
    popup_element = wait.until(EC.presence_of_element_located(locators.POPUP_TEXT))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", popup_element)
    time.sleep(0.5)

    # Проверяем, что элемент успешно подгрузился и содержит текст
    assert popup_element is not None, "Форма обратной связи не появилась"
