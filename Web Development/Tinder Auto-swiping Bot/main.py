import os
import time
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

load_dotenv()

PHONE_NUMBER = os.getenv('PHONE_NUMBER')
PASSWORD = os.getenv('PASSWORD')

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

time.sleep(5)

# facebook_btn = driver.find_element(By.XPATH, '//*[@id="c-1480665743"]/main/div/div[1]/div/div/div[3]/span/div[2]/button')
# facebook_btn.click()

# driver.switch_to.frame('gsi_984808_861630')
WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, '//*[@id="gsi_984808_861630"]')))

google_continue = driver.find_element(By.XPATH, '//*[@id="container"]/div/div[2]/span[1]')
google_continue.click()

time.sleep(2)

base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]

driver.switch_to.window(fb_login_window)
print(driver.title)

time.sleep(3)

# phone_num = driver.find_element(By.XPATH, '//*[@id="email"]')
# phone_num.send_keys(PHONE_NUMBER)
# password = driver.find_element(By.NAME, "pass")
# password.send_keys(PASSWORD)
#
# fb_login = driver.find_element(By.NAME, "login")
# fb_login.click()
#
# time.sleep(10)



