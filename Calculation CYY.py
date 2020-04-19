
import sqlite3
conn=sqlite3.connect('/Users/mac/Desktop/Final Project Yiyang.db')
#conn = sqlite3.connect('/Users/yzhixuan/Desktop/CoronavirusStopper/final1.db')
cur = conn.cursor()
#f = open("/Users/yzhixuan/Desktop/CoronavirusStopper/README.txt", "w")
f=open("/Users/Mac/Desktop/aaa.txt",'w')
cur.execute('SELECT state, positive, recovered, death From USstatescurrent')
data=[]
for row in cur:
    data.append(row)
print(data)
totalpositivecases=0
totaldeath=0
totalrecovered=0
for row in data:
    if row[1]!=None:
        totalpositivecases+=row[1]
    if row[3]!=None:
        totaldeath+=row[3]
    if row[2]!=None:
        totalrecovered+=row[2]
f.write("State distribution of positive cases:\n")
for row in data:
        f.write("State {} contains {} percent of total US positive cases.\n".format(row[0],100*row[1]/totalpositivecases))
f.write("US and each states death rate:\n")
f.write("US death rate of coronavirus is {} precent.\n".format(100*totaldeath/totalpositivecases))
for row in data:
    if row[3]!=None or 0:
        f.write("State {} death rate is {}\n".format(row[0],100*row[3]/row[1]))
    else:
        f.write("State {} death rate is unavailable".format(row[0]))
f.write("US and each states recover rate:\n")
f.write("US recover rate of coronavirus is {} percent.\n".format(100*totalrecovered/totalpositivecases))
for row in data:
    if row[2]!=None:
        f.write("State {} recover rate is {} percent.\n".format(row[0],100*row[2]/row[1]))
    else:
        f.write("State {} recover rate unavailable.\n".format(row[0]))
f.close()