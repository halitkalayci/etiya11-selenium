from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

def test_invalid_login_shows_error(driver,wait):
    username_input = wait.until(EC.visibility_of_element_located((By.ID, "user-name")))
    password_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='password']")))
    login_btn = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='login-button']")))

    # Act -> Aksiyon aşaması (logine tıkla, inputa yaz)
    username_input.send_keys("deneme_selenium")
    password_input.send_keys("invalid_password")
    login_btn.click()
    error_message = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='error']")))
    # Assert -> Doğrulama aşaması (assert error message == şu)
    # testin tüm sonucu assertin yanına verdiğim koşula bağlı.
    assert error_message.text == "Epic sadface: Username and password do not match any user in this service"

def test_valid_login(driver,wait):
    username_input = wait.until(EC.visibility_of_element_located((By.ID, "user-name")))
    password_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='password']")))
    login_btn = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='login-button']")))
    username_input.send_keys("standard_user")
    password_input.send_keys("secret_sauce")
    login_btn.click()
    assert driver.current_url == "https://www.saucedemo.com/inventory.html"