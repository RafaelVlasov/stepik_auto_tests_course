from selenium import webdriver
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

# вставляем значения
    input1 = browser.find_element_by_name("firstname")
    input1.send_keys("Rafael")
    input2 = browser.find_element_by_name("lastname")
    input2.send_keys("Rafael")
    input3 = browser.find_element_by_name("email")
    input3.send_keys("Rafael")
    
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'text.txt')           # добавляем к этому пути имя файла
    
    tap1 = browser.find_element_by_id("file")
    tap1.send_keys(file_path)
    
    tap2 = browser.find_element_by_class_name("btn-primary")
    tap2.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
