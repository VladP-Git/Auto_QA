from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.login_page_locators import LoginPageLocators


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get("https://www.saucedemo.com/")

    def get_username_input(self):
        return self.wait.until(EC.presence_of_element_located((By.ID, LoginPageLocators.username_input)))

    def get_password_input(self):
        return self.wait.until(EC.presence_of_element_located((By.ID, LoginPageLocators.password_input)))

    def get_login_button(self):
        return self.wait.until(EC.presence_of_element_located((By.ID, LoginPageLocators.login_button)))

    def enter_username(self, username):
        username_field = self.get_username_input()
        username_field.clear()
        username_field.send_keys(username)

    def enter_password(self, password):
        username_field = self.get_password_input()
        username_field.clear()
        username_field.send_keys(password)

    def click_login_button(self):
        self.get_login_button().click()

    def error_message(self):
        return self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "error-message-container"))).text

    def successful_login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()













