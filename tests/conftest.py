import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from config import Config
from utils.wait_helpers import wait_for_page_load, wait_for_url_contains


@pytest.fixture(scope="function")
def driver(request):
    """WebDriver fixture with configuration support"""
    
    # Ensure necessary directories exist
    Config.ensure_dirs()
    
    # Configure browser based on config
    if Config.BROWSER == "chrome":
        options = Options()
        if Config.HEADLESS:
            options.add_argument("--headless")
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        # Disable automation flags for better stability
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        
        driver = webdriver.Chrome(options=options)
    
    elif Config.BROWSER == "firefox":
        options = FirefoxOptions()
        if Config.HEADLESS:
            options.add_argument("--headless")
        options.add_argument("--width=1920")
        options.add_argument("--height=1080")
        
        driver = webdriver.Firefox(options=options)
    
    else:
        raise ValueError(f"Unsupported browser: {Config.BROWSER}")
    
    # Set page load timeout
    driver.set_page_load_timeout(Config.PAGE_LOAD_TIMEOUT)
    
    # NO IMPLICIT WAIT - Using explicit waits only
    driver.maximize_window()
    
    yield driver
    
    # Screenshot on failure
    if Config.SCREENSHOT_ON_FAILURE and request.node.rep_call.failed:
        test_name = request.node.name
        driver.save_screenshot(f"{Config.SCREENSHOT_DIR}/{test_name}_failure.png")
    
    # Teardown
    driver.quit()


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    """Hook to capture test results for screenshot on failure"""
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)


@pytest.fixture(scope="function")
def login_to_trade(driver):
    """Login fixture that uses explicit waits instead of sleep"""
    from pages.login_page import LoginPage
    from utils.wait_helpers import wait_for_url_contains
    
    login_page = LoginPage(driver)
    login_page.navigate()
    login_page.enter_account_id(Config.TEST_USERNAME)
    login_page.enter_password(Config.TEST_PASSWORD)
    login_page.click_login()
    
    # Wait for redirect to trade page instead of fixed sleep
    wait_for_url_contains(driver, "/trade", timeout=Config.DEFAULT_TIMEOUT)
    wait_for_page_load(driver)
    
    return driver
