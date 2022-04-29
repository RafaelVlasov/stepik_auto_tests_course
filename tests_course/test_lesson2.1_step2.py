from selenium import webdriver
import math
import time

# функция для возврата значения формулы
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

# считываем значение х
    x_element = browser.find_element_by_id("treasure")
    x = x_element.get_attribute("valuex")
    print(x)
# считаем значение формулы
    y = calc(x)
# вставляем значение
    input1 = browser.find_element_by_css_selector("#answer")
    input1.send_keys(y)
    tap1 = browser.find_element_by_css_selector("#robotCheckbox")
    tap1.click()
    tap2 = browser.find_element_by_css_selector("#robotsRule")
    tap2.click()
    
    tap3 = browser.find_element_by_css_selector(".btn-default")
    tap3.click()
    

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
