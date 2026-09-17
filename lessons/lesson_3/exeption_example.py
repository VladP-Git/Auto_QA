from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


try:
    driver = webdriver.Chrome()
    driver.get("https://suninjuly.github.io/cats.html#")
    driver.find_element(By.ID, 'bullet')
    print('найден')
except NoSuchElementException:
    print('не найден')