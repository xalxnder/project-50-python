from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/cookieclicker/")

WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#langSelect-EN')))

language = driver.find_element(By.CSS_SELECTOR, value='#langSelect-EN')
language.click()


cookie_count = 0
for i in range(5000):
    while True:
        try:
            cookie = driver.find_element(By.CSS_SELECTOR, '#bigCookie')
            count = driver.find_element(By.CSS_SELECTOR, '#cookies')
            count = int(count.text.split(' ')[0])
            print(type(count))
            cookie.click()
            break
        except StaleElementReferenceException:
            continue



# print(cookie)
# for i in range(1000):
#     cookie.click()
# article_number = driver.find_element(By.XPATH, value='//*[@id="articlecount"]/a[1]')
# anyone = driver.find_element(By.LINK_TEXT, value='anyone can edit')
#
#
# search = driver.find_element(By.NAME, value='search')
# search.send_keys('Python')
# search.send_keys(Keys.RETURN)

