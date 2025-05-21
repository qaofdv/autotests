from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    link = "https://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input = browser.find_element(By.CSS_SELECTOR, "[name='firstname']")
    input.send_keys('testName')
    input = browser.find_element(By.CSS_SELECTOR, "[name='lastname']")
    input.send_keys('testLastname')
    input = browser.find_element(By.CSS_SELECTOR, "[name='email']")
    input.send_keys('testEmail')
    upload = browser.find_element(By.ID, "file")
    currentFolder = os.path.dirname(__file__)
    projectFolder = os.path.abspath(os.path.join(currentFolder, ".."))
    filePath = os.path.join(projectFolder, "testData", "testFile.txt")
    upload.send_keys(filePath)
    submit = browser.find_element(By.TAG_NAME, "button")
    submit.click()


finally:
    time.sleep(10)
    browser.quit()
