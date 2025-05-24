from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

def calc(x, y):
  return str(x+y)
try:
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x = int((browser.find_element(By.ID, "num1")).text)
    y = int((browser.find_element(By.ID, "num2")).text)
    sum = calc(x, y)

    dropdown = Select(browser.find_element(By.ID, "dropdown"))
    dropdown.select_by_value(sum)
    submit = browser.find_element(By.TAG_NAME, "button")
    submit.click()


finally:
    time.sleep(10)
    browser.quit()