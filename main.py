import selenium

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service

import time

service = Service()
option = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=option)

url = "https://id2.rtu.lv/openam/UI/Login?locale=lv&goto=https%3A%2F%2Festudijas.rtu.lv"
driver.get(url)
time.sleep(1)

#ievada lietotaj vardu
find = driver.find_element(By.ID, "IDToken1")
find.send_keys("LietVards")

#ievada paroli
find = driver.find_element(By.ID, "IDToken2")
find.send_keys("Parole")
#input()
#"Pieteikties" -> Enter
find.send_keys('\ue007')
time.sleep(5)
#input()
find = driver.find_element(By.CLASS_NAME, "gotocal")
find.click()
time.sleep(5)
#find = driver.find_element(By.CLASS_NAME, "name.d-inline-block")
timeClass = []
workNames = driver.find_elements(By.CLASS_NAME, "name.d-inline-block")
"""
timeClassBefore = driver.find_elements(By.CLASS_NAME, "col-11")

for elem in timeClassBefore:
    timeClass.append(elem.find_elements(By.TAG_NAME, "a"))
"""
trial = driver.find_elements(By.CLASS_NAME, "row.col-11")
trial2 = driver.find_elements(By.CLASS_NAME, "row.row.col-11")

#timeClass = timeClassBefore.find_elements(By.TAG_NAME, "a")
"""
for elem in timeClassBefore:
    timeClass.append(elem.get_attribute("a"))
    try:
        print(elem.get_attribute("a"))
    except:
        print("NoneType")
"""
time.sleep(1)
for texts in workNames:
    print(texts.text)

for texts in trial:
    print(texts.text)

for texts in trial2:
    print(texts.text)

"""
for texts in timeClass:
    for elemz in texts:
        try:
            print(elemz.text)
        except:
            print(elemz)
"""
input()
driver.close()
