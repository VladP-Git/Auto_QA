# test_homework_4.py
import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import urls
import locators


@pytest.fixture
def driver():
    # Настраиваем автоматическое раскрытие окна браузера
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


# ================= ЗАДАНИЕ 1 =================
def test_change_button_text(driver):
    # 1. Перейдите на сайт Text Input
    driver.get(urls.URL_TEXT_INPUT)
    wait = WebDriverWait(driver, 10)

    # 2. Введите в поле ввода текст "ITCH"
    input_field = wait.until(EC.visibility_of_element_located(locators.INPUT_FIELD))
    input_field.send_keys("ITCH")

    # 3. Нажмите на синюю кнопку
    button = wait.until(EC.element_to_be_clickable(locators.UPDATING_BUTTON))
    button.click()

    # 4. Проверьте, что текст кнопки изменился на "ITCH"
    assert button.text == "ITCH", f"Ожидался текст кнопки 'ITCH', но получили '{button.text}'"


# ================= ЗАДАНИЕ 2 =================
def test_loading_images_alt_attribute(driver):
    # 1. Перейдите на сайт Loading Images
    driver.get(urls.URL_LOADING_IMAGES)
    wait = WebDriverWait(driver, 15)

    # 2. Дожидаемся, пока контейнер для изображений станет видимым
    wait.until(EC.visibility_of_element_located(locators.IMAGE_CONTAINER))

    # Так как картинки подгружаются последовательно, подождём, пока загрузится третья картинка в галерее
    # Для этого используем явное ожидание, проверяя, что количество элементов в контейнере стало >= 3
    wait.until(lambda d: len(d.find_elements(*locators.GALLERY_IMAGES)) >= 3)

    # Получаем актуальный список картинок из галереи
    images_list = driver.find_elements(*locators.GALLERY_IMAGES)

    # 3. Получите значение атрибута alt у третьего изображения в галерее
    target_image = images_list[2]  # Индекс 2 — это третий элемент
    alt_value = target_image.get_attribute("alt")

    # Выведем в лог для отладки, какие alt успели подгрузиться
    all_alts = [img.get_attribute("alt") for img in images_list]
    print(f"\nЗагруженные атрибуты alt в галерее: {all_alts}")

    # 4. Убедитесь, что значение атрибута alt равно "award"
    assert alt_value == "award", f"Ожидался атрибут alt='award', но на 3-й позиции получен '{alt_value}'. Все картинки: {all_alts}"
