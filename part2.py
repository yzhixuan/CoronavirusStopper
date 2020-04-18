import requests
import sqlite3

url = "https://coronavirus-19-api.herokuapp.com/countries"

payload = {}
headers= {}

response = requests.request("GET", url, headers=headers, data = payload)
data = response.json()

# set up the database tables
conn = sqlite3.connect('/Users/yzhixuan/Desktop/final project/final1.db')
cur = conn.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS Covidinfo
            (Country TEXT UNIQUE, Cases INTEGER, Active INTEGER, Critical INTEGER, TestsPerOneMillion INTEGER)''')

cur.execute("SELECT * FROM Covidinfo")
if len(list(cur)) >= 100:
    cur.execute("DROP TABLE Covidinfo")
    cur.execute('''CREATE TABLE IF NOT EXISTS Covidinfo
            (Country TEXT UNIQUE, Cases INTEGER, Active INTEGER, Critical INTEGER, TestsPerOneMillion INTEGER)''')
    

count = 0
for dictionary in data:
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

conn.commit()

cur.close()