from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InventoryPage:
    INVENTORY_ITEM = (By.CLASS_NAME, "inventory_item")
    CART_BADGE     = (By.CLASS_NAME, "shopping_cart_badge")
    CART_LINK      = (By.CLASS_NAME, "shopping_cart_link")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def add_first_n_items_to_cart(self, n=2):
        items = self.wait.until(EC.visibility_of_all_elements_located(self.INVENTORY_ITEM))
        for item in items[:n]:
            add_button = item.find_element(By.TAG_NAME, "button")
            add_button.click()

    def get_cart_count(self):
        badge = self.wait.until(EC.visibility_of_element_located(self.CART_BADGE))
        return int(badge.text)

    def open_cart(self):
        self.driver.find_element(*self.CART_LINK).click()
