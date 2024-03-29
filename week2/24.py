from selenium import webdriver
import time
import math
import os

link = 'http://suninjuly.github.io/file_input.html'
try:
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(1)

    input1 = browser.find_element_by_name('firstname')
    input1.send_keys("Ivan")

    input2 = browser.find_element_by_css_selector('input[name="lastname"]')
    input2.send_keys("Petrov")

    input3 = browser.find_element_by_css_selector('input[name="email"]')
    input3.send_keys("test@math.ru")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, '1.6.txt')
    input4 = browser.find_element_by_id('file')
    input4.send_keys(file_path)

    button = browser.find_element_by_css_selector('button.btn')
    button.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла