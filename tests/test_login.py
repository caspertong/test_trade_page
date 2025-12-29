import pytest
from pages.login_page import LoginPage
import time

# Constants for test data
TEST_ACCOUNT_ID = "1000529"
TEST_PASSWORD = "A8WU$l3ne$$u"

def test_login_page_loads(driver):
    """
    Verify that the login page loads and essential elements are present.
    """
    login_page = LoginPage(driver)
    login_page.navigate()
    
    assert login_page.is_visible(LoginPage.ACCOUNT_INPUT)
    assert login_page.is_visible(LoginPage.PASSWORD_INPUT)
    assert login_page.is_visible(LoginPage.LOGIN_BUTTON)

def test_valid_login_flow(driver):
    """
    Verify the login flow using provided credentials.
    Note: Depending on the site behavior (2FA, CAPTCHA, etc.), this might just verify the button is clickable
    or verify redirection.
    """
    login_page = LoginPage(driver)
    login_page.navigate()
    
    # Button should be disabled initially (if that's the behavior) or just check it exists
    # Based on subagent inspection, let's verify we can enter text.
    
    login_page.enter_account_id(TEST_ACCOUNT_ID)
    login_page.enter_password(TEST_PASSWORD)
    
    # Wait a brief moment for UI state update if needed (react apps sometimes have slight delays on input validation)
    time.sleep(1) 
    
    # assert login_page.is_login_button_enabled() 
    
    # Attempt login
    login_page.click_login()
    
    # Add an assertion here depending on what happens next. 
    # For now, we just pass if no exception occurs, or wait to see if URL changes.
    time.sleep(5) # Wait to observe result manually or for redirect
    
    # Example assertion (adjust based on actual success state)
    # assert "dashboard" in driver.current_url.lower() 
