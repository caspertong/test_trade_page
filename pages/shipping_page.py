from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
import time

class ShippingPage(BasePage):
    #Title
    TITLE = (By.XPATH, "//h1[text()='Shipping']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Next']")

    #Personal Details
    STREET = (By.XPATH, "//input[@name='street']")
    HOUSE_NUMBER = (By.XPATH, "//input[@name='houseNumber']")
    POST_CODE = (By.XPATH, "//input[@name='postcode']")
    CITY = (By.XPATH, "//input[@name='city']")
    REGION_DROPDOWN = (By.XPATH, "//div[@name='regionId']")
    REGION_DROPDOWN_SELECT = (By.XPATH, "//li[text()='Alaska']")

    #Shipping Method
    FIRST_SHIPPING_METHOD = (By.XPATH, "//div[text()='Best Way Table Rate']")
    
    def __init__(self, driver):
        super().__init__(driver)

    def is_loaded(self):
        return self.is_visible(self.TITLE)

    def enter_street(self, street):
        self.send_keys(self.STREET, street)

    def enter_house_number(self, house_number):
        self.send_keys(self.HOUSE_NUMBER, house_number)

    def enter_post_code(self, post_code):
        self.send_keys(self.POST_CODE, post_code)

    def enter_city(self, city):
        self.send_keys(self.CITY, city)

    def select_region(self):
        self.click(self.REGION_DROPDOWN)
        time.sleep(1)
        self.click(self.REGION_DROPDOWN_SELECT)

    def click_first_shipping_method(self):
        self.click(self.FIRST_SHIPPING_METHOD)

    def click_next(self):
        self.click(self.NEXT_BUTTON)
        