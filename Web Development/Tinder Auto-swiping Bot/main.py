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

driver.get("https://tinder.com/")

# cookies = driver.find_element(By.LINK_TEXT, "I decline")
# cookies.click()

time.sleep(3)

login_btn = driver.find_element(By.LINK_TEXT, "Log in")
login_btn.click()

time.sleep(10)

facebook_btn = driver.find_element(By.XPATH, '//*[@id="c-1480665743"]/main/div/div[1]/div/div/div[3]/span/div[2]/button')
facebook_btn.click()
