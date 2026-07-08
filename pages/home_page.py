from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


class Homepage():
    INVENTORY_LIST = (By.CSS_SELECTOR, "[data-test='inventory-list']")
    INVENTORY_ITEM = (By.CSS_SELECTOR, "[data-test='inventory-item']")
    
    def __init__(self, driver: webdriver.Chrome, wait: WebDriverWait):
        self.driver = driver
        self.wait = wait
    
    def get_count_of_items(self):
        inv_list = self.wait.until(EC.visibility_of_element_located(self.INVENTORY_LIST))
        inv_items = inv_list.find_elements(*self.INVENTORY_ITEM)
        return len(inv_items)