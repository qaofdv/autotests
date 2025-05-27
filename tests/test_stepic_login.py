import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

@pytest.mark.parametrize('url', ["236895", "236896", "236897","236898","236899","236903","236904","236905"])
class TestLogin:
    def test_creds_login (self, browser, url):
        timeout = 30
        link = f"https://stepik.org/lesson/{url}/step/1"
        browser.get(link)
        WebDriverWait(browser, timeout).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "navbar__auth_login"))
            )
        login_button = browser.find_element(By.CLASS_NAME, "navbar__auth_login")
        login_button.click()
        WebDriverWait(browser, timeout).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "modal-dialog-inner"))
        )
        email = browser.find_element(By.ID, 'id_login_email')
        email.send_keys("lalala") #add email
        password = browser.find_element(By.ID, 'id_login_password')
        password.send_keys("lalala") #add password
        submit_button = browser.find_element(By.CLASS_NAME, "sign-form__btn")
        submit_button.click()
        WebDriverWait(browser, timeout).until(
            EC.invisibility_of_element((By.CLASS_NAME, "modal-dialog-inner"))
        )
        WebDriverWait(browser, timeout).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "ember-text-area"))
        )

        try:
            WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".again-btn.white")))
            solve_button = browser.find_element(By.CSS_SELECTOR, ".again-btn.white")
            solve_button.click()
            ok_button = browser.find_element(By.XPATH, "//footer/button[1]")
            ok_button.click()
        except:
            pass

        answerInput = WebDriverWait(browser, timeout).until(
            EC.element_to_be_clickable((By.CLASS_NAME, 'ember-text-area'))
        )
        answer = str(math.log(int(time.time())))
        answerInput.send_keys(answer)
        send_button = browser.find_element(By.CLASS_NAME, "submit-submission")
        send_button.click()
        WebDriverWait(browser, timeout).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "smart-hints__hint"))
        )
        feedbackText = browser.find_element(By.CLASS_NAME, "smart-hints__hint")
        assert feedbackText.text == "Correct!"