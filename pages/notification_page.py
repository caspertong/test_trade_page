from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class NotificationPage(BasePage):
    #Top right corner bell
    NOTIFICATION_BELL = (By.CSS_SELECTOR, "div[data-testid='notification-selector']")

    #Notification Position
    NOTIFICATION_LIST = (By.CSS_SELECTOR, "div[data-testid='notification-list-result-item-meta']")


    def __init__(self, driver):
        super().__init__(driver)

    def get_latest_notification(self):
        self.click(self.NOTIFICATION_BELL)
        time.sleep(1)
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located(self.NOTIFICATION_LIST))
        raw_text = element.text
        print(f"DEBUG: Raw Notification Text: '{raw_text}'")
        # Expected format: "Open Positions (x)"
        if " | " in raw_text:
            symbol = raw_text.split(' | ')[0]
            symbol = symbol.replace(" ", "")
            order_id = raw_text.split(' | ')[1].split('. ')[1]
            print(f"DEBUG: Parsed Symbol: {symbol}")
            print(f"DEBUG: Parsed Order ID: {order_id}")
            return symbol, int(order_id)
        else:
            print("DEBUG: Could not parse count, returning 0")
            return None, 0