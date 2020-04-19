import requests
import sqlite3
import json

urlc="https://covidtracking.com/api/v1/states/current.json"
r = requests.get(urlc)
datac = json.loads(r.text) 
finalc=[]
for dict in datac:
    state=dict['state']
    positive=dict['positive']
    recovered=dict['recovered']
    death=dict['death']
    info=(state,positive,recovered,death)
    finalc.append(info)


urly = "https://coronavirus-19-api.herokuapp.com/countries"
payloady = {}
headersy= {}
responsey = requests.request("GET", urly, headers=headersy, data = payloady)
datay = responsey.json()

url = "https://api.covid19api.com/summary"

payload = {}
headers= {}

response = requests.request("GET", url, headers=headers, data = payload)
countryDict = response.json()

# set up the database tables
conn = sqlite3.connect('finalDB.db')
cur = conn.cursor()

#Chenyiyang
cur.execute('Create TABLE USstatescurrent (state TEXT, positive INTEGER, recovered INTEGER, death INTEGER)')
x=0
y=20
for num in range(0,len(finalc)//20):
    if num <len(finalc)//20:
        for ele in finalc[x:y]:
            cur.execute('INSERT INTO USstatescurrent (state,positive,recovered,death) VALUES (?,?,?,?)', (ele[0],ele[1],ele[2],ele[3]))
        x+=20
        y+=20
for ele in finalc[x:]:
    cur.execute('INSERT INTO USstatescurrent (state,positive,recovered,death) VALUES (?,?,?,?)', (ele[0],ele[1],ele[2],ele[3]))


#Yangzhixuan
cur.execute('''CREATE TABLE IF NOT EXISTS Covidinfo
            (Country TEXT UNIQUE, Cases INTEGER, Active INTEGER, Critical INTEGER, TestsPerOneMillion INTEGER)''')

cur.execute("SELECT * FROM Covidinfo")
if len(list(cur)) >= 100:
    cur.execute("DROP TABLE Covidinfo")
    cur.execute('''CREATE TABLE IF NOT EXISTS Covidinfo
            (Country TEXT UNIQUE, Cases INTEGER, Active INTEGER, Critical INTEGER, TestsPerOneMillion INTEGER)''')


count = 0
for dictionary in datay:
    Country = dictionary["country"]
    Cases = dictionary["cases"]
    Active= dictionary["active"]
    Critical = dictionary["critical"]
    TestsPerOneMillion=dictionary['testsPerOneMillion']

    while True:
        cur.execute("SELECT * FROM Covidinfo WHERE country = ?", (Country,))
        row = cur.fetchone()
        if row is None:
            cur.execute('INSERT INTO Covidinfo (Country, Cases, Active, Critical,TestsPerOneMillion) VALUES (?, ?, ?, ?, ?)',
            (Country, Cases, Active, Critical,TestsPerOneMillion))
            count = count + 1
            break
        else:
            break

    if count == 20:
        break

#Anna
cur.execute('''CREATE TABLE IF NOT EXISTS TotalByCountry
            (Country TEXT UNIQUE, TotalConfirmed INTEGER, TotalDeaths INTEGER, TotalRecovered INTEGER)''')
cur.execute('''CREATE TABLE IF NOT EXISTS NewByCountry
            (Country TEXT UNIQUE, NewConfirmed INTEGER, NewDeaths INTEGER, NewRecovered INTEGER)''')

cur.execute("SELECT * FROM TotalByCountry")
if len(list(cur)) >= 100:
    cur.execute("DROP TABLE TotalByCountry")
    cur.execute("DROP TABLE NewByCountry")
    cur.execute('''CREATE TABLE IF NOT EXISTS TotalByCountry
            (Country TEXT UNIQUE, TotalConfirmed INTEGER, TotalDeaths INTEGER, TotalRecovered INTEGER)''')
    cur.execute('''CREATE TABLE IF NOT EXISTS NewByCountry
            (Country TEXT UNIQUE, NewConfirmed INTEGER, NewDeaths INTEGER, NewRecovered INTEGER)''')




count = 0
for x in countryDict["Countries"]:
    c = x["Country"]
    tConfirm = x["TotalConfirmed"]
    tDeath = x["TotalDeaths"]
    tRecovered = x["TotalRecovered"]
    nConfirm = x["NewConfirmed"]
    nDeath = x["NewDeaths"]
    nRecovered = x["NewRecovered"]
    while True:
        cur.execute("SELECT * FROM TotalByCountry WHERE Country = ?", (c,))
        row = cur.fetchone()
        if row is None:
            cur.execute('INSERT INTO TotalByCountry (Country, TotalConfirmed, TotalDeaths, TotalRecovered) VALUES (?, ?, ?, ?)',(c, tConfirm, tDeath, tRecovered))
            cur.execute('INSERT INTO NewByCountry (Country, NewConfirmed, NewDeaths, NewRecovered) VALUES (?, ?, ?, ?)',(c, nConfirm, nDeath, nRecovered))
            count = count + 1
            break
        else:
            break
       
    if count == 20:
        break

conn.commit()

cur.close()



    
