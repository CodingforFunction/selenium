from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(executable_path="D:\KVS\geckodriver-v0.31.0-win64\geckodriver.exe")
driver.get("https://ekharid.haryana.gov.in/fci/cmr_login")

ek = input("E-KHAIRD-->")

driver.find_element(By.ID, "txtSearch").send_keys(ek)
driver.find_element(By.ID, "btn_Filter").click()
driver.find_element(By.ID, "LnkDetails").click()