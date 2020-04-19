import json
import requests
import sqlite3

try:
    url="https://covidtracking.com/api/v1/states/daily.json"
    r = requests.get(url)
    data = json.loads(r.text) 
except:
    print("error when reading from url")
    data = {}
final=[]
for dict in data:
    if dict['date']>20200410:
        state=dict['state']
        positive=dict['positive']
        try:
            recovered=dict['recovered']
        except:
            recovered=0
        try:
            death=dict['death']
        except:
            death=0
        positiveIncrease=dict['positiveIncrease']
        date=dict['date']
        info=(state,date,positive,recovered,death,positiveIncrease)
        final.append(info)
conn=sqlite3.connect('/Users/mac/Desktop/Final Project Yiyang.db')
cur=conn.cursor()
try:
    cur.execute('Create TABLE USstatesrecords (state TEXT, date INTEGER, positive INTEGER, recovered INTEGER, death INTEGER, positiveIncrease INTEGER)')
except:
    print("Table USstatesrecords already exists")
x=0
y=20
for num in range(0,len(final)//20):
    if num <len(final)//20:
        for ele in final[x:y]:
            cur.execute('INSERT INTO USstatesrecords (state,date,positive,recovered,death,positiveIncrease) VALUES (?,?,?,?,?,?)', (ele[0],ele[1],ele[2],ele[3],ele[4],ele[5]))
        x+=20
        y+=20
for ele in final[x:]:
    cur.execute('INSERT INTO USstatesrecords (state,date,positive,recovered,death,positiveIncrease) VALUES (?,?,?,?,?,?)', (ele[0],ele[1],ele[2],ele[3],ele[4],ele[5]))
conn.commit()
cur.execute('SELECT state,date,positive,recovered,death,positiveIncrease From USstatesrecords')
for row in cur:
    print(row)
cur.close()
