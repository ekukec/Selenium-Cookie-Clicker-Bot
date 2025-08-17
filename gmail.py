import os
from time import sleep
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.chrome.options import Options
import undetected_chromedriver as uc

# Load environment variables
load_dotenv()

# Get credentials from environment
email_address = os.getenv('GMAIL_EMAIL')
password = os.getenv('GMAIL_PASSWORD')
wait_time = int(os.getenv('DEFAULT_WAIT_TIME', '10'))

if not email_address or not password:
    raise ValueError("Please set GMAIL_EMAIL and GMAIL_PASSWORD in your .env file")

options = Options()
user_agent = os.getenv('USER_AGENT', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36')
options.add_argument(f"user-agent={user_agent}")

chrome_driver_path = os.getenv('CHROME_DRIVER_PATH')
# driver = webdriver.Chrome(executable_path=chrome_driver_path)  # Commented out as using undetected chrome
driver = uc.Chrome(use_subprocess=True)

# Use environment variable for Gmail URL or fallback to the original long URL
gmail_url = os.getenv('GMAIL_LOGIN_URL', 'https://accounts.google.com/v3/signin/identifier?dsh=S335807938%3A1678301367762108&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F%3Ftab%3Drm%26ogbl&emr=1&followup=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F%3Ftab%3Drm%26ogbl&osid=1&passive=1209600&service=mail&flowName=GlifWebSignIn&flowEntry=ServiceLogin&ifkv=AWnogHcscDB9KuM0ZjEZfdHtR3hg09ynTtABi3S_SJLw7hWBXSljFLl_f_xt-Xrk3laT4czqyYSPqw')
driver.get(gmail_url)

email = driver.find_element(By.NAME, "identifier")
email.send_keys(email_address, Keys.TAB, Keys.TAB, Keys.TAB, Keys.ENTER)

try:
    login_wait_time = int(os.getenv('LOGIN_WAIT_TIME', '10'))
    wait = WebDriverWait(driver, login_wait_time).until(expected_conditions.visibility_of_element_located((By.NAME, "Passwd")))
    password_field = driver.find_element(By.NAME, "Passwd")
    password_field.send_keys(password, Keys.TAB, Keys.TAB, Keys.ENTER)
    sleep(wait_time)
finally:
    driver.quit()