import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    """Centralized configuration for Selenium tests"""
    
    # Base URL
    BASE_URL = os.getenv("BASE_URL", "https://graphcommerce.vercel.app/")
    
    # Browser Settings
    BROWSER = os.getenv("BROWSER", "chrome").lower()
    HEADLESS = os.getenv("HEADLESS", "false").lower() == "true"
    
    # Wait Configuration (in seconds)
    DEFAULT_TIMEOUT = int(os.getenv("DEFAULT_TIMEOUT", "10"))
    SHORT_TIMEOUT = int(os.getenv("SHORT_TIMEOUT", "3"))
    LONG_TIMEOUT = int(os.getenv("LONG_TIMEOUT", "20"))
    POLL_FREQUENCY = float(os.getenv("POLL_FREQUENCY", "0.5"))
    
    # Page Load Timeout
    PAGE_LOAD_TIMEOUT = int(os.getenv("PAGE_LOAD_TIMEOUT", "30"))
    
    # Screenshot Settings
    SCREENSHOT_ON_FAILURE = os.getenv("SCREENSHOT_ON_FAILURE", "true").lower() == "true"
    SCREENSHOT_DIR = os.getenv("SCREENSHOT_DIR", "screenshots")
    
    # Test Credentials
    TEST_EMAIL = os.getenv("TEST_EMAIL", "test123@gmail.com")
    TEST_PASSWORD = os.getenv("TEST_PASSWORD", "K9#vP2m!zL4t-Q8x")
    
    # Retry Configuration
    MAX_RETRY_ATTEMPTS = int(os.getenv("MAX_RETRY_ATTEMPTS", "3"))
    RETRY_DELAY = float(os.getenv("RETRY_DELAY", "1"))
    
    @classmethod
    def ensure_dirs(cls):
        """Create necessary directories if they don't exist"""
        Path(cls.SCREENSHOT_DIR).mkdir(parents=True, exist_ok=True)
