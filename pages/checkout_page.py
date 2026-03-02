from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage:
    FIRST_NAME   = (By.ID, "first-name")
    LAST_NAME    = (By.ID, "last-name")
    POSTAL_CODE  = (By.ID, "postal-code")
    CONTINUE_BTN = (By.ID, "continue")
    FINISH_BTN   = (By.ID, "finish")
    BACK_HOME    = (By.ID, "back-to-products")
    COMPLETE_MSG = (By.CLASS_NAME, "complete-header")
    ERROR_MSG    = (By.CSS_SELECTOR, "h3[data-test='error']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def fill_information_and_continue(self, first, last, postal):
        self.driver.find_element(*self.FIRST_NAME).send_keys(first)
        self.driver.find_element(*self.LAST_NAME).send_keys(last)
        self.driver.find_element(*self.POSTAL_CODE).send_keys(postal)
        self.driver.find_element(*self.CONTINUE_BTN).click()

    def finish_checkout(self):
        self.wait.until(EC.element_to_be_clickable(self.FINISH_BTN)).click()

    def get_success_message(self):
        msg = self.wait.until(EC.visibility_of_element_located(self.COMPLETE_MSG))
        return msg.text

    def get_error_message(self):
        elem = self.wait.until(EC.visibility_of_element_located(self.ERROR_MSG))
        return elem.text
