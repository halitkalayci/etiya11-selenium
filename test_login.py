from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import pytest


# POM => Page Object Model

# Dün yazdığımız testleri pytest'E geçirelim. conftest ve decoratorler kullanmaya özen gösterelim.

@pytest.mark.parametrize("username,password,expected_error", [ 
    ("abc","123","Epic sadface: Username and password do not match any user in this service") , 
    ("","","Epic sadface: Username is required") , 
    ("deneme","","Epic sadface: Password is required") ])
def test_invalid_login_shows_error(driver,wait,username,password,expected_error):
    username_input = wait.until(EC.visibility_of_element_located((By.ID, "user-name")))
    password_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='password']")))
    login_btn = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='login-button']")))
    username_input.send_keys(username)
    password_input.send_keys(password)
    login_btn.click()
    error_message = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='error']")))
    assert error_message.text == expected_error

def test_valid_login(driver,wait):
    username_input = wait.until(EC.visibility_of_element_located((By.ID, "user-name")))
    password_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='password']")))
    login_btn = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='login-button']")))
    username_input.send_keys("standard_user")
    password_input.send_keys("secret_sauce")
    login_btn.click()
    assert driver.current_url == "https://www.saucedemo.com/inventory.html"