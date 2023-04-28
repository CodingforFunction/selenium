import math
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

ek =["CMR_090123094005886RiRR12843","CMR_090123094307899RiRR12844","CMR_090123094520822RiRR12847","CMR_090123094710505RiRR12851","CMR_090123095043109RiRR12854","CMR_090123095351611RiRR12857","CMR_090123095900475RiRR12862","CMR_090123100620170RiRR12876","CMR_090123101309621RiRR12884","CMR_090123101621678RiRR12887","CMR_090123102906536RiRR12901","CMR_090123103220793RiRR12908","CMR_090123103626943RiRR12916","CMR_090123104119770RiRR12922","CMR_090123104928029RiRR12940","CMR_090123105422490RiRR12957","CMR_090123105653068RiRR12964","CMR_090123104537245RiRR12929","CMR_090123105125234RiRR12948","CMR_090123094854634RiRR12853","CMR_090123095626648RiRR12858","CMR_090123095853038RiRR12861","CMR_090123102926321RiRR12902","CMR_090123103104602RiRR12906","CMR_090123103228435RiRR12909","CMR_090123110514839RiRR12983","CMR_090123103543048RiRR12915","CMR_090123104046064RiRR12920","CMR_090123104511713RiRR12928","CMR_090123110310507RiRR12978","CMR_090123110955477RiRR12991","CMR_090123104459744RiRR12927","CMR_090123104711695RiRR12935","CMR_090123104931076RiRR12941","CMR_090123105049125RiRR12946","CMR_090123105156254RiRR12950","CMR_090123105312887RiRR12955","CMR_090123105455525RiRR12958","CMR_090123105604611RiRR12962","CMR_090123105714528RiRR12965","CMR_090123105851931RiRR12969","CMR_090123110029382RiRR12971","CMR_090123110219999RiRR12976","CMR_090123110440831RiRR12982","CMR_090123110557240RiRR12985","CMR_090123110823280RiRR12989","CMR_090123111129083RiRR12994","CMR_090123111310108RiRR12997","CMR_090123111424613RiRR13001","CMR_090123105142002RiRR12949","CMR_090123105421646RiRR12956","CMR_090123105758261RiRR12967","CMR_090123110108544RiRR12973","CMR_090123110525857RiRR12984","CMR_090123111147042RiRR12995","CMR_090123111401700RiRR12998","CMR_090123111706860RiRR13006","CMR_090123112302617RiRR13010","CMR_090123112454637RiRR13012","CMR_090123112648134RiRR13013","CMR_090123112829992RiRR13014","CMR_090123113015477RiRR13017","CMR_090123113214041RiRR13022","CMR_090123121630980RiRR13042","CMR_090123121923263RiRR13044","CMR_090123122246158RiRR13048","CMR_090123113609676RiRR13027","CMR_090123113833307RiRR13029","CMR_090123114104940RiRR13031"]
msp = 3074.62

opt = Options()
opt.add_experimental_option("debuggerAddress", "Localhost:9125")
driver = webdriver.Chrome(executable_path="D:\\KVS\\drivers\\chromedriver_win32\\chromedriver.exe", chrome_options=opt)
driver.get("https://ekharid.haryana.gov.in/FCI/CMR_AA_BillMgmt")

for i in ek:
    driver.find_element(By.ID, "txtSearch").send_keys(i)
    driver.find_element(By.ID, "btn_Filter").click()
    driver.find_element(By.ID, "LnkDetails").click()

    weight1 = driver.find_element(By.ID, "ContentPlaceHolder1_grd_Heads_lbl_NetWeight_0").text
    weight2 = float(weight1)
    agency = driver.find_element(By.ID, "ContentPlaceHolder1_lbl_Agency").text

    if (weight2 > 291):
        truck = math.ceil(weight2 / 290)
    else:
        truck = 1
    gross = weight2 * msp
    tds = math.ceil(gross * 0.001)
    # paid1 = gross - 120 * truck #for DFSC
    # paid2 = gross - 120 * truck - tds #for HAFED
    if (agency == "FOOD AND SUPPLY"):
        paid = gross - 120 * truck
    else:
        paid = gross - 120 * truck - tds
    driver.find_element(By.ID, "ContentPlaceHolder1_grd_Heads_lbl_PassedAmount_0").send_keys(Keys.CONTROL+"A")

    driver.find_element(By.ID, "ContentPlaceHolder1_grd_Heads_lbl_PassedAmount_0").send_keys(paid)
    driver.find_element(By.ID, "ContentPlaceHolder1_grd_Heads_lbl_PassedAmount_0").send_keys(Keys.TAB)

    driver.find_element(By.ID, "txt_Reason").send_keys("PASSED")

    driver.find_element(By.ID, "btnPassBill").click()
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    driver.switch_to.alert.accept()