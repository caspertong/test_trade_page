from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    TimeoutException, 
    StaleElementReferenceException,
    ElementClickInterceptedException
)
from config import Config
import time


def wait_for_element_to_be_clickable(driver, locator, timeout=None, retry=True):
    """
    Wait for element to be clickable with retry mechanism
    
    Args:
        driver: WebDriver instance
        locator: Tuple of (By, selector)
        timeout: Wait timeout in seconds (uses Config.DEFAULT_TIMEOUT if not provided)
        retry: Whether to retry on StaleElementReferenceException
        
    Returns:
        WebElement that is clickable
    """
    timeout = timeout or Config.DEFAULT_TIMEOUT
    attempts = Config.MAX_RETRY_ATTEMPTS if retry else 1
    
    for attempt in range(attempts):
        try:
            element = WebDriverWait(driver, timeout, poll_frequency=Config.POLL_FREQUENCY).until(
                EC.element_to_be_clickable(locator)
            )
            return element
        except StaleElementReferenceException:
            if attempt == attempts - 1:
                raise
            time.sleep(Config.RETRY_DELAY)
        except TimeoutException:
            raise TimeoutException(f"Element {locator} not clickable after {timeout} seconds")


def wait_for_element_visible(driver, locator, timeout=None):
    """
    Wait for element to be visible
    
    Args:
        driver: WebDriver instance
        locator: Tuple of (By, selector)
        timeout: Wait timeout in seconds
        
    Returns:
        Visible WebElement
    """
    timeout = timeout or Config.DEFAULT_TIMEOUT
    try:
        element = WebDriverWait(driver, timeout, poll_frequency=Config.POLL_FREQUENCY).until(
            EC.visibility_of_element_located(locator)
        )
        return element
    except TimeoutException:
        raise TimeoutException(f"Element {locator} not visible after {timeout} seconds")


def wait_for_element_present(driver, locator, timeout=None):
    """
    Wait for element to be present in DOM (not necessarily visible)
    
    Args:
        driver: WebDriver instance
        locator: Tuple of (By, selector)
        timeout: Wait timeout in seconds
        
    Returns:
        WebElement present in DOM
    """
    timeout = timeout or Config.DEFAULT_TIMEOUT
    try:
        element = WebDriverWait(driver, timeout, poll_frequency=Config.POLL_FREQUENCY).until(
            EC.presence_of_element_located(locator)
        )
        return element
    except TimeoutException:
        raise TimeoutException(f"Element {locator} not present after {timeout} seconds")


def wait_for_element_to_disappear(driver, locator, timeout=None):
    """
    Wait for element to disappear (useful for overlays, modals)
    
    Args:
        driver: WebDriver instance
        locator: Tuple of (By, selector)
        timeout: Wait timeout in seconds
        
    Returns:
        True if element disappeared
    """
    timeout = timeout or Config.SHORT_TIMEOUT
    try:
        WebDriverWait(driver, timeout, poll_frequency=Config.POLL_FREQUENCY).until(
            EC.invisibility_of_element_located(locator)
        )
        return True
    except TimeoutException:
        return False


def wait_for_text_in_element(driver, locator, text, timeout=None):
    """
    Wait for specific text to appear in element
    
    Args:
        driver: WebDriver instance
        locator: Tuple of (By, selector)
        text: Expected text
        timeout: Wait timeout in seconds
        
    Returns:
        True if text found
    """
    timeout = timeout or Config.DEFAULT_TIMEOUT
    try:
        WebDriverWait(driver, timeout, poll_frequency=Config.POLL_FREQUENCY).until(
            EC.text_to_be_present_in_element(locator, text)
        )
        return True
    except TimeoutException:
        raise TimeoutException(f"Text '{text}' not found in element {locator} after {timeout} seconds")


def wait_for_url_change(driver, old_url, timeout=None):
    """
    Wait for URL to change from old_url
    
    Args:
        driver: WebDriver instance
        old_url: Previous URL
        timeout: Wait timeout in seconds
        
    Returns:
        New URL
    """
    timeout = timeout or Config.DEFAULT_TIMEOUT
    try:
        WebDriverWait(driver, timeout, poll_frequency=Config.POLL_FREQUENCY).until(
            lambda d: d.current_url != old_url
        )
        return driver.current_url
    except TimeoutException:
        raise TimeoutException(f"URL did not change from {old_url} after {timeout} seconds")


def wait_for_url_contains(driver, url_fragment, timeout=None):
    """
    Wait for URL to contain specific fragment
    
    Args:
        driver: WebDriver instance
        url_fragment: Fragment that should be in URL
        timeout: Wait timeout in seconds
        
    Returns:
        True if URL contains fragment
    """
    timeout = timeout or Config.DEFAULT_TIMEOUT
    try:
        WebDriverWait(driver, timeout, poll_frequency=Config.POLL_FREQUENCY).until(
            EC.url_contains(url_fragment)
        )
        return True
    except TimeoutException:
        raise TimeoutException(f"URL does not contain '{url_fragment}' after {timeout} seconds")


def wait_for_element_attribute(driver, locator, attribute, value, timeout=None):
    """
    Wait for element attribute to have specific value
    
    Args:
        driver: WebDriver instance
        locator: Tuple of (By, selector)
        attribute: Attribute name
        value: Expected attribute value
        timeout: Wait timeout in seconds
        
    Returns:
        True if attribute has expected value
    """
    timeout = timeout or Config.DEFAULT_TIMEOUT
    try:
        WebDriverWait(driver, timeout, poll_frequency=Config.POLL_FREQUENCY).until(
            lambda d: d.find_element(*locator).get_attribute(attribute) == value
        )
        return True
    except TimeoutException:
        raise TimeoutException(
            f"Element {locator} attribute '{attribute}' did not equal '{value}' after {timeout} seconds"
        )


def wait_for_page_load(driver, timeout=None):
    """
    Wait for page to fully load (document.readyState === 'complete')
    
    Args:
        driver: WebDriver instance
        timeout: Wait timeout in seconds
        
    Returns:
        True if page loaded
    """
    timeout = timeout or Config.PAGE_LOAD_TIMEOUT
    try:
        WebDriverWait(driver, timeout, poll_frequency=Config.POLL_FREQUENCY).until(
            lambda d: d.execute_script("return document.readyState") == "complete"
        )
        return True
    except TimeoutException:
        raise TimeoutException(f"Page did not load after {timeout} seconds")


def wait_for_ajax(driver, timeout=None):
    """
    Wait for jQuery AJAX calls to complete (if jQuery is present)
    
    Args:
        driver: WebDriver instance
        timeout: Wait timeout in seconds
        
    Returns:
        True if AJAX completed
    """
    timeout = timeout or Config.SHORT_TIMEOUT
    try:
        WebDriverWait(driver, timeout, poll_frequency=Config.POLL_FREQUENCY).until(
            lambda d: d.execute_script("return typeof jQuery !== 'undefined' ? jQuery.active == 0 : true")
        )
        return True
    except TimeoutException:
        # Not critical if jQuery doesn't exist
        return True
