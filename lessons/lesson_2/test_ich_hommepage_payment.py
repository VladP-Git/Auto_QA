from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time
from urls import HOMEPAGE

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get(HOMEPAGE)
    yield driver
    driver.quit()

def test_about_button(driver):
    """
    1) кликаем по кнопке о нас
    2) проверяем наличие текста
    """
    about_button = driver.find_element(By.LINK_TEXT, 'О нас')
    about_button.click()
    about_company = driver.find_element(By.LINK_TEXT, 'О компании')
    assert about_company.text == 'О компании'
def test_payment_methods(driver):
    payment_methods_button = driver.find_element(By.LINK_TEXT, "Способы оплаты")
    time.sleep(2)
    payment_methods_button.click()
    payment_section = driver.find_element(By.XPATH, "//*[@id='rec1921734713']/div/div/div[5]/h2")
    time.sleep(2)
    payment_section.screenshot('screenshots/01_payment_section.png')
    driver.save_screenshot('screenshots/02_payment_fullsection.png')
    print('скриншот готов')
    time.sleep(2)