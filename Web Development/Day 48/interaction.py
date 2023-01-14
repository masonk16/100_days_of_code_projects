import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

load_dotenv()

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

CHROME_DRIVER_PATH = os.getenv('CHROME_DRIVER_PATH')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

driver.get("http://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element(By.NAME, "fName")
first_name.send_keys("Mason")
last_name = driver.find_element(By.NAME, "lName")
last_name.send_keys("Mapfundematsva")
email = driver.find_element(By.NAME, "email")
email.send_keys("1mukanyawacho@gmail.com")

submit = driver.find_element(By.CSS_SELECTOR, 'form button')
submit.click()




# article_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
#
# search = driver.find_element(By.NAME, "search")
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)

