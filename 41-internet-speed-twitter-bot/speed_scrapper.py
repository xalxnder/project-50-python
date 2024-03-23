from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.speedtest.net/")

driver.find_element(By.CSS_SELECTOR, '.start-text').click()


def get_speeds():
    """

    Returns:
        tuple: Returns a tuple containg download speed, and upload speed.

    """
    WebDriverWait(driver, 100).until(
        lambda driver: driver.find_element(By.CSS_SELECTOR, '.download-speed').text.replace('.', '', 1).isdigit())
    WebDriverWait(driver, 100).until(
        lambda driver: driver.find_element(By.CSS_SELECTOR, '.upload-speed').text.replace('.', '', 1).isdigit())
    upload_speed = driver.find_element(By.CSS_SELECTOR, '.upload-speed').text
    download_speed = driver.find_element(By.CSS_SELECTOR, '.download-speed').text
    return download_speed, upload_speed
