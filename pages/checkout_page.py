from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import time

class CheckoutPage(BasePage):
    #Title
    TITLE = (By.XPATH, "//span[text()='Total ']")
    CLOSE_BUTTON = (By.XPATH, "//button[@class='MuiButtonBase-root MuiFab-root MuiFab-circular MuiFab-sizeResponsive MuiFab-default MuiFab-root MuiFab-circular MuiFab-sizeResponsive MuiFab-default LayoutHeaderClose-root mui-style-i069pz']//*[name()='svg']")

    #Product
    PRODUCT1_NAME = (By.XPATH, "//a[contains(text(), 'Anna Socks')]")
    PRODUCT2_NAME = (By.XPATH, "//a[contains(text(), 'Tamara Socks')]")

    PRODUCT1_SIZE = (By.XPATH, "//div[text()='Size 36 to 40']")
    PRODUCT2_SIZE = (By.XPATH, "//div[text()='7 to 9 years']")
    
    PRODUCT1_PRICE = (By.XPATH, "//div[@class='ActionCardLayout-root layoutList MuiBox-root mui-style-195fhik']//div[1]//div[1]//div[2]//div[2]//span[1]")
    PRODUCT2_PRICE = (By.XPATH, "//div[@class='MuiContainer-root MuiContainer-maxWidthMd mui-style-1y2k7wu']//div[2]//div[1]//div[2]//div[2]//span[1]")

    PRODUCT_REMOVE = (By.XPATH, "//button[text()='Remove']")

    CHECKOUT_BUTTON = (By.XPATH, "//span[@class='CartStartCheckout-checkoutButtonTotal MuiBox-root mui-style-ecuirf']")

    def __init__(self, driver):
        super().__init__(driver)

    def is_loaded(self):
        return self.is_visible(self.TITLE)

    def get_product1_name(self):
        return self.get_text(self.PRODUCT1_NAME)

    def get_product2_name(self):
        return self.get_text(self.PRODUCT2_NAME)

    def get_product1_size(self):
        return self.get_text(self.PRODUCT1_SIZE)

    def get_product2_size(self):
        return self.get_text(self.PRODUCT2_SIZE)

    def get_product1_price(self):
        return self.get_text(self.PRODUCT1_PRICE)

    def get_product2_price(self):
        return self.get_text(self.PRODUCT2_PRICE)

    def clear_all_existing_products(self):
        while len(self.driver.find_elements(By.XPATH, "//button[text()='Remove']")) > 0:
            self.click(self.PRODUCT_REMOVE)
            time.sleep(2)

    def click_close_button(self):
        self.click(self.CLOSE_BUTTON)

    def click_checkout_button(self):
        self.click(self.CHECKOUT_BUTTON)
