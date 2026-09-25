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
#
# def test_implicitly_waiting(driver):
#     driver.implicitly_wait(10)
#     driver.get("https://www.selenium.dev/selenium/web/dynamic.html")
#     driver.find_element(By.ID, 'adder').click()
#     element = driver.find_element(By.ID, 'box0')
#     assert element.get_attribute('class') == 'redbox'
#
# def test_explicitly_wating(driver):
#     driver.get("https://www.selenium.dev/selenium/web/dynamic.html")
#     wait = WebDriverWait(driver, 10)
#     reveal_button = driver.find_element(By.ID, 'reveal')
#     reveal_button.click()
#     element = wait.until(EC.visibility_of_element_located((By.ID, 'revealed')))
#     assert element.is_displayed()
#
# def test_ajax_request_implicit(driver):
#     driver.implicitly_wait(20)
#     driver.get("http://www.uitestingplayground.com/ajax")
#     ajax_button = driver.find_element(By.ID, 'ajaxButton')
#     ajax_button.click()
#     ajax_text_element = driver.find_element(By.CLASS_NAME, 'bg-success')
#     assert 'Data loaded with AJAX get request.' in ajax_text_element.text
#
# def test_wait_for_button(driver):
#     wait = WebDriverWait(driver, 10)
#     driver.get('http://www.uitestingplayground.com/loaddelay')
#     button = wait.until(EC.presence_of_element_located((By.XPATH, "//button[text()='Button Appearing After Delay']")))
#     assert button.is_displayed()




# def test_login_to_orangehrm(driver):
#     driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
#     wait = WebDriverWait(driver, 10)
#
#     username_field = wait.until(EC.presence_of_element_located((By.NAME, 'username')))
#     username_field.send_keys("Admin")
#
#     password_field = wait.until(EC.presence_of_element_located((By.NAME, 'password')))
#     password_field.send_keys("admin123")
#
#     login_button= wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
#     login_button.click()
#
#     dashboard_header = wait.until(EC.text_to_be_present_in_element((By.TAG_NAME, "h6"), "Dashboard"))
#     assert dashboard_header, 'в заголовке нету текста "Dashboard"'
#     assert "dashboard" in driver.current_url

# Пример решения от преподавателя:
def test_show_calculator(driver):
    wait = WebDriverWait(driver, 15)
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    delay_input = driver.find_element(By.ID, "delay")
    delay_input.clear()
    delay_input.send_keys("10")
    driver.find_element(By.XPATH, "//span[text()='7']").click()
    driver.find_element(By.XPATH, "//span[text()='+']").click()
    driver.find_element(By.XPATH, "//span[text()='8']").click()
    driver.find_element(By.XPATH, "//span[text()='=']").click()
    result_element = wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15"))
    assert result_element
    