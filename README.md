# Automatizācijas projekts
## Projekta uzdevums
Projekta uzdevums ir izveidot kodu, kurš automatizēs vienu no maniem ikdienas uzdevumiem.
Ideja: Izveidot kodu kurš paziņos par jaunajiem mājas darbiem.
Idejas koda izveidošanas plāns:
  - Programmai vajag iegūt informāciju par esošajiem mājas darbiem
    - Uzzināt un pielietot efektīvāko ceļu informācijas iegūšanai
  - Salīdzināt iegūtos datus ar iepriekš zināmajiem datiem (kur dati ir mājas darbi)
  - Saglabāt jaunos datus .xlsx failā
  - Atvērt lietotni (Telegram)
    - Paziņot jaunos mājas darbus
    - Atgādināt par vecajiem mājas darbiem
  Programmas darbības pabeigtas

## Lietotās python bibliotēkas
#Datu iegūšana 
1. selenium
Selenium tika lietots, jo vajag ielogoties saitē, ko ar BeautifulSoup 4 nav iespējams darīt
Selenium pārvietojas pa tīmekli un spēj atrast html elementus pēc Xpath, klasēm, id, attribūtiem, ar ko varēja atrast mājas darbu datus

#Datu saglabāšana
3. openpyxl
Ar openpyxl bibliotēku var apstrādāt .xlsx failus, kur tika saglabāti mājas darbu dati kā arī vēlāk nolasīti

#Darbības ar aplikāciju
3. pywinauto
pywinauto nebija iespējas daudz lietot, jo mana izvēlētā lietotne nevar būt manipulēta ar pywinauto bibliotēku,
šī bibliotēka tika lietota tikai lai atvērtu pašu aplikāciju

4. pyautogui

5. win32api
ar win32api bibliotēku

7. win32gui

#Palīgbibliotēkas
7. sys

8. time

9. userInformation


## Programmas izmantošana

### Video, kur norādīts kā programma strādā


## Esošie kļūdas (angļu val. bugs) kodā!
Lietojot pywinauto vismaz, kā tika uzzināts nav iespējam manipulēt ar lietotni "Telegram", tāpēc programma nav dinamiska, bet statiska, lietotnei "Telegram" vajag atrasties kreisajā stūrī un 
