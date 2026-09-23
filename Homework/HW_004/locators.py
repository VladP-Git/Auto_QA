# locators.py
from selenium.webdriver.common.by import By

# --- Локаторы для Задания 1 (Text Input) ---
INPUT_FIELD = (By.ID, "newButtonName")  # Поле для ввода нового имени кнопки
UPDATING_BUTTON = (By.ID, "updatingButton")  # Синяя кнопка, меняющая имя

# --- Локаторы для Задания 2 (Loading Images) ---
# Ищем картинки строго внутри целевого блока галереи (id="image-container")
GALLERY_IMAGES = (By.CSS_SELECTOR, "#image-container img")
# Ожидаем появления блока с картинками
IMAGE_CONTAINER = (By.ID, "image-container")
