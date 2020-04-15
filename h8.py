import json
import requests
import sqlite3

try:
    url="https://covidtracking.com/api/v1/states/current.json"
    r = requests.get(url,state='MI')
    data = json.loads(r.text) 
except:
    print("error when reading from url")
    data = {}
final=[]
for dict in data:
    state=dict['state']
    positive=dict['positive']
    recovered=dict['recovered']
    death=dict['death']
    info=(state,positive,recovered,death)
    final.append(info)
    date=dict["lastUpdateEt"]
conn=sqlite3.connect('/Users/mac/Desktop/Final Project Yiyang.db')
cur=conn.cursor()
try:
    cur.execute('Create TABLE USstates (states TEXT, positive INTEGER, recovered INTEGER, death INTEGER)')
except:
    print("Table USstates already exists")
for ele in final:
    cur.execute('INSERT INTO USstates (states, positive, recovered, death) VALUES (?,?,?,?)', (ele[0],ele[1],ele[2],ele[3]))
conn.commit()
print("USstates: ")
cur.execute('SELECT states, positive, recovered, death From USstates')
for row in cur:
    print(row)
cur.close()
