from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
import time



chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.speedtest.net/")

driver.find_element(By.CSS_SELECTOR, '.start-text').click()

WebDriverWait(driver, 100).until(lambda driver: driver.find_element(By.CSS_SELECTOR, '.download-speed').text.replace('.', '', 1).isdigit())
WebDriverWait(driver, 100).until(lambda driver: driver.find_element(By.CSS_SELECTOR, '.upload-speed').text.replace('.', '', 1).isdigit())
upload_speed = driver.find_element(By.CSS_SELECTOR, '.upload-speed')
download_speed = driver.find_element(By.CSS_SELECTOR, '.download-speed')
print(download_speed.text)
print(upload_speed.text)

