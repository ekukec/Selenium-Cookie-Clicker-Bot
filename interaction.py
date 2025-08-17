import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Load environment variables
load_dotenv()

chrome_driver_path = os.getenv('CHROME_DRIVER_PATH', 'chromedriver')
driver = webdriver.Chrome(executable_path=chrome_driver_path)

url = os.getenv('WIKIPEDIA_URL', 'https://en.wikipedia.org/wiki/Main_Page')
driver.get(url)

article_button = driver.find_element(By.XPATH, "//a[@title='Special:Statistics']")

# print(article_button.text)
# article_button.click()

# all_portals = driver.find_element(By.LINK_TEXT, "Pages")
# all_portals.click()

search_term = os.getenv('WIKIPEDIA_SEARCH_TERM', 'python')
search = driver.find_element(By.NAME, "search")
search.send_keys(search_term)
search.send_keys(Keys.ENTER)

# Clean up
driver.quit()