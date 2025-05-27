from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try: 
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x = int((browser.find_element(By.CSS_SELECTOR, "[valuex]")).get_attribute('valuex'))

    y = calc(x)
    input = browser.find_element(By.ID, "answer")
    input.send_keys(y)
    rule1 = browser.find_element(By.ID, "robotCheckbox")
    rule1.click()
    rule2 = browser.find_element(By.ID, "robotsRule")
    rule2.click()
    submit = browser.find_element(By.TAG_NAME, "button")
    submit.click()


finally:
    time.sleep(10)
    browser.quit()