import selenium

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service

import time

from openpyxl import Workbook
from openpyxl import load_workbook

import userInformation as usrI
usrName = usrI.username
passW = usrI.password

service = Service()
option = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=option)

url = "https://id2.rtu.lv/openam/UI/Login?locale=lv&goto=https%3A%2F%2Festudijas.rtu.lv"
driver.get(url)
time.sleep(1)

#ievada lietotaj vardu
find = driver.find_element(By.ID, "IDToken1")
find.send_keys(usrName)

#ievada paroli
find = driver.find_element(By.ID, "IDToken2")
find.send_keys(passW)
#input()
#"Pieteikties" -> Enter
find.send_keys('\ue007')
time.sleep(5)
#input()
find = driver.find_element(By.CLASS_NAME, "gotocal")
find.click()
time.sleep(5)

workNames = driver.find_elements(By.CLASS_NAME, "name.d-inline-block")
classTime = driver.find_elements(By.XPATH, "//div[@class='row']/div[@class='col-11']")
className = driver.find_elements(By.XPATH, "//div[@class='row mt-1']/div[@class='col-11']/a")

time.sleep(1)

for texts in classTime:
    print(texts.text)

for texts in className:
    print(texts.text)

for texts in workNames:
    print(texts.text)





input()
driver.close()

