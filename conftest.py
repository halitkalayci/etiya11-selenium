from selenium import webdriver
import pytest
from selenium.webdriver.support.ui import WebDriverWait
import datetime
import os

@pytest.fixture # her teste çalışmadan önce bu fonksiyon çalışacak ve driver objesini test fonksiyonuna gönderecek.
def driver(request):
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    # yield => testi çalıştır
    yield driver # return => fonksiyonu bitir ve döndür.
    #TODO: Geliştir.
    folder_name = f"screenshots-{datetime.datetime.now().strftime('%Y-%m-%d %H')}"
    if os.path.exists(folder_name) == False:
        os.mkdir(folder_name)
    driver.save_screenshot(filename=f"{folder_name}/screenshot_{request.node.name}.png")
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