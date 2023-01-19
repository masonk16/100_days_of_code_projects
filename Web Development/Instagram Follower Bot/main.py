import os
import time
from dotenv import load_dotenv
from selenium import webdriver
from selenium.common import ElementClickInterceptedException
from selenium.webdriver import ActionChains
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

        time.sleep(5)
        modal_root = self.driver.find_element(By.ID, 'ssrb_root_start')
        self.driver.execute_script("arguments[0].style.display='block';", modal_root)
        modal_end = self.driver.find_element(By.ID, 'ssrb_root_end')
        self.driver.execute_script("arguments[0].style.display='block';", modal_end)
        modal = self.driver.find_element(By.XPATH, '//*[@id="mount_0_0_Lj"]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]')
        for i in range(10):
            # In this case we're executing some Javascript, that's what the execute_script() method does.
            # The method can accept the script as well as a HTML element.
            # The modal in this case, becomes the arguments[0] in the script.
            # Then we're using Javascript to say: "scroll the top of the modal (popup) element by the height of the modal (popup)"
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

    def follow(self):
        all_buttons = self.driver.find_elements(By.CSS_SELECTOR, "li button")
        for button in all_buttons:
            try:
                button.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(By.XPATH, '/html/body/div[5]/div/div/div/div[3]/button[2]')
                cancel_button.click()


bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()
