# Задание 2: Тестирование Drag & Drop (Перетаскивание изображения в корзину)
# Открыть страницу Drag & Drop Demo.
# Перейти по ссылке: https://www.globalsqa.com/demo-site/draganddrop/.
# Выполнить следующие шаги:
# Захватить первую фотографию (верхний левый элемент).
# Перетащить её в область корзины (Trash).
# Проверить, что после перемещения:
# В корзине появилась одна фотография.
# В основной области осталось 3 фотографии.
# Ожидаемый результат:
# Фотография успешно перемещается в корзину.
# Вне корзины остаются 3 фотографии.
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By



# Открываем браузер и переходим на страницу
url = "https://www.globalsqa.com/demo-site/draganddrop/"
driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window()

iframe = driver.find_element(By.CSS_SELECTOR, "iframe[src*='photo-manager']")
driver.switch_to.frame(iframe)

photo = driver.find_element(By.XPATH, '//ul[@id="gallery"]/li[1]')
trash = driver.find_element(By.ID, 'trash')

actions = ActionChains(driver)
actions.drag_and_drop(photo, trash).perform()

time.sleep(5)

# Проверяем количество фотографий в корзине
photos_in_trash = len(
    driver.find_elements(
        By.XPATH,
        "//div[@id='trash']//ul/li"
    )
)

# Проверяем количество фотографий в галерее
photos_in_gallery = len(
    driver.find_elements(
        By.XPATH,
        "//ul[@id='gallery']/li"
    )
)
assert photos_in_trash == 1
assert photos_in_gallery == 3
time.sleep(3)
driver.quit()

