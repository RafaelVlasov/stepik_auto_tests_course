from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

# функция для возврата значения формулы
def num_sum(x, y):
  return int(x) + int(y)

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

# считываем значение х и y
    x_element = browser.find_element_by_id("num1")
    x = x_element.text
    print(x)
    y_element = browser.find_element_by_id("num2")
    y = y_element.text
    print(y)
    
# получаем значение выражения
    result = num_sum(x, y)
    
# ищем значение в выпадающем списке

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_visible_text(str(result))
    
# нажимаем кнопку отправить
    tap_button = browser.find_element_by_css_selector(".btn-default")
    tap_button.click()
    

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
