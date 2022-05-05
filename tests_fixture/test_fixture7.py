import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

list_links = ["https://stepik.org/lesson/236895/step/1", "https://stepik.org/lesson/236896/step/1", "https://stepik.org/lesson/236897/step/1", "https://stepik.org/lesson/236898/step/1", "https://stepik.org/lesson/236899/step/1", "https://stepik.org/lesson/236903/step/1", "https://stepik.org/lesson/236904/step/1", "https://stepik.org/lesson/236905/step/1"]

text = ""

@pytest.mark.parametrize('links', list_links)
def test_verification_text_after_correct_answer(browser, links):
    link = f"{links}"
    browser.get(link)
    browser.implicitly_wait(5)
    textarea = browser.find_element_by_tag_name("textarea")
    textarea.send_keys(str(math.log(int(time.time()))))
    button = WebDriverWait(browser, 3).until(EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission")))
    button.click()
    message = WebDriverWait(browser, 3).until(EC.visibility_of_element_located((By.CLASS_NAME, "smart-hints__hint"))).text
    assert message == "Correct!", f"{message}"

        
