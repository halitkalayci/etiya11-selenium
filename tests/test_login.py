from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage


def test_invalid_login_shows_error(driver,wait):
    login_page = LoginPage(driver,wait)
    login_page.login("abc","123")
    assert login_page.get_error_text() == "Epic sadface: Username and password do not match any user in this service"

def test_valid_login(driver, wait):
    login_page = LoginPage(driver,wait)
    login_page.login("standard_user","secret_sauce")
    assert driver.current_url == "https://www.saucedemo.com/inventory.html"

def test_username_required(driver,wait):
    login_page = LoginPage(driver,wait)
    login_page.login("","abc123")
    assert login_page.get_error_text() == "Epic sadface: Username is required"