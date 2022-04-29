from selenium import webdriver
import math
import time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)


    button1 = browser.find_element_by_class_name("btn-primary")
    button1.click()
    alert = browser.switch_to.alert
    alert.accept()

# получаем значения х
    elem_x = browser.find_element_by_id("input_value")
    result = calc(elem_x.text)

# вводим значения х
    answer = browser.find_element_by_id("answer")
    answer.send_keys(result)
    
    button2 = browser.find_element_by_class_name("btn-primary")
    button2.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
