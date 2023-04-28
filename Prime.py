import math

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
ek = ["CMR_210423105440426RiRR81849","CMR_210423112721896RiRR81890","CMR_210423101132440RiRR81775","CMR_200423163031233RiRR81701","CMR_200423163611132RiRR81703","CMR_210423102035903RiRR81790","CMR_200423163230589RiRR81702","CMR_210423105558029RiRR81850","CMR_200423163723445RiRR81704","CMR_210423112859954RiRR81892","CMR_200423164131007RiRR81705","CMR_210423101314491RiRR81776","CMR_210423113022294RiRR81893","CMR_210423111920100RiRR81880","CMR_200423164503687RiRR81706","CMR_200423164923666RiRR81707","CMR_210423112222675RiRR81883","CMR_210423105651688RiRR81852","CMR_210423105741290RiRR81854","CMR_210423101523881RiRR81778"]
opt = Options()
opt.add_experimental_option("debuggerAddress", "Localhost:9125")
driver = webdriver.Chrome(executable_path="D:\\KVS\\drivers\\chromedriver_win32\\chromedriver.exe",chrome_options=opt)
driver.get("https://ekharid.haryana.gov.in/FCI/CMR_AA_ProcessBill")

for i in ek:
    opt = Options()
    opt.add_experimental_option("debuggerAddress", "Localhost:9125")
    driver = webdriver.Chrome(executable_path="D:\\KVS\\drivers\\chromedriver_win32\\chromedriver.exe",chrome_options=opt)

    driver.find_element(By.ID, "txtSearch").send_keys(i)
    driver.find_element(By.ID, "btn_Filter").click()
    try:
        driver.find_element(By.XPATH, "(//*[@id='LnkDetails'])[2]").click()
    except:
            driver.find_element(By.ID, "LnkDetails").click()

    #msp1 = driver.find_element(By.ID, "ContentPlaceHolder1_grd_Heads_lbl_HeadRate_0").text
    msp2 = 3074.62
    weight1 = driver.find_element(By.ID, "ContentPlaceHolder1_grd_Heads_lbl_NetWeight_0").text
    cmd = driver.find_element(By.ID, "ContentPlaceHolder1_lblCommodityVariety").text
    agency = driver.find_element(By.ID, "ContentPlaceHolder1_lbl_Agency").text

    weight2 = float(weight1)
    if (cmd == "RRA 2022_23 FRK" or cmd == "RRC 2022_23 FRK"):
        weightfm1 = driver.find_element(By.ID, "ContentPlaceHolder1_grd_Heads_lbl_FRK_Wgt_0").text
        weightfm2 = float(weightfm1)
        weightfi1 = driver.find_element(By.ID, "ContentPlaceHolder1_grd_Heads_lbl_FRK_Wgt_1").text
        weightfi2 = float(weightfi1)

    if (cmd == "RRA 2022_23 FRK" or cmd == "RRC 2022_23 FRK"):
        inc = float(7300)

    if (weight2 > 291):
        truck = math.ceil(weight2 / 290)
    else:
        truck = 1
    if (cmd == "RRA 2022_23 FRK" or cmd == "RRC 2022_23 FRK"):
        gross = (weightfm2 * msp2) + (weightfi2 * inc)
        tds = math.ceil(gross * 0.001)
    else:
        gross = weight2 * msp2
        tds = math.ceil(gross*0.001)
    #paid1 = gross - 120 * truck #for DFSC
    #paid2 = gross - 120 * truck - tds #for HAFED
    if agency == "FOOD AND SUPPLY":
        paid = gross - 120 * truck
    else:
        paid = gross - 120 * truck - tds

    if cmd == "RRA 2022_23 FRK" or cmd == "RRC 2022_23 FRK":
        driver.find_element(By.ID, "ContentPlaceHolder1_grd_Heads_lbl_Comment_0").send_keys("MSP")
        #driver.find_element(By.ID, "ContentPlaceHolder1_grd_Heads_lbl_PassedAmount_0").send_keys(weightfm2 * msp2)
        driver.find_element(By.ID, "ContentPlaceHolder1_grd_Heads_lbl_ClaimedAmount_0").click()
        driver.find_element(By.ID, "ContentPlaceHolder1_grd_Heads_lbl_Comment_1").send_keys("INCREMENTAL COST")
        #driver.find_element(By.ID, "ContentPlaceHolder1_grd_Heads_lbl_PassedAmount_1").send_keys(weightfi2 * inc)
        driver.find_element(By.ID, "ContentPlaceHolder1_grd_Heads_lbl_ClaimedAmount_0").click()
        if (agency == "FOOD AND SUPPLY"):
            driver.find_element(By.ID, "ContentPlaceHolder1_txt_OtherDeduction").send_keys(120 * truck)
            driver.find_element(By.ID, "ContentPlaceHolder1_grd_Heads_lbl_ClaimedAmount_0").click()
        else:
            driver.find_element(By.ID, "ContentPlaceHolder1_txt_OtherDeduction").send_keys(120 * truck+tds)
            driver.find_element(By.ID, "ContentPlaceHolder1_grd_Heads_lbl_ClaimedAmount_0").click()
    else:
        #driver.find_element(By.ID, "ContentPlaceHolder1_grd_Heads_lbl_PassedAmount_0").send_keys(paid)
        #driver.find_element(By.ID, "ContentPlaceHolder1_grd_Heads_lbl_PassedAmount_0").send_keys(Keys.TAB)
        if (agency == "FOOD AND SUPPLY"):
            driver.find_element(By.ID, "ContentPlaceHolder1_txt_OtherDeduction").send_keys(120 * truck)
            driver.find_element(By.ID, "ContentPlaceHolder1_grd_Heads_lbl_ClaimedAmount_0").click()
        else:
            driver.find_element(By.ID, "ContentPlaceHolder1_txt_OtherDeduction").send_keys(120 * truck+tds)
            driver.find_element(By.ID, "ContentPlaceHolder1_grd_Heads_lbl_ClaimedAmount_0").click()

        """WebDriverWait(driver, 10).until(EC.alert_is_present())
        driver.switch_to.alert.accept()
        if agency == "FOOD AND SUPPLY":
            driver.find_element(By.ID, "ContentPlaceHolder1_grd_Heads_lbl_Comment_0").send_keys('WEIGHBRIDGE CHARGE')
        else:
            driver.find_element(By.ID, "ContentPlaceHolder1_grd_Heads_lbl_Comment_0").send_keys('WEIGHBRIDGE CHARGE+TDS')"""

    driver.find_element(By.ID, "txt_Reason").send_keys("PASSED")

    driver.find_element(By.ID, "btnPassBill").click()
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    driver.switch_to.alert.accept()