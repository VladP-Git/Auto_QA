import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def driver():
    """Фикстура инициализирует Chrome с отключенными уведомлениями об утечке паролей."""
    chrome_options = Options()

    # Отключаем встроенное окно Chrome "Смените пароль"
    chrome_options.add_experimental_option("prefs", {
        "profile.password_manager_leak_detection": False,
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    })

    # Дополнительно убираем инфо-панель "Браузером управляет автоматизированное ПО"
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.use_experimental_option = False

    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    yield driver
    driver.quit()