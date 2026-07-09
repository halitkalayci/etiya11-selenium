from selenium import webdriver
import pytest
from selenium.webdriver.support.ui import WebDriverWait
import datetime
import os
from pages.login_page import LoginPage
import allure

@pytest.fixture # her teste çalışmadan önce bu fonksiyon çalışacak ve driver objesini test fonksiyonuna gönderecek.
def driver(request):
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    yield driver
    with allure.step("Ekran görüntüsü alınır ve eklenir."):
        allure.attach(driver.get_screenshot_as_png(), name="Ekran Görüntüsü", attachment_type=allure.attachment_type.PNG)
        allure.attach(driver.page_source, name="Sayfa Kaynağı", attachment_type=allure.attachment_type.HTML)
        allure.attach(driver.current_url, name="Mevcut URL", attachment_type=allure.attachment_type.TEXT)
    driver.quit()

@pytest.fixture
def wait(driver):
    wait = WebDriverWait(driver, 20)
    yield wait

@pytest.fixture
def wait_second(driver):
    wait = WebDriverWait(driver, 10)
    yield wait

@pytest.fixture
def authed_driver():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    wait = WebDriverWait(driver, 20)
    login_page = LoginPage(driver, wait)
    login_page.login("standard_user", "secret_sauce")
    yield driver
    with allure.step("Ekran görüntüsü alınır ve eklenir."):
        allure.attach(driver.get_screenshot_as_png(), name="Ekran Görüntüsü", attachment_type=allure.attachment_type.PNG)
        allure.attach(driver.page_source, name="Sayfa Kaynağı", attachment_type=allure.attachment_type.HTML)
        allure.attach(driver.current_url, name="Mevcut URL", attachment_type=allure.attachment_type.TEXT)
    driver.quit()

@pytest.fixture
def authed_driver_wait(authed_driver):
    wait = WebDriverWait(authed_driver, 20)
    yield wait