from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys

class LoginPage(BasePage):
    # Locators
    ACCOUNT_ICON = (By.CSS_SELECTOR, "a[id='account']")
    ACCOUNT_EMAIL_INPUT = (By.CSS_SELECTOR, "input[type='email']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[id='current-password']")
    SIGNIN_BUTTON = (By.XPATH, "//button[@type='submit']")

    
    URL = "https://graphcommerce.vercel.app/"

    def __init__(self, driver):
        super().__init__(driver)

    def navigate(self):
        self.open_url(self.URL)

    def click_account_icon(self):
        self.click(self.ACCOUNT_ICON)

    def enter_account_email(self, account_email):
        self.send_keys(self.ACCOUNT_EMAIL_INPUT, account_email)

    def enter_password(self, password):
        self.send_keys(self.PASSWORD_INPUT, password + Keys.RETURN)

    def click_signin(self):
        self.click(self.SIGNIN_BUTTON)
    
    def is_signin_button_enabled(self):
        return self.is_enabled(self.SIGNIN_BUTTON)
