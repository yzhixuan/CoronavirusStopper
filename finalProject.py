import requests
import sqlite3

url = "https://api.covid19api.com/summary"

payload = {}
headers= {}

response = requests.request("GET", url, headers=headers, data = payload)
countryDict = response.json()

# set up the database tables
conn = sqlite3.connect('finalDB.db')
cur = conn.cursor()
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



    
