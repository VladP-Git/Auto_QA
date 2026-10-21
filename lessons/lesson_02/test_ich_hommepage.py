import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.common.by import By


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_about_button(driver):
    driver.get("https://itcareerhub.de/ru")
    about_button = driver.find_element(By.LINK_TEXT, 'О нас')
    about_button.click()
    about_company = driver.find_element(By.LINK_TEXT, 'О компании')
    assert about_company.text == 'О компании'
    print(about_company.text)
