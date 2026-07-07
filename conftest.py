from selenium import webdriver
import pytest
from selenium.webdriver.support.ui import WebDriverWait
import random

@pytest.fixture # her teste çalışmadan önce bu fonksiyon çalışacak ve driver objesini test fonksiyonuna gönderecek.
def driver():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    # yield => testi çalıştır
    yield driver # return => fonksiyonu bitir ve döndür.
    rnd = random.randint(1,1000)
    driver.save_screenshot(filename=f"screenshot_{rnd}.png")
    driver.quit()
    # yield => döndür ama bitirme, devamı gelecek.

@pytest.fixture
def wait(driver):
    wait = WebDriverWait(driver, 20)
    yield wait

@pytest.fixture
def wait_second(driver):
    wait = WebDriverWait(driver, 10)
    yield wait