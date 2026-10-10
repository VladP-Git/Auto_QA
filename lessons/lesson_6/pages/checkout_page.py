from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def fill_checkout_form(self, first_name, last_name, postal_code):
        first_name_field = self.wait.until(
            EC.visibility_of_element_located((By.ID, "first-name"))
        )
        first_name_field.clear()
        first_name_field.send_keys(first_name)

        last_name_field = self.wait.until(
            EC.visibility_of_element_located((By.ID, "last-name"))
        )
        last_name_field.clear()
        last_name_field.send_keys(last_name)

        postal_code_field = self.wait.until(
            EC.visibility_of_element_located((By.ID, "postal-code"))
        )
        postal_code_field.clear()
        postal_code_field.send_keys(postal_code)

        self.wait.until(
            EC.element_to_be_clickable((By.ID, "continue"))
        ).click()

    def get_total_price(self):
        total_element = self.wait.until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, "summary_total_label")
            )
        )
        return total_element.text.split(": ")[1]
