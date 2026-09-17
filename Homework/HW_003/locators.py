# locators.py
from selenium.webdriver.common.by import By

# Кнопка куки
COOKIE_ACCEPT_BTN = (By.XPATH, "//button[contains(text(), 'Accept') or contains(text(), 'Принять') or contains(@class, 'accept')]")

# Универсальные локаторы (ищут по href-атрибутам, тексту и частичным совпадениям)
LOGO = (By.XPATH, "//a[contains(@href, 'itcareerhub') or contains(@class, 'logo')]//img | //img[contains(@alt, 'Hub') or contains(@src, 'logo')]")
LINK_PROGRAMS = (By.XPATH, "//a[contains(@href, 'weiterbildung') or contains(@href, 'programs') or contains(., 'Программ')]")
LINK_PAYMENT = (By.XPATH, "//a[contains(@href, 'schulgebuhren') or contains(@href, 'payment') or contains(., 'Способ')]")
LINK_ABOUT = (By.XPATH, "//a[contains(@href, 'o-nas') or contains(@href, 'about') or contains(., 'О нас')]")
LINK_CONTACTS = (By.XPATH, "//a[contains(@href, 'contact') or contains(@href, 'kontakt') or contains(., 'Контакт')]")
LINK_REVIEWS = (By.XPATH, "//a[contains(@href, 'reviews') or contains(@href, 'bewertungen') or contains(., 'Отзыв')]")
LINK_BLOG = (By.XPATH, "//a[contains(@href, 'blog') or contains(., 'Блог')]")

# Языковые кнопки (ищем по тексту "ru" и "de" внутри ссылок/блоков переключения)
LANG_RU = (By.XPATH, "//a[text()='ru' or contains(@href, '/ru') or contains(., 'ru')]")
LANG_DE = (By.XPATH, "//a[text()='de' or contains(@href, '/de') or contains(., 'de')]")

# Кнопка отправки заявки (или обратного звонка)
BTN_CALLBACK = (By.XPATH, "//button[contains(., 'ЗАЯВКУ') or contains(., 'звонок') or contains(., 'консультацию')] | //a[contains(., 'КОНСУЛЬТАЦИЮ') or contains(., 'ЗАЯВКУ')]")
# Текст внутри всплывающей формы / блока заявки
POPUP_TEXT = (By.XPATH, "//*[contains(text(), 'Запишитесь') or contains(text(), 'Оставьте заявку') or contains(text(), 'консультацию')]")
