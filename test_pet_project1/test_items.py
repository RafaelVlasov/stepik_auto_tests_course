import pytest
from selenium import webdriver
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_find_button_transfer_product_to_basket(browser):
    browser.get(link)
    button = browser.find_elements_by_class_name("btn-add-to-basket")
    assert button, "button missing"
    time.sleep(5)
