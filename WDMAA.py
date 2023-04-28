from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

opt = Options()
opt.add_experimental_option("debuggerAddress", "Localhost:9125")
driver = webdriver.Chrome(executable_path="D:\\KVS\\drivers\\chromedriver_win32\\chromedriver.exe",chrome_options=opt)
driver.get("https://ekharid.haryana.gov.in/FCI/WDM_AA_Bill")
bill = ["WDM_130423161304044WhUR21954","WDM_130423160337282WhUR21953","WDM_130423163053554WhUR21956","WDM_130423162458161WhUR21955"]
amt = ["638340","618928","71500","60698"]
for (a,b) in zip(bill,amt):
    driver.find_element(By.ID, "txtSearch").send_keys(a)
    driver.find_element(By.ID, "btn_Filter").click()
    driver.find_element(By.ID, "LnkDetails").click()
    driver.find_element(By.ID, "txt_Total_PayableAmount").send_keys(b)
    driver.find_element(By.ID, "txt_Reason").send_keys("Passed")
    driver.find_element(By.ID, "btnPassBill").click()
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    driver.switch_to.alert.accept()

