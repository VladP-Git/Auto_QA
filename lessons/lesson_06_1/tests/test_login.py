from pages.login_page import LoginPage


def test_success_login(driver):
    """
    проверяет успешную авторизацию с валидными данными
    """
    login_page = LoginPage(driver)
    login_page.enter_username('standard_user')
    login_page.enter_password('secret_sauce')
    login_page.click_login_button()
    assert driver.current_url == 'https://www.saucedemo.com/inventory.html'


def test_incorrect_password(driver):
    login_page = LoginPage(driver)
    login_page.enter_username('standard_user')
    login_page.enter_password('incorrect_password')
    login_page.click_login_button()
    assert 'Username and password do not match' in login_page.error_message()


def test_locked_out_user(driver):
    login_page = LoginPage(driver)
    login_page.enter_username('locked_out_user')
    login_page.enter_password('secret_sauce')
    login_page.click_login_button()
    assert 'Sorry, this user has been locked out' in login_page.error_message()


def test_empty_username(driver):
    login_page = LoginPage(driver)
    login_page.get_username_input().clear()
    login_page.enter_password('secret_sauce')
    login_page.click_login_button()
    assert 'Username is required' in login_page.error_message()


def test_empty_password(driver):
    login_page = LoginPage(driver)
    login_page.enter_username('standard_user')
    login_page.get_password_input().clear()
    login_page.click_login_button()
    assert 'Password is required' in login_page.error_message()











