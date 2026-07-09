from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage
import allure

@allure.title("Login sayfasında yanlış bilgilerle giriş.")
@allure.description("Login sayfasında yanlış bilgilerle giriş yapıldığında hata mesajının görüntülendiğini doğrular.")
@allure.severity(allure.severity_level.CRITICAL)
@allure.issue("PROJ-12345","Login error bug") # jiraya bağla
@allure.testcase("TC-061") # jiraya bağla
@allure.link("https://youtube.com.tr", "Test Case") # custom link..
def test_invalid_login_shows_error(driver,wait):
    login_page = LoginPage(driver,wait)
    login_page.login("abc","123")
    allure.attach(driver.get_screenshot_as_png(), name="Ekran Görüntüsü", attachment_type=allure.attachment_type.PNG)
    assert login_page.get_error_text() == "Epic sadface: Username and password do not match any user in this service"


@allure.title("Geçerli giriş bilgileriyle giriş yapma.")
@allure.description("Geçerli giriş bilgileriyle giriş yapıldığında kullanıcıların ana sayfasına yönlendirildiğini doğrular.")
@allure.severity(allure.severity_level.BLOCKER)
def test_valid_login(driver, wait):
    allure.step("Login sayfası açılır.")
    login_page = LoginPage(driver,wait)
    allure.step("Geçerli kullanıcı adı ve şifre ile giriş yapılır.")
    login_page.login("standard_user","secret_sauce")
    allure.step("Ekran görüntüsü alınır ve eklenir.")
    allure.attach(driver.get_screenshot_as_png(), name="Ekran Görüntüsü", attachment_type=allure.attachment_type.PNG)
    allure.attach(driver.page_source, name="Sayfa Kaynağı", attachment_type=allure.attachment_type.HTML)
    allure.attach(driver.current_url, name="Mevcut URL", attachment_type=allure.attachment_type.TEXT)
    assert driver.current_url == "https://www.saucedemo.com/inventory.html"

def test_username_required(driver,wait):
    login_page = LoginPage(driver,wait)
    login_page.login("","abc123")
    assert login_page.get_error_text() == "Epic sadface: Username is required"