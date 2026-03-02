from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:
    CART_ITEM     = (By.CLASS_NAME, "cart_item")
    CHECKOUT_BTN  = (By.ID, "checkout")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def get_cart_items_names(self):
        items = self.wait.until(EC.visibility_of_all_elements_located(self.CART_ITEM))
        names = []
        for item in items:
            name = item.find_element(By.CLASS_NAME, "inventory_item_name").text
            names.append(name)
        return names

    def remove_item_by_name(self, product_name):
        items = self.wait.until(EC.visibility_of_all_elements_located(self.CART_ITEM))
        for item in items:
            name = item.find_element(By.CLASS_NAME, "inventory_item_name").text
            if name == product_name:
                item.find_element(By.TAG_NAME, "button").click()
                return

    def get_items_count(self):
        items = self.driver.find_elements(*self.CART_ITEM)
        return len(items)

    def click_checkout(self):
        self.driver.find_element(*self.CHECKOUT_BTN).click()
