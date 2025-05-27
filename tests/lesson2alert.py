from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try:
    link = "https://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()
    confirm = browser.switch_to.alert
    confirm.accept()

    x = int(browser.find_element(By.ID, "input_value").text)
    text = browser.find_element(By.ID, "answer")
    text.send_keys(calc(x))
    button1 = browser.find_element(By.TAG_NAME, "button")
    button1.click()

finally:
    time.sleep(10)
    browser.quit()