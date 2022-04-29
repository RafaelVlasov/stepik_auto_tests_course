from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    button = browser.find_element_by_class_name("btn-primary")
    button.click()
    
    browser.execute_script("window.scrollBy(0, 100);")

# получаем значения х
    elem_x = browser.find_element_by_id("input_value")
    result = calc(elem_x.text)

# вводим значения х
    answer = browser.find_element_by_id("answer")
    answer.send_keys(result)

    button2 = browser.find_element_by_id("solve")
    button2.click()
    time.sleep(5)
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
