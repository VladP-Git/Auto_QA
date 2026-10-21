from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time


def test_move():
    driver = webdriver.Chrome()
    driver.get("https://crossbrowsertesting.github.io/hover-menu.html")

    dropdown = driver.find_element(By.LINK_TEXT, "Dropdown")
    actions = ActionChains(driver)
    actions.move_to_element(dropdown).perform()

    secondary_menu = driver.find_element(By. LINK_TEXT, 'Secondary Menu')

    actions.move_to_element(secondary_menu).perform()
    secondery_action = driver.find_element(By. LINK_TEXT, 'Secondary Action')

    assert secondery_action

    secondery_action.click()