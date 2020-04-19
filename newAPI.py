import requests
import sqlite3

url = "https://coronavirus-19-api.herokuapp.com/countries"

payload = {}
headers= {}

response = requests.request("GET", url, headers=headers, data = payload)
data = response.json()

# set up the database tables
conn = sqlite3.connect('/Users/yzhixuan/Desktop/final project1.db')
cur = conn.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS Covid19
            (Country TEXT UNIQUE, TodayCases INTEGER, TodayDeaths INTEGER, Critical INTEGER)''')

cur.execute("SELECT * FROM Covid19")
if len(list(cur)) >= 100:
    cur.execute("DROP TABLE Covid19")
    cur.execute('''CREATE TABLE IF NOT EXISTS Covid19
            (Country TEXT UNIQUE, TodayCases INTEGER, TodayDeaths INTEGER, Critical INTEGER)''')
    

count = 0
for dictionary in data:
    Country = dictionary["country"]
    TodayCases= dictionary["todayCases"]
    TodayDeaths = dictionary["todayDeaths"]
    Critical = dictionary["critical"]
    
    while True:
        cur.execute("SELECT * FROM Covid19 WHERE country = ?", (Country,))
        row = cur.fetchone()
        if row is None:
            cur.execute('INSERT INTO Covid19 (Country, TodayCases, TodayDeaths, Critical) VALUES (?, ?, ?, ?)',(Country, TodayCases, TodayDeaths, Critical))
            count = count + 1
            break
        else:
            break
       
    if count == 20:
        break

conn.commit()

cur.close()