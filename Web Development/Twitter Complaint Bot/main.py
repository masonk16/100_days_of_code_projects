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

PROMISED_UP = 10
PROMISED_DOWN = 150
TWITTER_EMAIL = os.getenv('TWITTER_EMAIL')
TWITTER_PASSWORD = os.getenv('TWITTER_PASSWORD')
CHROME_DRIVER_PATH = os.getenv('CHROME_DRIVER_PATH')

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")

        time.sleep(5)
        go_btn = self.driver.find_element(By.CSS_SELECTOR, ".start-button a")
        go_btn.click()

        time.sleep(90)
        self.up = self.driver.find_element(By.CLASS_NAME, "upload-speed").text
        print(self.up)
        self.down = self.driver.find_element(By.CLASS_NAME, "download-speed").text
        print(self.down)

    def tweet_at_provider(self):
        pass


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
# bot.tweet_at_provider()
