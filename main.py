from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(options=options)

USR = "admin"
PASS = "ADD_YOUR_GATEWAY_PASSWORD_HERE"

driver.get("http://192.168.1.1")
username = WebDriverWait(driver,5).until(EC.presence_of_element_located((By.ID,"index_username")))
password = driver.find_element(By.ID,"password")
username.send_keys(USR)
password.send_keys(PASS + Keys.ENTER)
time.sleep(3) #Succesful LogIn
