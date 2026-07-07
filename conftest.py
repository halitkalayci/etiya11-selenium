from selenium import webdriver
import pytest
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture # her teste çalışmadan önce bu fonksiyon çalışacak ve driver objesini test fonksiyonuna gönderecek.
def driver():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    yield driver

@pytest.fixture
def wait(driver):
    wait = WebDriverWait(driver, 20)
    yield wait