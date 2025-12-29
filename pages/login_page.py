from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    # Locators
    ACCOUNT_INPUT = (By.CSS_SELECTOR, 'input[data-testid="login-user-id"]')
    PASSWORD_INPUT = (By.CSS_SELECTOR, 'input[data-testid="login-password"]')
    LOGIN_BUTTON = (By.CSS_SELECTOR, 'button[data-testid="login-submit"]')
    
    URL = "https://aqxtrader.aquariux.com/web/login"

    def __init__(self, driver):
        super().__init__(driver)

    def navigate(self):
        self.open_url(self.URL)

    def enter_account_id(self, account_id):
        self.send_keys(self.ACCOUNT_INPUT, account_id)

    def enter_password(self, password):
        self.send_keys(self.PASSWORD_INPUT, password)

    def click_login(self):
        self.click(self.LOGIN_BUTTON)
    
    def is_login_button_enabled(self):
        return self.is_enabled(self.LOGIN_BUTTON)
