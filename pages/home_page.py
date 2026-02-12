from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):
   #Top Bar
   SEACH_ICON = (By.XPATH, "//button[@class='MuiButtonBase-root MuiFab-root MuiFab-circular MuiFab-sizeLarge MuiFab-colorInherit MuiFab-root MuiFab-circular MuiFab-sizeLarge MuiFab-colorInherit mui-style-1v1s05g']//*[name()='svg']")
   SEARCH_INPUT = (By.XPATH, "//input[@placeholder='Search all products...']")
   CART_ICON = (By.XPATH, "//a[@aria-label='Cart']")

   #Filters
   SIZE_BUTTON = (By.XPATH, "//p[normalize-space()='Size']")
   SIZE_36_40 = (By.XPATH, "//div[normalize-space()='Size 36 to 40']")
   SIZE_APPLY_BUTTON = (By.XPATH, "//button[normalize-space()='Apply']")

   #Products
   FIRST_SOCKS = (By.XPATH, "//h2[text()='Anna Socks']")
   SECOND_SOCKS = (By.XPATH, "//h2[text()='Tamara Socks']")
   
   def __init__(self, driver):
      super().__init__(driver)

   def is_loaded(self):
      return self.is_visible(self.SEACH_ICON)
      
   def click_search_icon(self):
      self.click(self.SEACH_ICON) 

   def enter_search_input(self, search_input):
      self.send_keys(self.SEARCH_INPUT, search_input)

   def click_cart_icon(self):
      self.click(self.CART_ICON)

   def click_size_button(self):
      self.click(self.SIZE_BUTTON)

   def click_size_36_40(self):
      self.click(self.SIZE_36_40)

   def click_size_apply_button(self):
      self.click(self.SIZE_APPLY_BUTTON)

   def click_first_socks(self):
    # self.wait_for_element_clickable(self.FIRST_SOCKS, 5)
    self.click(self.FIRST_SOCKS)

   def click_second_socks(self):
    # self.wait_for_element_clickable(self.SECOND_SOCKS, 5)
    self.click(self.SECOND_SOCKS)
