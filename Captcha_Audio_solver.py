from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium_recaptcha_solver import RecaptchaSolver
import time


chrome_options = Options()
chrome_options.add_argument("--disable-notifications") # Suppress browser notifications
chrome_options.add_argument("--start-maximized") # Start the browser window maximized

# Specify the path to the ChromeDriver
chrome_driver_path = '/path/to/chromedriver' # Replace with the actual path


# Initialize the WebDriver service and create a Chrome driver instance
service = Service(chrome_driver_path) 
driver = webdriver.Chrome(service=service, options=chrome_options)

# Define the target URL
url = "https://www.google.com/recaptcha/api2/demo"


solver = RecaptchaSolver(driver=driver)

driver.get(url)

recaptcha_iframe = driver.find_element(By.XPATH, '//iframe[@title="reCAPTCHA"]')
time.sleep(5)

solver.click_recaptcha_v2(iframe=recaptcha_iframe)