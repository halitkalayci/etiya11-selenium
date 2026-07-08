from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

class LoginPage():
    # Bileşenler
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.CSS_SELECTOR,  "[data-test='password']")
    LOGIN_BTN = (By.CSS_SELECTOR,  "[data-test='login-button']")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")
    #

    def __init__(self, driver:webdriver.Chrome, wait:WebDriverWait):
        self.driver = driver
        self.wait = wait

    def send_username(self, username):
        self.wait.until(EC.visibility_of_element_located(self.USERNAME_INPUT)).send_keys(username)

    def send_password(self, password):
        self.wait.until(EC.visibility_of_element_located(self.PASSWORD_INPUT)).send_keys(password)

    def click_login_button(self):
        self.wait.until(EC.visibility_of_element_located(self.LOGIN_BTN)).click()
        
    def login(self, username, password):
        self.send_username(username)
        self.send_password(password)
        self.click_login_button()

    def get_error_text(self):
        text = self.wait.until(EC.visibility_of_element_located(self.ERROR_MESSAGE)).text
        return text