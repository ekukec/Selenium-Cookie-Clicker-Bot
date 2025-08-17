import os
import time
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# Load environment variables
load_dotenv()

chrome_driver_path = os.getenv('CHROME_DRIVER_PATH', 'chromedriver')
driver = webdriver.Chrome(executable_path=chrome_driver_path)

url = os.getenv('COOKIE_CLICKER_URL', 'http://orteil.dashnet.org/experiments/cookie/')
driver.get(url)

cookie = driver.find_element(By.ID, "cookie")

game_start = time.perf_counter()
game_time = int(time.perf_counter() - game_start)
upgrade_done = 0
total_money = 0
total_time = int(os.getenv('GAME_DURATION', '120'))
upgrade_interval = int(os.getenv('UPGRADE_CHECK_INTERVAL', '5'))

while game_time < total_time:
    game_time = int(time.perf_counter() - game_start)

    if game_time % upgrade_interval == 0 and game_time != 0 and upgrade_done != game_time:
        money = int(driver.find_element(By.ID, "money").text.replace(",",""))
        total_money += money
        store_options = driver.find_element(By.ID, "store").find_elements(By.TAG_NAME, "div")
        store_options.pop()
        store_options.reverse()
        for option in store_options:
            print(f"DEBUG: {option.text}")
            option_price_fetched = False
            try:
                option_price = int(option.find_element(By.TAG_NAME, "b").text.split(" - ")[1].replace(",", ""))
                option_price_fetched = True
            except:
                option_price_fetched = False
                option_price = 0
            if option_price < money and option_price_fetched:
                id_to_buy = option.get_attribute('id')
                print(f"finding by id: {id_to_buy}\n{option.text}")
                driver.find_element(By.ID, id_to_buy).click()
                break

        upgrade_done = game_time
    else:
        cookie.click()

print(f"Time elapsed: {time.perf_counter() - game_start}\nMoney per second: {total_money / total_time}")
driver.quit()