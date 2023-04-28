from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

opt = Options()
opt.add_experimental_option("debuggerAddress", "Localhost:9125")
driver = webdriver.Chrome(executable_path="D:\\KVS\\drivers\\chromedriver_win32\\chromedriver.exe",chrome_options=opt)
driver.get("https://ekharid.haryana.gov.in/FCI/CMR_AA_ProcessBill")
ek = ["CMR_261222103338257RiRR9592","CMR_090223115735719RiRR37601"]
for i in ek:
    driver.find_element(By.ID, "txtSearch").send_keys(i)
    driver.find_element(By.ID, "btn_Filter").click()
    driver.find_element(By.ID, "LnkDetails").click()
    a = driver.find_element(By.ID, "ContentPlaceHolder1_grd_Heads_lbl_ClaimedAmount_0").text
    driver.find_element(By.ID, "ContentPlaceHolder1_grd_Heads_lbl_PassedAmount_0").send_keys(a)
    driver.find_element(By.ID, "ContentPlaceHolder1_grd_Heads_lbl_ClaimedAmount_0").click()
    a = driver.find_element(By.ID, "ContentPlaceHolder1_grd_Heads_lbl_ClaimedAmount_1").text
    driver.find_element(By.ID, "ContentPlaceHolder1_grd_Heads_lbl_PassedAmount_1").send_keys(a)
    driver.find_element(By.ID, "ContentPlaceHolder1_grd_Heads_lbl_ClaimedAmount_1").click()
    a = driver.find_element(By.ID, "ContentPlaceHolder1_grd_Heads_lbl_ClaimedAmount_2").text
    driver.find_element(By.ID, "ContentPlaceHolder1_grd_Heads_lbl_PassedAmount_2").send_keys(a)
    driver.find_element(By.ID, "ContentPlaceHolder1_grd_Heads_lbl_ClaimedAmount_2").click()
    a = driver.find_element(By.ID, "ContentPlaceHolder1_grd_Heads_lbl_ClaimedAmount_3").text
    driver.find_element(By.ID, "ContentPlaceHolder1_grd_Heads_lbl_PassedAmount_3").send_keys(a)
    driver.find_element(By.ID, "ContentPlaceHolder1_grd_Heads_lbl_ClaimedAmount_2").click()
    a = driver.find_element(By.ID, "ContentPlaceHolder1_grd_Heads_lbl_ClaimedAmount_4").text
    driver.find_element(By.ID, "ContentPlaceHolder1_grd_Heads_lbl_PassedAmount_4").send_keys(a)
    driver.find_element(By.ID, "ContentPlaceHolder1_grd_Heads_lbl_ClaimedAmount_2").click()
    a = driver.find_element(By.ID, "ContentPlaceHolder1_grd_Heads_lbl_ClaimedAmount_5").text
    driver.find_element(By.ID, "ContentPlaceHolder1_grd_Heads_lbl_PassedAmount_5").send_keys(a)
    driver.find_element(By.ID, "ContentPlaceHolder1_grd_Heads_lbl_ClaimedAmount_2").click()
    a = driver.find_element(By.ID, "ContentPlaceHolder1_grd_Heads_lbl_ClaimedAmount_6").text
    driver.find_element(By.ID, "ContentPlaceHolder1_grd_Heads_lbl_PassedAmount_6").send_keys(a)
    driver.find_element(By.ID, "ContentPlaceHolder1_grd_Heads_lbl_ClaimedAmount_2").click()
    a = driver.find_element(By.ID, "ContentPlaceHolder1_grd_Heads_lbl_ClaimedAmount_7").text
    driver.find_element(By.ID, "ContentPlaceHolder1_grd_Heads_lbl_PassedAmount_7").send_keys(a)
    driver.find_element(By.ID, "ContentPlaceHolder1_grd_Heads_lbl_ClaimedAmount_2").click()
    a = driver.find_element(By.ID, "ContentPlaceHolder1_grd_Heads_lbl_ClaimedAmount_8").text
    driver.find_element(By.ID, "ContentPlaceHolder1_grd_Heads_lbl_PassedAmount_8").send_keys(a)
    driver.find_element(By.ID, "ContentPlaceHolder1_grd_Heads_lbl_ClaimedAmount_2").click()
    a = driver.find_element(By.ID, "ContentPlaceHolder1_grd_Heads_lbl_ClaimedAmount_9").text
    driver.find_element(By.ID, "ContentPlaceHolder1_grd_Heads_lbl_PassedAmount_9").send_keys(a)
    driver.find_element(By.ID, "ContentPlaceHolder1_grd_Heads_lbl_ClaimedAmount_2").click()

    driver.find_element(By.ID, "txt_Reason").send_keys("PASSED")
    driver.find_element(By.ID, "btnPassBill").click()
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    driver.switch_to.alert.accept()