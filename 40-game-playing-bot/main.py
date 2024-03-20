from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/cookieclicker/")

# Select the English language
WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#langSelect-EN')))
language = driver.find_element(By.CSS_SELECTOR, value='#langSelect-EN')
language.click()

five_second_check = time.time() + 5

end_time = time.time() + 10

while True:
    try:
        # Select the cookie
        cookie = driver.find_element(By.CSS_SELECTOR, '#bigCookie')
        # Get the number of cookies text
        count = driver.find_element(By.CSS_SELECTOR, '#cookies')

        cookie.click()
    except StaleElementReferenceException:
        continue
    # Check if five seconds have passed
    if time.time() > five_second_check:
        try:
            # Get all the unlocked items
            unlocked_items = driver.find_elements(By.CSS_SELECTOR, '.unlocked')
            # Get the ids of the unlocked items
            unlocked_items_ids = ['#' + i.get_attribute('id') for i in unlocked_items]
            # Get the prices of the unlocked items
            prices = [driver.find_element(By.CSS_SELECTOR, item).text for item in unlocked_items_ids]
            # Remove the new line character and convert the prices to integers
            parsed_prices = [int(i.split('\n')[1]) for i in prices]
            # Combine the ids and prices into a dictionary
            unlocked_items_dict = {unlocked_items_ids[i]: parsed_prices[i] for i in range(len(unlocked_items_ids))}
            # Get the most expensive item
            most_expensive = max(parsed_prices)

            # Click the most expensive item
            for item_id, price in unlocked_items_dict.items():
                if price == most_expensive:
                    driver.find_element(By.CSS_SELECTOR, item_id).click()

            # Reset the clock
            five_second_check = time.time() + 5

        except:
            continue

        # End the game after the specified end_time
        if time.time() > end_time:
            print(count.text)

            break
