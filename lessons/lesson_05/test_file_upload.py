import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_file_upload():

    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/upload")
    time.sleep(4)

    # Получаем путь к файлу test_file.txt,
    # который находится в той же папке, что и этот Python-файл.
    #
    # __file__ — путь к текущему Python-файлу.
    # os.path.abspath(__file__) — получаем абсолютный путь.
    # os.path.dirname(...) — получаем папку с Python-файлом.
    # os.path.join(...) — добавляем к этой папке имя файла.
    file_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "test_file_2.txt"
    )

    file_input = driver.find_element(By.ID, "file-upload")
    file_input.send_keys(file_path)

    upload_button = driver.find_element(By.ID, "file-submit")
    time.sleep(3)
    upload_button.click()

    uploaded_file = driver.find_element(By.ID, "uploaded-files")
    time.sleep(2)
    assert uploaded_file.text == 'test_file_2.txt'