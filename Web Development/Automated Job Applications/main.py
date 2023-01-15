import os
import time
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

load_dotenv()

ACCOUNT_EMAIL = os.getenv('ACCOUNT_EMAIL')
ACCOUNT_PASSWORD = os.getenv('ACCOUNT_PASSWORD')

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

CHROME_DRIVER_PATH = os.getenv('CHROME_DRIVER_PATH')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3436115481&f_AL=true&f_E=2%2C3&f_T=9%2C25169%2C25194&f_TPR=r2592000&f_WT=2&keywords=python%20developer&refresh=true&sortBy=R")

sign_in_button = driver.find_element(By.LINK_TEXT, "Sign in")
sign_in_button.click()

#Wait for the next page to load.
time.sleep(5)

email_field = driver.find_element(By.ID, "username")
email_field.send_keys(ACCOUNT_EMAIL)
password_field = driver.find_element(By.ID, "password")
password_field.send_keys(ACCOUNT_PASSWORD)
password_field.send_keys(Keys.ENTER)
