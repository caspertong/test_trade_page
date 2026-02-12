from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import time

class ProductSelectPage(BasePage):
    #Product Title
    PRODUCT_TITLE = (By.CSS_SELECTOR, "//div[@class='MuiTypography-root MuiTypography-h3 MuiTypography-gutterBottom mui-style-1akb2ty']")
    BACK_BUTTON = (By.XPATH, "//button[@aria-label='Back']")

    #Product Input
    SIZE_36_40 = (By.XPATH, "//div[text()='36-40']")
    SIZE_7_9 = (By.XPATH, "//div[text()='7-9Y']")

    #Price
    ORIGINAL_PRICE = (By.CSS_SELECTOR, "span[class='ProductPagePrice-discountPrice MuiBox-root mui-style-1reirs0']")
    DISCOUNT_PRICE = (By.CSS_SELECTOR, "span[class='ProductPagePrice-finalPrice MuiBox-root mui-style-1xdhyk6']")

    #Add to Cart
    ADD_TO_CART_BUTTON = (By.XPATH, "//button[text()='Add to Cart']")
    POP_OUT_CLOSE = (By.XPATH, "//button[@aria-label='Close']")
    VIEW_SHOPPING_CART = (By.CSS_SELECTOR, "a[id='view-shopping-cart-button']")


    def __init__(self, driver):
        super().__init__(driver)

    def is_loaded(self):
        return self.is_visible(self.PRODUCT_TITLE)

    def select_size_36_40(self):
        self.wait_for_element_visible(self.SIZE_36_40, 5)
        time.sleep(1)
        self.click(self.SIZE_36_40)

    def select_size_7_9(self):
        self.wait_for_element_visible(self.SIZE_7_9, 5)
        time.sleep(1)
        self.click(self.SIZE_7_9)

    def get_original_price(self):
        return self.get_text(self.ORIGINAL_PRICE)

    def get_discount_price(self):
        return self.get_text(self.DISCOUNT_PRICE)
    
    def click_add_to_cart(self):
        self.click(self.ADD_TO_CART_BUTTON)

    def click_pop_out_close(self):
        self.click(self.POP_OUT_CLOSE)

    def click_back_button(self):
        self.click(self.BACK_BUTTON)
    
    def click_view_shopping_cart(self):
        self.wait_for_element_visible(self.VIEW_SHOPPING_CART, 5)
        self.click(self.VIEW_SHOPPING_CART)