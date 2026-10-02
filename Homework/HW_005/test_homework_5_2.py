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
    Создаёт экземпляр Chrome, разворачивает его и гарантированно закрывает после теста.
    """
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_drag_and_drop_images(browser):
    """Тестирование Drag & Drop с блокировкой перекрывающего рекламного баннера и окна согласия."""
    url = "https://www.globalsqa.com/demo-site/draganddrop/"
    browser.get(url)

    # Инициализируем явное ожидание
    wait = WebDriverWait(browser, 5)

    # 1. ОБРАБОТКА ОКНА СОГЛАСИЯ (Cookie-баннер fc-consent-root)
    try:
        consent_button = wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR,
                 "div.fc-consent-root button.fc-cta-consent, div.fc-consent-root button[aria-label='Consent']")
            )
        )
        consent_button.click()
        print("\n[INFO] Окно согласия успешно закрыто.")
        time.sleep(1.5)
    except Exception:
        print("\n[INFO] Окно согласия не появилось, продолжаем.")

    # 2. ИСПРАВЛЕНО: Полное уничтожение рекламного баннера снизу страницы через JavaScript
    # Находим любой подозрительный iframe или div с рекламой внизу страницы и скрываем его
    try:
        browser.execute_script("""
            var ads = document.querySelectorAll('iframe[id*="aswift"], div[class*="ad"], ins.adsbygoogle');
            ads.forEach(function(ad) { ad.style.display = 'none'; });

            // Также принудительно скрываем нижнюю фиксированную панель, если она создана div-ом
            var bottomBanners = document.querySelectorAll('div[style*="position: fixed"], div[style*="bottom: 0"]');
            bottomBanners.forEach(function(banner) { banner.style.display = 'none'; });
        """)
        print("[INFO] Рекламный баннер успешно заблокирован и скрыт.")
    except Exception:
        print("[INFO] Не удалось выполнить JS для скрытия рекламы.")

    # 3. Переключение во фрейм с менеджером фотографий
    iframe = browser.find_element(By.CSS_SELECTOR, "iframe[src*='photo-manager']")
    browser.switch_to.frame(iframe)

    # 4. Поиск элементов для перетаскивания
    photo = browser.find_element(By.XPATH, '//ul[@id="gallery"]/li')
    trash = browser.find_element(By.ID, 'trash')

    # 5. Выполнение Drag & Drop
    actions = ActionChains(browser)
    actions.drag_and_drop(photo, trash).perform()

    # Даем время на завершение анимации падения картинки
    time.sleep(5)

    # Подсчет результатов
    photos_in_trash = len(
        browser.find_elements(By.XPATH, "//div[@id='trash']//ul/li")
    )

    photos_in_gallery = len(
        browser.find_elements(By.XPATH, "//ul[@id='gallery']/li")
    )

    # Проверка выполнения условий
    assert photos_in_trash == 1, f"Ошибка: В корзине должно быть 1 фото, но там: {photos_in_trash}"
    assert photos_in_gallery == 3, f"Ошибка: В галерее должно быть 3 фото, но там: {photos_in_gallery}"
