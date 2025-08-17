import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By

# Load environment variables
load_dotenv()

# Uncomment and use these sections as needed:

# Amazon Price Checker Section
def check_amazon_price():
    chrome_driver_path = os.getenv('CHROME_DRIVER_PATH', 'chromedriver')
    driver = webdriver.Chrome(executable_path=chrome_driver_path)
    
    amazon_url = os.getenv('AMAZON_URL', 'https://www.amazon.com/Instant-Pot-Ultra-Programmable-Sterilizer/dp/B06Y1MP2PY/ref=pd_rhf_d_ee_s_pd_sbs_rvi_sccl_1_1/135-0460176-6142851?pd_rd_w=ajYm2&content-id=amzn1.sym.a089f039-4dde-401a-9041-8b534ae99e65&pf_rd_p=a089f039-4dde-401a-9041-8b534ae99e65&pf_rd_r=DXMH2P11MG8EBAPZ060P&pd_rd_wg=ODUOg&pd_rd_r=4efb55e1-73cd-402a-8f9f-cd8ae7ccb159&pd_rd_i=B06Y1MP2PY&th=1')
    
    driver.get(amazon_url)
    try:
        price = driver.find_element(By.ID, "corePrice_feature_div")
        print(price.text)
    except Exception as e:
        print(f"Could not find price: {e}")
    finally:
        driver.quit()

# Python.org Scraper Section
def scrape_python_org():
    chrome_driver_path = os.getenv('CHROME_DRIVER_PATH', 'chromedriver')
    driver = webdriver.Chrome(executable_path=chrome_driver_path)
    
    python_url = os.getenv('PYTHON_ORG_URL', 'https://python.org')
    driver.get(python_url)
    
    try:
        # Search bar
        search_bar = driver.find_element(By.NAME, "q")
        print(f"Search bar found: {search_bar.tag_name}")
        print(f"Placeholder: {search_bar.get_attribute('placeholder')}")
        
        # Logo
        logo = driver.find_element(By.CLASS_NAME, "python-logo")
        print(f"Logo size: {logo.size}")
        
        # Documentation link
        documentation_link = driver.find_element(By.CSS_SELECTOR, ".documentation-widget a")
        print(f"Documentation link text: {documentation_link.text}")
        
        # Submit bug button
        submit_bug_button = driver.find_element(By.XPATH, '//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
        print(f"Submit bug button text: {submit_bug_button.text}")
        
    except Exception as e:
        print(f"Error scraping python.org: {e}")
    finally:
        driver.quit()

# Events Scraper Section
def scrape_python_events():
    chrome_driver_path = os.getenv('CHROME_DRIVER_PATH', 'chromedriver')
    driver = webdriver.Chrome(executable_path=chrome_driver_path)
    
    python_url = os.getenv('PYTHON_ORG_URL', 'https://python.org')
    driver.get(python_url)
    
    try:
        upcoming_events_array = [
            row.text for row in driver.find_element(By.CLASS_NAME, "event-widget")
            .find_element(By.CLASS_NAME, "menu")
            .find_elements(By.TAG_NAME, "li")
        ]
        upcoming_events = {}
        
        counter = 0
        for event in upcoming_events_array:
            try:
                time = event.split("\n")[0]
                name = event.split("\n")[1]
                upcoming_events[counter] = {"time": time, "name": name}
                counter += 1
            except IndexError:
                continue
        
        print("Upcoming Python Events:")
        for event_id, event_data in upcoming_events.items():
            print(f"{event_id}: {event_data['time']} - {event_data['name']}")
            
    except Exception as e:
        print(f"Error scraping events: {e}")
    finally:
        driver.quit()

# Main execution
if __name__ == "__main__":
    # Choose which function to run by uncommenting:
    
    # check_amazon_price()
    # scrape_python_org()
    # scrape_python_events()
    
    # Or import and run other modules:
    # import interaction
    # import gmailV2
    import cookie_clicker