import math

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

ek = input("E-KHAIRD-->")
msp = 3074.62
#weight = float(input("DEL WEIGHT-->"))

opt = Options()
opt.add_experimental_option("debuggerAddress", "Localhost:9123")
driver = webdriver.Chrome(executable_path="D:\\KVS\\drivers\\chromedriver_win32\\chromedriver.exe", chrome_options=opt)
driver.get("https://ekharid.haryana.gov.in/FCI/CMR_AA_ProcessBill")
driver.find_element(By.ID,"txtSearch").send_keys(ek)
driver.find_element(By.ID,"btn_Filter").click()
driver.find_element(By.ID,"LnkDetails").click()

weight1 = driver.find_element(By.ID,"ContentPlaceHolder1_grd_Heads_lbl_NetWeight_0").text
weight2 = float(weight1)

truck = math.ceil(weight2/290)
paid = weight2*msp-120*truck
driver.find_element(By.ID,"ContentPlaceHolder1_grd_Heads_lbl_PassedAmount_0").send_keys(paid)
driver.find_element(By.ID,"ContentPlaceHolder1_grd_Heads_lbl_PassedAmount_0").send_keys(Keys.TAB)

WebDriverWait(driver, 10).until(EC.alert_is_present())
driver.switch_to.alert.accept()

driver.find_element(By.ID,"ContentPlaceHolder1_grd_Heads_lbl_Comment_0").send_keys('WEIGHBRIDGE CHARGE')
driver.find_element(By.ID,"txt_Reason").send_keys("PASSED")

driver.find_element(By.ID,"btnPassBill").click()
WebDriverWait(driver, 10).until(EC.alert_is_present())
driver.switch_to.alert.accept()