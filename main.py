from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# eski versiyonlarda bu kurulumu manual yapıp yolunu vermem gerekebilir!
driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

sleep(1)
username_input = driver.find_element(By.ID, "user-name")
username_input.send_keys("deneme_selenium")

sleep(10)