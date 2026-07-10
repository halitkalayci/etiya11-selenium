# test projesinin dışında the-internet.herokuapp.com sitesindeki istisnai durumların
# örneklendirildiği dosya

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
driver = Chrome()

# driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")

wait = WebDriverWait(driver, 10)

# start_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='start']/button")))
# start_button.click()

# # yükleme aksiyonunun tamamlanmasını bekle
# loader = wait.until(EC.invisibility_of_element_located((By.ID, "loading")))

# finish_div = wait.until(EC.visibility_of_element_located((By.ID, "finish")))
# print(finish_div.text)

# driver.get("https://the-internet.herokuapp.com/javascript_alerts")

# js_alert_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='content']/div/ul/li[1]/button")))

# js_alert_btn.click()

# alert = wait.until(EC.alert_is_present())
# sleep(1)
# alert.accept()

# js_confirm_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='content']/div/ul/li[2]/button")))
# js_confirm_btn.click()

# confirm = wait.until(EC.alert_is_present())
# sleep(1)
# confirm.dismiss()


# js_prompt_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='content']/div/ul/li[3]/button")))
# js_prompt_btn.click()

# prompt = wait.until(EC.alert_is_present())
# sleep(1)
# prompt.send_keys("deneme")
# sleep(1)
# prompt.accept()




# driver.get("https://the-internet.herokuapp.com/windows")


# link = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='content']/div/a")))
# link.click()
# # sekmeler arası gezmek istiyorsan switch_to.window(SEKME)
# driver.switch_to.window(driver.window_handles[1])
# h3 = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/h3")))
# print(h3.text)


# driver.get("https://the-internet.herokuapp.com/iframe")

# # ilgili frame'i bul ve geçiş yap
# wait.until(EC.frame_to_be_available_and_switch_to_it((By.ID, "mce_0_ifr")))

# content = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='tinymce']/p")))
# print(content.text)

# driver.switch_to.default_content() # varsayılan dom'a dön
# title = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='content']/div/h3")))
# print(title.text)

driver.get("https://the-internet.herokuapp.com/infinite_scroll")
sleep(1)
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sleep(1)