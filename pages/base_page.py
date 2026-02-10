from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import (
    TimeoutException,
    StaleElementReferenceException,
    ElementClickInterceptedException,
    NoSuchElementException
)
from config import Config
from utils.wait_helpers import (
    wait_for_element_visible,
    wait_for_element_to_be_clickable,
    wait_for_element_present,
    wait_for_element_to_disappear,
    wait_for_page_load,
    wait_for_ajax
)
import time


class BasePage:
    """Base page object with robust wait strategies and reusable actions"""
    
    def __init__(self, driver):
        self.driver = driver
        self.timeout = Config.DEFAULT_TIMEOUT
        self.short_timeout = Config.SHORT_TIMEOUT
        self.long_timeout = Config.LONG_TIMEOUT

    def open_url(self, url):
        """Navigate to URL and wait for page load"""
        self.driver.get(url)
        wait_for_page_load(self.driver)

    def find_element(self, locator, timeout=None):
        """Find element with explicit wait for visibility"""
        return wait_for_element_visible(self.driver, locator, timeout)
    
    def find_element_present(self, locator, timeout=None):
        """Find element present in DOM (not necessarily visible)"""
        return wait_for_element_present(self.driver, locator, timeout)
    
    def wait_for_element_visible(self, locator, timeout=None):
        """Wait for element to be visible"""
        return wait_for_element_visible(self.driver, locator, timeout)
    
    def wait_for_element_clickable(self, locator, timeout=None):
        """Wait for element to be clickable"""
        return wait_for_element_to_be_clickable(self.driver, locator, timeout)
    
    def wait_for_element_disappear(self, locator, timeout=None):
        """Wait for element to disappear (overlays, modals)"""
        return wait_for_element_to_disappear(self.driver, locator, timeout)
    
    def click(self, locator, timeout=None, retry=True):
        """
        Click element with retry mechanism for intercepted clicks
        
        Args:
            locator: Tuple of (By, selector)
            timeout: Wait timeout
            retry: Whether to retry on ElementClickInterceptedException
        """
        attempts = Config.MAX_RETRY_ATTEMPTS if retry else 1
        
        for attempt in range(attempts):
            try:
                element = wait_for_element_to_be_clickable(self.driver, locator, timeout, retry=False)
                # Scroll element into view
                self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
                element.click()
                return
            except ElementClickInterceptedException:
                if attempt == attempts - 1:
                    # Last attempt - try JavaScript click
                    element = self.find_element_present(locator, timeout)
                    self.driver.execute_script("arguments[0].click();", element)
                else:
                    time.sleep(Config.RETRY_DELAY)
            except StaleElementReferenceException:
                if attempt == attempts - 1:
                    raise
                time.sleep(Config.RETRY_DELAY)

    def wait_and_click(self, locator, timeout=None):
        """Alias for click with explicit wait"""
        self.click(locator, timeout)
    
    def send_keys(self, locator, text, clear_first=True, timeout=None):
        """
        Send keys to input element with optional clear
        
        Args:
            locator: Tuple of (By, selector)
            text: Text to send
            clear_first: Whether to clear field first
            timeout: Wait timeout
        """
        element = wait_for_element_to_be_clickable(self.driver, locator, timeout)
        
        if clear_first:
            # Use Ctrl+A + Backspace for better reliability than .clear()
            element.click()
            element.send_keys(Keys.CONTROL + "a")
            element.send_keys(Keys.BACKSPACE)
        
        element.send_keys(text)
    
    def send_keys_slowly(self, locator, text, delay=0.1, timeout=None):
        """
        Send keys with delay between each keystroke (for sensitive inputs)
        
        Args:
            locator: Tuple of (By, selector)
            text: Text to send
            delay: Delay between keystrokes in seconds
            timeout: Wait timeout
        """
        element = wait_for_element_to_be_clickable(self.driver, locator, timeout)
        for char in text:
            element.send_keys(char)
            time.sleep(delay)
    
    def get_text(self, locator, timeout=None):
        """Get text from element"""
        element = self.find_element(locator, timeout)
        return element.text
    
    def get_attribute(self, locator, attribute, timeout=None):
        """Get attribute value from element"""
        element = self.find_element(locator, timeout)
        return element.get_attribute(attribute)

    def is_visible(self, locator, timeout=None):
        """Check if element is visible"""
        timeout = timeout or self.short_timeout
        try:
            wait_for_element_visible(self.driver, locator, timeout)
            return True
        except TimeoutException:
            return False
    
    def is_present(self, locator, timeout=None):
        """Check if element is present in DOM"""
        timeout = timeout or self.short_timeout
        try:
            wait_for_element_present(self.driver, locator, timeout)
            return True
        except TimeoutException:
            return False
            
    def is_enabled(self, locator, timeout=None):
        """Check if element is enabled"""
        try:
            element = wait_for_element_present(self.driver, locator, timeout)
            return element.is_enabled()
        except TimeoutException:
            return False
    
    def is_clickable(self, locator, timeout=None):
        """Check if element is clickable"""
        timeout = timeout or self.short_timeout
        try:
            wait_for_element_to_be_clickable(self.driver, locator, timeout, retry=False)
            return True
        except TimeoutException:
            return False
    
    def scroll_to_element(self, locator, timeout=None):
        """Scroll element into view"""
        element = self.find_element_present(locator, timeout)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        return element
    
    def hover(self, locator, timeout=None):
        """Hover over element"""
        element = self.find_element(locator, timeout)
        ActionChains(self.driver).move_to_element(element).perform()
    
    def wait_for_page_load(self):
        """Wait for page to fully load"""
        wait_for_page_load(self.driver)
    
    def wait_for_ajax(self):
        """Wait for AJAX calls to complete"""
        wait_for_ajax(self.driver)
    
    def refresh_page(self):
        """Refresh the page and wait for load"""
        self.driver.refresh()
        wait_for_page_load(self.driver)
    
    def get_current_url(self):
        """Get current URL"""
        return self.driver.current_url
    
    def switch_to_frame(self, locator, timeout=None):
        """Switch to iframe"""
        element = self.find_element(locator, timeout)
        self.driver.switch_to.frame(element)
    
    def switch_to_default_content(self):
        """Switch back to main content from iframe"""
        self.driver.switch_to.default_content()
    
    def execute_script(self, script, *args):
        """Execute JavaScript"""
        return self.driver.execute_script(script, *args)
    
    def take_screenshot(self, filename):
        """Take screenshot and save to file"""
        Config.ensure_dirs()
        filepath = f"{Config.SCREENSHOT_DIR}/{filename}"
        self.driver.save_screenshot(filepath)
        return filepath
