from selenium.webdriver.common.by import By

# Поле ввода задержки
DELAY_INPUT = (By.CSS_SELECTOR, "#delay")

# Кнопки калькулятора (поиск по тексту на кнопках-спанах)
BTN_7 = (By.XPATH, "//span[text()='7']")
BTN_PLUS = (By.XPATH, "//span[text()='+']")
BTN_8 = (By.XPATH, "//span[text()='8']")
BTN_EQUAL = (By.XPATH, "//span[text()='=']")

# Экран калькулятора, где отображается результат
CALC_SCREEN = (By.CLASS_NAME, "screen")
