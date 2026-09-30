from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://example.com")

# Открываем новую вкладку
driver.execute_script("window.open('https://google.com', '_blank');")

tabs = driver.window_handles

# Выводим список всех вкладок
# print(driver.window_handles)

print(driver.current_window_handle)

driver.switch_to.window(tabs[1])
print(driver.current_window_handle)

driver.switch_to.window(tabs[0])
print(driver.current_window_handle)