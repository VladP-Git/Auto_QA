from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_implicitly_waiting(driver):
    driver.implicitly_wait(10)
    driver.get("https://www.selenium.dev/selenium/web/dynamic.html")
    driver.find_element(By.ID, 'adder').click()
    element = driver.find_element(By.ID, 'box0')
    assert element.get_attribute('class') == 'redbox'

def test_explicitly_wating(driver):
    driver.get("https://www.selenium.dev/selenium/web/dynamic.html")
    wait = WebDriverWait(driver, 10)
    reveal_button = driver.find_element(By.ID, 'reveal')
    reveal_button.click()
    element = wait.until(EC.visibility_of_element_located((By.ID, 'revealed')))
    assert element.is_displayed()

def test_ajax_request_implicit(driver):
    driver.implicitly_wait(20)
    driver.get("http://www.uitestingplayground.com/ajax")
    ajax_button = driver.find_element(By.ID, 'ajaxButton')
    ajax_button.click()
    ajax_text_element = driver.find_element(By.CLASS_NAME, 'bg-success')
    assert 'Data loaded with AJAX get request.' in ajax_text_element.text

def test_wait_for_button(driver):
    wait = WebDriverWait(driver, 10)
    driver.get('http://www.uitestingplayground.com/loaddelay')
    button = wait.until(EC.presence_of_element_located((By.XPATH, "//button[text()='Button Appearing After Delay']")))
    assert button.is_displayed()