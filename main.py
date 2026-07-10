# test projesinin dışında the-internet.herokuapp.com sitesindeki istisnai durumların
# örneklendirildiği dosya

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = Chrome()

driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")

wait = WebDriverWait(driver, 10)

start_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='start']/button")))
start_button.click()

# yükleme aksiyonunun tamamlanmasını bekle
loader = wait.until(EC.invisibility_of_element_located((By.ID, "loading")))

finish_div = wait.until(EC.visibility_of_element_located((By.ID, "finish")))
print(finish_div.text)