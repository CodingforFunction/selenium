from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
opt = Options()
opt.add_experimental_option("debuggerAddress", "Localhost:9125")
driver = webdriver.Chrome(executable_path="D:\\KVS\\drivers\\chromedriver_win32\\chromedriver.exe", chrome_options=opt)
driver.get("https://ekharid.haryana.gov.in/FCI/CMR_AA_BillMgmt")
ek = ["CMR_210423100630380RiRR81767","CMR_210423105259790RiRR81846","CMR_210423105342252RiRR81847","CMR_210423100925841RiRR81773","CMR_200423162722361RiRR81700","CMR_210423112430796RiRR81886","CMR_210423105440426RiRR81849","CMR_210423112721896RiRR81890","CMR_210423101132440RiRR81775","CMR_200423163031233RiRR81701","CMR_200423163611132RiRR81703","CMR_210423102035903RiRR81790","CMR_200423163230589RiRR81702","CMR_210423105558029RiRR81850","CMR_200423163723445RiRR81704","CMR_210423112859954RiRR81892","CMR_200423164131007RiRR81705","CMR_210423101314491RiRR81776","CMR_210423113022294RiRR81893","CMR_210423111920100RiRR81880","CMR_200423164503687RiRR81706","CMR_200423164923666RiRR81707","CMR_210423112222675RiRR81883","CMR_210423105651688RiRR81852","CMR_210423105741290RiRR81854","CMR_210423101523881RiRR81778"]
for i in ek:
    driver.find_element(By.ID, "txtSearch").send_keys(i)
    driver.find_element(By.ID, "btn_Filter").click()
    driver.find_element(By.ID, "LnkDetails").click()

    driver.find_element(By.ID, "txt_Reason").send_keys("PASSED")

    driver.find_element(By.ID, "btnPassBill").click()
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    driver.switch_to.alert.accept()