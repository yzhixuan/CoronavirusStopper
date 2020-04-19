import json
import requests
import sqlite3

try:
    url="https://covidtracking.com/api/v1/states/current.json"
    r = requests.get(url)
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
    
conn=sqlite3.connect('/Users/mac/Desktop/Final Project Yiyang.db')
cur=conn.cursor()
try:
    cur.execute('Create TABLE USstatescurrent (state TEXT, positive INTEGER, recovered INTEGER, death INTEGER)')
except:
    print("Table USstatescurrent already exists")
x=0
y=20
for num in range(0,len(final)//20):
    if num <len(final)//20:
        for ele in final[x:y]:
            cur.execute('INSERT INTO USstatescurrent (state,positive,recovered,death) VALUES (?,?,?,?)', (ele[0],ele[1],ele[2],ele[3]))
        x+=20
        y+=20
for ele in final[x:]:
    cur.execute('INSERT INTO USstatescurrent (state,positive,recovered,death) VALUES (?,?,?,?)', (ele[0],ele[1],ele[2],ele[3]))
conn.commit()
print("USstates: ")
cur.execute('SELECT state, positive, recovered, death From USstatescurrent')
for row in cur:
    print(row)
cur.close()
