import selenium

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service

import time

import csv

import unicodedata

from openpyxl import Workbook, load_workbook


import userInformation as usrI

"""
usrName = usrI.username
passW = usrI.password

service = Service()
option = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=option)

url = usrI.userURL
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
"""
######
workNames = usrI.testWorks
className = usrI.testClasses
classTime = usrI.testTimes
######

filePath = usrI.filePathXlsx
wb = load_workbook(filePath)
ws = wb.active
maxRows = ws.max_row
oldWorkNames = []
oldClassName = []
oldClassTime = []

#myworkbook=openpyxl.load_workbook()
#worksheet=myworkbook.wb('Sheet1')
for i in range(len(workNames)):
    workNames[i] = unicodedata.normalize("NFKD", workNames[i]).encode("ascii", "ignore")
    className[i] = unicodedata.normalize("NFKD", className[i]).encode("ascii", "ignore")
    classTime[i] = unicodedata.normalize("NFKD", classTime[i]).encode("ascii", "ignore")


"""
            try:
            ws['B'+ str(i+1)] = str(textWork)
            ws['C'+ str(i+1)] = str(textClass)
            ws['D'+ str(i+1)] = str(textTime)
            #cellref=worksheet.cell(row=i, column=4) cellref.value=
        except:
            print("oops with the xlsx")
"""
#wb2 = Workbook()
wb.save(filePath)
#'D:\VSCODE_Programmes\Projects\Lists\prr\data2.xlsx'
wb.close()

"""
homeworks = []
time.sleep(1)
for data in range(workNames):
    homeworks.append(workNames[data]+','+className[data]+','+classTime[data])
"""

"""
filepathcsv = usrI.filePathcsv
with open(, 'w', newline='') as csvF:
    file = csv.writer(csvF, delimiter="$")
    for i in range(len(homeworks)):
        print("doeshappen")
        try:
            file.writerow(homeworks[i])
        except:
            try:
                file.writerow(unicodedata.normalize('NFKD',homeworks[i]).encode("ascii", 'ignore'))
            except:
                print("noneOfThemWorkError")
        else:
            print("text was encoded")

csvF.close()

for texts in classTime:
    print(texts.text)

for texts in className:
    print(texts.text)

for texts in workNames:
    print(texts.text)
"""


#input()
#driver.close()

