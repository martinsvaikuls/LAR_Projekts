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
### Datu iegūšana 

1. selenium
Selenium tika lietots, jo vajag ielogoties saitē, ko ar BeautifulSoup 4 nav iespējams darīt
Selenium pārvietojas pa tīmekli un spēj atrast html elementus pēc Xpath, klasēm, id, attribūtiem, ar ko varēja atrast mājas darbu datus

### Datu saglabāšana

2. openpyxl
Ar openpyxl bibliotēku var apstrādāt .xlsx failus, kur tika saglabāti mājas darbu dati kā arī vēlāk nolasīti

### Darbības ar aplikāciju

3. pywinauto
pywinauto nebija iespējas daudz lietot, jo mana izvēlētā lietotne nevar būt manipulēta ar pywinauto bibliotēku,
šī bibliotēka tika lietota, lai atvērtu pašu aplikāciju un lietotu peli un klaviatūru

4. pyautogui
Šī bibliotēka tika lietota, lai apskatītos kuras lietotnes šobrīd ir atvērtas, lai zinātu vai vajag atvērt telegram aplikāciju

5. win32gui
bibliotēka tiek lietota lai mijiedarbotos ar Windows OS 
ar šo bibliotēku programma pārvietoja un palielināja telegram aplikāciju

### Palīgbibliotēkas

6. sys
Ja telegram aplikācija neveras vaļā, tad programma pārstāj darboties sys.exit()

7. time
bibliotēka tika lietota lai programma "pagaidītu" līdz atveras vietnes un telegram aplikācija, kā arī laiks tiek apskatīts lai programma nedarbotos visu laiku.

8. userInformation
Tā nav īsti bibliotēka, bet vieta kur saglabāt lietotāja informāciju, piem., paroli, lietvārdu, path uz dokumentiem.


## Programmas izmantošana
1. Izlasīt esošās nepilnības kodā
2. Izveidot jaunu .xlsx failu
3. Izveidot un ievadīt lietotāja informāciju "bibliotēkā" userInformation.py, kura atrodas tajā pašā mapē, kur atrodas main.py
4. Aplikācijā telegram novietot terzēšanas saraksti kā pirmo no rindām, ja tajā vēlams nosūtīt informāciju.
5. Telegram saskarne (angļu val. interface) ir uz 125%
6. Uzsākt programmu un aiziet uztaisīt tēju/kafiju (programma aizņem ~3min)


### Video, kur norādīts kā programma strādā
https://youtu.be/LVsoKAMpAGs

## Esošās kļūdas/nepilnības kodā!
  - Nav zināms, kā programma darbosies ja lietotājs vēlās lietot citu aplikāciju
  - Paziņojums tiek nosūtīts uz 1. saraksti Telegram aplikācijā
  - Paziņojums tiek nosūtīts ļoti lēni
  - Ja telegram ir atvērts un citas vietnes ir priekšplānā tad tajā netiks ievietota informācija
  - Dati tiek saglabāti tikai xlsx (vajadzētu pievienot .txt)
  - Tiek lietots userInformation.py nevis config fails

## Iespējamie papildinājumi!
  - Lietotājs var izvēlēties, lai programma nerādītu līdz kuram datumam, bet cik dienas ir palikušas no šīs dienas.
  - Programma pārbauda, vai mājas darbs jau ir izpildīts, ja tas ir tad to nenorāda.
  - Programma ar kuras palīdzību var nosūtīt mājas darbus.
  - Programma saīsina kursu nosaukumus uz lietotāja dotajiem
  - ...
