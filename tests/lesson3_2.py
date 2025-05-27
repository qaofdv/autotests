import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_reg1(browser):
    link = "http://suninjuly.github.io/registration1.html"
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your first name']").send_keys("Ivan")
    browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your last name']").send_keys("Petrov")
    browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your email']").send_keys("test@test.com")
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()
    time.sleep(1)
    welcome_text = browser.find_element(By.TAG_NAME, "h1").text
    assert welcome_text == "Congratulations! You have successfully registered!", "Registration failed"

def test_reg2(browser):
    link = "http://suninjuly.github.io/registration2.html"
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your first name']").send_keys("Ivan")
    browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your last name']").send_keys("Petrov")
    browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your email']").send_keys("test@test.com")
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()
    time.sleep(1)
    welcome_text = browser.find_element(By.TAG_NAME, "h1").text
    assert welcome_text == "Congratulations! You have successfully registered!", "Registration failed"
