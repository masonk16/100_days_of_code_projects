import os
import time
from dotenv import load_dotenv
import undetected_chromedriver as webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

load_dotenv()

EMAIL = os.getenv('EMAIL')
PASSWORD = os.getenv('PASSWORD')

# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option("detach", True)
# chrome_options.add_argument("--enable-automation")

CHROME_DRIVER_PATH = os.getenv('CHROME_DRIVER_PATH')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://tinder.com/")

# cookies = driver.find_element(By.LINK_TEXT, "I decline")
# cookies.click()

time.sleep(3)

login_btn = driver.find_element(By.LINK_TEXT, "Log in")
login_btn.click()

time.sleep(5)

google_btn = driver.find_element(By.TAG_NAME, 'iframe')
driver.switch_to.frame(google_btn)
google_continue = driver.find_element(By.XPATH, '//*[@id="container"]/div')
google_continue.click()

time.sleep(2)

base_window = driver.window_handles[0]
google_login_window = driver.window_handles[1]
driver.switch_to.window(google_login_window)
print(driver.title)

time.sleep(3)

email = driver.find_element(By.NAME, 'identifier')
email.send_keys(EMAIL)
email.send_keys(Keys.ENTER)

time.sleep(3)

password = driver.find_element(By.NAME, "Passwd")
password.send_keys(PASSWORD)
password.send_keys(Keys.ENTER)
#
# fb_login = driver.find_element(By.NAME, "login")
# fb_login.click()

time.sleep(10)

driver.switch_to.window(base_window)
print(driver.title)

#Allow location
allow_location_button = driver.find_element_by_xpath(By.XPATH, '//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
allow_location_button.click()

#Disallow notifications
notifications_button = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]')
notifications_button.click()

#Allow cookies
cookies = driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div[1]/button')
cookies.click()


