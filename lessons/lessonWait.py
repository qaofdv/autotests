import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
browser = webdriver.Chrome()
try:
    browser.get("https://suninjuly.github.io/explicit_wait2.html")
    price = WebDriverWait(browser, 12).until(
            EC.text_to_be_present_in_element((By.ID, "price"), '$100')
        )
    book = browser.find_element(By.ID, "book")
    book.click()
    x = int(browser.find_element(By.ID, "input_value").text)
    text = browser.find_element(By.ID, "answer")
    text.send_keys(calc(x))
    button1 = browser.find_element(By.ID, "solve")
    button1.click()
finally:
    time.sleep(10)
    browser.quit()

