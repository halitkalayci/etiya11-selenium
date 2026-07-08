from selenium import webdriver
import pytest
from selenium.webdriver.support.ui import WebDriverWait
import datetime
import os

@pytest.fixture # her teste çalışmadan önce bu fonksiyon çalışacak ve driver objesini test fonksiyonuna gönderecek.
def driver(request):
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()

@pytest.fixture
def wait(driver):
    wait = WebDriverWait(driver, 20)
    yield wait

@pytest.fixture
def wait_second(driver):
    wait = WebDriverWait(driver, 10)
    yield wait