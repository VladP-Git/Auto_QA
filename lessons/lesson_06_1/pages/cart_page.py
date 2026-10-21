from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def get_cart_item_price(self, item_name):
        item_xpath = f"//div[text()='{item_name}']/ancestor::div[@class='cart_item']//div[@class='inventory_item_price']"
        return self.wait.until(EC.presence_of_element_located((By.XPATH, item_xpath))).text

    def remove_item_from_cart(self, item_name):
        button_xpath = f"//div[text()='{item_name}']/ancestor::div[@class='cart_item']//button"
        self.wait.until(EC.element_to_be_clickable((By.XPATH, button_xpath))).click()

    def proceed_to_checkout(self):
        self.wait.until(EC.presence_of_element_located((By.ID, "checkout"))).click()



