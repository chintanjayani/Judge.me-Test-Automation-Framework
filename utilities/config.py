import os
from dotenv import load_dotenv

class Config:
    def __init__(self):
        load_dotenv()
        self.base_url = os.getenv('BASE_URL', 'https://judge.me')
        self.api_key = os.getenv('API_KEY')
        self.environment = os.getenv('ENVIRONMENT', 'test')
        self.browser = os.getenv('BROWSER', 'chromium')
        self.headless = os.getenv('HEADLESS', 'true').lower() == 'true'
        self.screenshot_on_failure = os.getenv('SCREENSHOT_ON_FAILURE', 'true').lower() == 'true'