import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

opt = Options()
opt.add_experimental_option("debuggerAddress", "Localhost:9125")

driver = webdriver.Chrome(options=opt)
driver.get("https://www.hrmsfci.in/mss/dashboard")
bill = ["CET1148161"]
for i in bill:
    driver.get("https://www.hrmsfci.in/cb/transactions/travel-allowance/list")
    time.sleep(2)
    driver.find_element(By.XPATH, "(//input[@type='search'])").send_keys(i)
    time.sleep(2)
    driver.find_element(By.XPATH, "(//i[@class='fa fa-retweet'])[1]").click()
    driver.find_element(By.XPATH, "(//a[normalize-space()='View Action History'])[1]").click()
    time.sleep(10)
    driver.find_element(By.XPATH, "(//a[normalize-space()='Action History Report'])[1]").click()
    time.sleep(10)
    driver.find_element(By.XPATH, "(//button[normalize-space()='Download'])[1]").click()
