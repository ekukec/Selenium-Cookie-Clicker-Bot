import os
from dotenv import load_dotenv
from undetected_chromedriver import Chrome
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Load environment variables
load_dotenv()

class Google:
    def __init__(self) -> None:
        self.url = os.getenv('GOOGLE_LOGIN_URL', 'https://accounts.google.com/ServiceLogin')
        self.driver = Chrome(use_subprocess=True)
        self.driver.get(self.url)
        self.time = int(os.getenv('DEFAULT_WAIT_TIME', '10'))

    def login(self, email, password):
        sleep(2)
        login_wait_time = int(os.getenv('LOGIN_WAIT_TIME', '20'))
        
        WebDriverWait(self.driver, login_wait_time).until(
            EC.visibility_of_element_located((By.NAME, 'identifier'))
        ).send_keys(f'{email}\n')
        
        sleep(2)
        
        WebDriverWait(self.driver, login_wait_time).until(
            EC.visibility_of_element_located((By.NAME, 'Passwd'))
        ).send_keys(f'{password}\n')

        self.code()

    def code(self):
        # [ ---------- paste your code here ---------- ]
        sleep(self.time)
        self.driver.quit()

# Get credentials from environment variables
email = os.getenv('GMAIL_EMAIL')
password = os.getenv('GMAIL_PASSWORD')

# Validate that required environment variables are set
if not email:
    raise ValueError("Please set GMAIL_EMAIL in your .env file")
if not password:
    raise ValueError("Please set GMAIL_PASSWORD in your .env file")

# Create and use the Google class
google = Google()
google.login(email, password)