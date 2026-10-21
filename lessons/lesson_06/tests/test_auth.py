from selenium.webdriver.common.by import By
from pages.login_page import LoginPage


def test_success_login_valid_data(driver):
    """Проверяет успешный вход с корректными учетными данными."""
    user_name_input_field = driver.find_element(By.ID, "user-name")
    user_name_input_field.send_keys("standard_user")
    password_input_field = driver.find_element(By.ID, "password")
    password_input_field.send_keys("secret_sauce")
    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()
    assert driver.current_url == "https://www.saucedemo.com/inventory.html", "Не удалось войти в систему."
    inventory_list = driver.find_element(By.CLASS_NAME, "inventory_list")
    assert inventory_list, "Список товаров не найден на странице."


def test_invalid_password(driver):
    """Проверяет отображение ошибки при вводе неверного пароля."""
    user_name_input_field = driver.find_element(By.ID, "user-name")
    user_name_input_field.send_keys("standard_user")
    password_input_field = driver.find_element(By.ID, "password")
    password_input_field.send_keys("wrong_password")
    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()
    error_message = driver.find_element(By.CLASS_NAME, "error-message-container")
    assert error_message, "Сообщение об ошибке не отображается."
    assert "Username and password do not match" in error_message.text, "Неверное сообщение об ошибке."


def test_locked_out_user(driver):
    """Проверяет невозможность входа заблокированного пользователя."""
    user_name_input_field = driver.find_element(By.ID, "user-name")
    user_name_input_field.send_keys("locked_out_user")
    password_input_field = driver.find_element(By.ID, "password")
    password_input_field.send_keys("secret_sauce")
    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()
    error_message = driver.find_element(By.CLASS_NAME, "error-message-container")
    assert error_message, "Сообщение об ошибке не отображается."
    assert "Sorry, this user has been locked out." in error_message.text, "Неверное сообщение об ошибке."


def test_empty_username(driver):
    """Проверяет отображение ошибки при пустом поле имени пользователя."""
    password_input_field = driver.find_element(By.ID, "password")
    password_input_field.send_keys("secret_sauce")
    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()
    error_message = driver.find_element(By.CLASS_NAME, "error-message-container")
    assert error_message, "Сообщение об ошибке не отображается."
    assert "Username is required" in error_message.text, "Неверное сообщение об ошибке."


def test_empty_password(driver):
    """Проверяет отображение ошибки при пустом поле пароля."""
    user_name_input_field = driver.find_element(By.ID, "user-name")
    user_name_input_field.send_keys("standard_user")
    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()
    error_message = driver.find_element(By.CLASS_NAME, "error-message-container")
    assert error_message, "Сообщение об ошибке не отображается."
    assert "Password is required" in error_message.text, "Неверное сообщение об ошибке."






def test_successful_login(driver):
    login_page = LoginPage(driver)
    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_on_login_button()
    assert "inventory.html" in driver.current_url, "Не удалось войти в систему."

def test_invalid_password(driver):
    login_page = LoginPage(driver)
    login_page.enter_username("standard_user")
    login_page.enter_password("wrong_password")
    login_page.click_on_login_button()
    assert "Username and password do not match" in login_page.error_message(), "Неверное сообщение об ошибке."


def test_locked_out_user(driver):
    login_page = LoginPage(driver)
    login_page.enter_username("locked_out_user")
    login_page.enter_password("secret_sauce")
    login_page.click_on_login_button()
    assert "Sorry, this user has been locked out." in login_page.error_message(), "Неверное сообщение об ошибке."


def test_empty_username(driver):
    login_page = LoginPage(driver)
    login_page.enter_password("secret_sauce")
    login_page.click_on_login_button()
    assert "Username is required" in login_page.error_message(), "Неверное сообщение об ошибке."


def test_empty_password(driver):
    login_page = LoginPage(driver)
    login_page.enter_username("standard_user")
    login_page.click_on_login_button()
    assert "Password is required" in login_page.error_message(), "Неверное сообщение об ошибке."









