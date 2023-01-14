import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

load_dotenv()

CHROME_DRIVER_PATH = os.getenv('CHROME_DRIVER_PATH')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.python.org/")
# price = driver.find_element(By.CLASS_NAME, "a-offscreen").text
event_times = driver.find_elements(By.CSS_SELECTOR, '.event-widget ul li time')
event_names = driver.find_elements(By.CSS_SELECTOR, '.event-widget ul li a')
events = {}

for n in range(len(event_times)):
    events[n] = {
        'time': event_times[n].text,
        'name': event_names[n].text
    }



print(events)
