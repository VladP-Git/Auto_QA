import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import pytest
from urls import CAT_MEMES
from locators import xpath_id_cat_bullet, xpath_id_cat_vova

# driver = webdriver.Chrome()
# driver.get("https://the-internet.herokuapp.com/forgot_password")
#
#
# form = driver.find_element(By.CSS_SELECTOR, "#forgot_password")
# print(form.text)
#
# element_by_xpath = driver.find_element(By.XPATH, '//*[@id="form_submit"]')
# print(element_by_xpath.text)

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get(CAT_MEMES)
    yield driver
    driver.quit()

# def test_find_cat_bullet(driver):
#     cat_bullet = driver.find_element(By.XPATH, xpath_id_cat_bullet)
#     assert cat_bullet.is_displayed() is True
#
# def test_find_cat_vova(driver):
#     cat_vova = driver.find_element(By.XPATH, xpath_id_cat_vova)
#     assert cat_vova.is_displayed() is True

# def test_find_all_cat(driver):
#     cats = driver.find_elements(By.CLASS_NAME, "box-shadow")
#     # for cat in cats:
#     #     print(cat.__repr__())
#     assert 'Lenin cat' in (cats[3].text)

# def test_find_title(driver):
#     title_text = driver.find_element(By.TAG_NAME, "h1").text
#     assert title_text == "Cat memes"

# def test_find_9_mins(driver):
#     cats = driver.find_elements(By.CLASS_NAME, "box-shadow")
#     assert '9 mins' in (cats[1].text)

#FAILED
# def test_find_album(driver):
#     assert driver.find_element(By.XPATH, "/html/body/header/div/a/strong").text == 'Cats album'

def test_login():
    driver = webdriver.Chrome()
    driver.get("http://the-internet.herokuapp.com/login")
    username_field = driver.find_element(By.ID, "username")
    username_field.send_keys("tomsmith")

    username_field = driver.find_element(By.ID, "password")
    username_field.send_keys("SuperSecretPassword!")

    login_button = driver.find_element(By.CLASS_NAME, "fa-sign-in")
    login_button.click()
    time.sleep(5)

    assert driver.find_element(
        By.XPATH,
        "//h4[text()='Welcome to the Secure Area. When you are done click logout below.']"
    )

