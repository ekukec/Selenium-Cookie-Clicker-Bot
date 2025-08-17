import os
import time
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By

# Load environment variables
load_dotenv()

chrome_driver_path = os.getenv('CHROME_DRIVER_PATH', 'chromedriver')
driver = webdriver.Chrome(chrome_driver_path)

url = os.getenv('COOKIE_CLICKER_URL', 'http://orteil.dashnet.org/experiments/cookie/')
driver.get(url)

# Get cookie to click on.
cookie = driver.find_element(By.ID,"cookie")

# Get upgrade item ids.
items = driver.find_elements(By.CSS_SELECTOR ,"#store div")
item_ids = [item.get_attribute("id") for item in items]

upgrade_interval = int(os.getenv('UPGRADE_CHECK_INTERVAL', '5'))
game_duration_minutes = int(os.getenv('GAME_DURATION_MINUTES', '5'))

timeout = time.time() + upgrade_interval
five_min = time.time() + 60 * game_duration_minutes

while True:
    cookie.click()

    # Every X seconds (from env):
    if time.time() > timeout:

        # Get all upgrade <b> tags
        all_prices = driver.find_elements(By.CSS_SELECTOR,"#store b")
        item_prices = []

        # Convert <b> text into an integer price.
        for price in all_prices:
            element_text = price.text
            if element_text != "":
                cost = int(element_text.split("-")[1].strip().replace(",", ""))
                item_prices.append(cost)

        # Create dictionary of store items and prices
        cookie_upgrades = {}
        for n in range(len(item_prices)):
            cookie_upgrades[item_prices[n]] = item_ids[n]

        # Get current cookie count
        money_element = driver.find_element(By.ID ,"money").text
        if "," in money_element:
            money_element = money_element.replace(",", "")
        cookie_count = int(money_element)

        # Find upgrades that we can currently afford
        affordable_upgrades = {}
        for cost, id in cookie_upgrades.items():
            if cookie_count > cost:
                affordable_upgrades[cost] = id

        # Purchase the most expensive affordable upgrade
        if affordable_upgrades:
            highest_price_affordable_upgrade = max(affordable_upgrades)
            print(highest_price_affordable_upgrade)
            to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]
            driver.find_element(By.ID, to_purchase_id).click()

        # Add another X seconds until the next check
        timeout = time.time() + upgrade_interval

    # After X minutes stop the bot and check the cookies per second count.
    if time.time() > five_min:
        cookie_per_s = driver.find_element(By.ID, "cps").text
        print(cookie_per_s)
        break

driver.quit()