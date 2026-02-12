from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
import time

class PaymentPage(BasePage):
    #Title
    TITLE = (By.XPATH, "//h1[text()='Payment']")

    #Shipping Info
    SHIPPING_USERNAME = (By.XPATH, "//body/div[@id='__next']/div/div[@class='LayoutDefault-root MuiBox-root mui-style-1tq8rhe']/div[@class='LayoutDefault-children']/div[@class='MuiContainer-root MuiContainer-maxWidthMd mui-style-1y2k7wu']/div[@class='CartSummary-root MuiBox-root mui-style-8n4yc2']/div[@class='CartSummary-detailsContainer MuiBox-root mui-style-15yrt0a']/div[@class='MuiBox-root mui-style-0']/div[@class='MuiTypography-root MuiTypography-body1 AddressMultiLine-root mui-style-15dc6y5']/div[@class='AddressMultiLine-title']/div[2]")
    SHIPPING_STREET_HOUSENUMBER = (By.XPATH, "//body/div[@id='__next']/div/div[@class='LayoutDefault-root MuiBox-root mui-style-1tq8rhe']/div[@class='LayoutDefault-children']/div[@class='MuiContainer-root MuiContainer-maxWidthMd mui-style-1y2k7wu']/div[@class='CartSummary-root MuiBox-root mui-style-8n4yc2']/div[@class='CartSummary-detailsContainer MuiBox-root mui-style-15yrt0a']/div[@class='MuiBox-root mui-style-0']/div[@class='MuiTypography-root MuiTypography-body1 AddressMultiLine-root mui-style-15dc6y5']/div[2]") 
    SHIPPING_POST_CODE_CITY = (By.XPATH, "//body/div[@id='__next']/div/div[@class='LayoutDefault-root MuiBox-root mui-style-1tq8rhe']/div[@class='LayoutDefault-children']/div[@class='MuiContainer-root MuiContainer-maxWidthMd mui-style-1y2k7wu']/div[@class='CartSummary-root MuiBox-root mui-style-8n4yc2']/div[@class='CartSummary-detailsContainer MuiBox-root mui-style-15yrt0a']/div[@class='MuiBox-root mui-style-0']/div[@class='MuiTypography-root MuiTypography-body1 AddressMultiLine-root mui-style-15dc6y5']/div[3]")
    SHIPPING_REGION_COUNTRY = (By.XPATH, "//body/div[@id='__next']/div/div[@class='LayoutDefault-root MuiBox-root mui-style-1tq8rhe']/div[@class='LayoutDefault-children']/div[@class='MuiContainer-root MuiContainer-maxWidthMd mui-style-1y2k7wu']/div[@class='CartSummary-root MuiBox-root mui-style-8n4yc2']/div[@class='CartSummary-detailsContainer MuiBox-root mui-style-15yrt0a']/div[@class='MuiBox-root mui-style-0']/div[@class='MuiTypography-root MuiTypography-body1 AddressMultiLine-root mui-style-15dc6y5']/div[4]")

    #Billing Info
    BILLING_USERNAME = (By.XPATH, "//div[@class='SectionContainer-root MuiBox-root mui-style-1chhb0k']//div[@class='AddressMultiLine-title']//div[2]")
    BILLING_STREET_HOUSENUMBER = (By.XPATH, "//body/div[@id='__next']/div/div[@class='LayoutDefault-root MuiBox-root mui-style-1tq8rhe']/div[@class='LayoutDefault-children']/div[@class='MuiContainer-root MuiContainer-maxWidthMd mui-style-1y2k7wu']/div[@class='CartSummary-root MuiBox-root mui-style-8n4yc2']/div[@class='CartSummary-detailsContainer MuiBox-root mui-style-15yrt0a']/div[@class='MuiBox-root mui-style-0']/div[@class='SectionContainer-root MuiBox-root mui-style-1chhb0k']/div[@class='MuiTypography-root MuiTypography-body1 AddressMultiLine-root mui-style-15dc6y5']/div[2]")
    BILLING_POST_CODE_CITY = (By.XPATH, "//div[@class='SectionContainer-root MuiBox-root mui-style-1chhb0k']//div[3]")
    BILLING_REGION_COUNTRY = (By.XPATH, "//div[@class='SectionContainer-root MuiBox-root mui-style-1chhb0k']//div[4]")

    def __init__(self, driver):
        super().__init__(driver)

    def is_loaded(self):
        return self.is_visible(self.TITLE)

    def get_shipping_username(self):
        return self.get_text(self.SHIPPING_USERNAME)

    def get_shipping_street_housenumber(self):
        return self.get_text(self.SHIPPING_STREET_HOUSENUMBER)

    def get_shipping_post_code_city(self):
        return self.get_text(self.SHIPPING_POST_CODE_CITY)

    def get_shipping_region_country(self):
        return self.get_text(self.SHIPPING_REGION_COUNTRY)

    def get_billing_username(self):
        return self.get_text(self.BILLING_USERNAME)

    def get_billing_street_housenumber(self):
        return self.get_text(self.BILLING_STREET_HOUSENUMBER)

    def get_billing_post_code_city(self):
        return self.get_text(self.BILLING_POST_CODE_CITY)

    def get_billing_region_country(self):
        return self.get_text(self.BILLING_REGION_COUNTRY)
