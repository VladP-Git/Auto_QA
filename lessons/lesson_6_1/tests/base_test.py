import pytest
from selenium import webdriver


class BaseTest:
    @pytest.fixture(scope="class")
    def driver(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        yield driver
        driver.quit()
