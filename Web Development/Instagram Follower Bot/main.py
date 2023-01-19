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

USERNAME = os.getenv('USERNAME')
PASSWORD = os.getenv('PASSWORD')
CHROME_DRIVER_PATH = os.getenv('CHROME_DRIVER_PATH')

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

class InstaFollower:

    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    def login(self):
        pass

