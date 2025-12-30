import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

@pytest.fixture(scope="function")
def driver():
    options = Options()
    # options.add_argument("--headless")  # Uncomment for headless mode
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    
    # Initialize the Chrome driver
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    driver.maximize_window()
    
    yield driver
    
    # Teardown
    driver.quit()

@pytest.fixture(scope="function")
def login_to_trade(driver):
    from pages.login_page import LoginPage
    login_page = LoginPage(driver)
    login_page.navigate()
    login_page.enter_account_id("1000529")
    login_page.enter_password("A8WU$l3ne$$u")
    login_page.click_login()
    # Wait for redirect?
    time.sleep(5) 
    return driver
