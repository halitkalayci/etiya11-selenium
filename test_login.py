from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


def test_invalid_login_shows_error():
    # 3A Principle
    # Arrange -> Hazırlık aşaması (driver, url, input)
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    wait = WebDriverWait(driver, 10)
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