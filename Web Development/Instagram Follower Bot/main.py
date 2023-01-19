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

SIMILAR_ACC ='w211_army'

IG_USERNAME = os.getenv('IG_USERNAME')
PASSWORD = os.getenv('PASSWORD')
CHROME_DRIVER_PATH = os.getenv('CHROME_DRIVER_PATH')

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

class InstaFollower:

    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")

        time.sleep(5)
        username = self.driver.find_element(By.NAME, 'username')
        username.send_keys(IG_USERNAME)
        password = self.driver.find_element(By.NAME, 'password')
        password.send_keys(PASSWORD)

        time.sleep(3)
        password.send_keys(Keys.ENTER)

    def find_followers(self):
        time.sleep(3)
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACC}")

        time.sleep(2)
        followers_tag = self.driver.find_element(By.CSS_SELECTOR, 'div ul li a')
        followers_tag.click()

    def follow(self):
        pass


bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()
