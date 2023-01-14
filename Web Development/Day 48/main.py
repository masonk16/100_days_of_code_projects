import os
from dotenv import load_dotenv
from selenium import webdriver

load_dotenv()

CHROME_DRIVER_PATH = os.getenv('CHROME_DRIVER_PATH')
driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)


