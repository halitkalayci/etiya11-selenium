from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

# eski versiyonlarda bu kurulumu manual yapıp yolunu vermem gerekebilir!
driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

# maksimum 10 saniye bu driveri bekletecek arkadaş.
wait = WebDriverWait(driver, 10)

#username_input = driver.find_element(By.ID, "user-name")
# ilgili EC durum sağlanana kadar (maksimum 10sn bekler.)
username_input = wait.until(EC.visibility_of_element_located((By.ID, "user-name")))
username_input.send_keys("deneme_selenium")

password_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='password']")))
password_input.send_keys("yanlişşifre123")

login_btn = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='login-button']")))
login_btn.click()

error_message = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='error']")))
print(error_message.text == "Epic sadface: Username and password do not match any user in this service")

driver.save_screenshot("1.png")
sleep(10)