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

PROMISED_DOWN = 150
PROMISED_UP = 10

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
        self.down = self.driver.find_element(By.CLASS_NAME, "download-speed").text
        print(f"Download: {self.down}")
        self.up = self.driver.find_element(By.CLASS_NAME, "upload-speed").text
        print(f"Upload: {self.up}")


    def tweet_at_provider(self):
        self.driver.get("https://www.twitter.com")

        time.sleep(5)
        login_btn = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div[1]/div/div/div/div[2]/div[2]/div/div/div[1]/a')
        login_btn.click()

        time.sleep(3)
        email_field = self.driver.find_element(By.NAME, 'text')
        email_field.send_keys(TWITTER_EMAIL)
        email_field.send_keys(Keys.ENTER)

        time.sleep(3)
        username_field = self.driver.find_element(By.NAME, 'text')
        username_field.send_keys('ChiComplaintB')
        username_field.send_keys(Keys.ENTER)

        time.sleep(2)
        password_field = self.driver.find_element(By.NAME, 'password')
        password_field.send_keys(TWITTER_PASSWORD)
        password_field.send_keys(Keys.ENTER)

        time.sleep(5)
        tweet_box = self.driver.find_element(By.CLASS_NAME, 'public-DraftStyleDefault-block')
        tweet_box.click()


bot = InternetSpeedTwitterBot()
# bot.get_internet_speed()
bot.tweet_at_provider()
