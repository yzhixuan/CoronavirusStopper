
import sqlite3

conn = sqlite3.connect('finalDB.db')
cur = conn.cursor()
f = open("CalculationOutput.txt", "w")

cur.execute("SELECT * FROM TotalByCountry")
f.write("Total Number of Country: %d \n" % len(list(cur)))

#Chenyiyang
cur.execute('SELECT state, positive, recovered, death From USstatescurrent')
data=[]
for row in cur:
    data.append(row)
#print(data)
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


cur.execute("SELECT * FROM TotalByCountry WHERE TotalConfirmed > 10000")
f.write("Country with more than 10000 confirmed cases: %d \n" % len(list(cur)))
cur.execute("SELECT * FROM TotalByCountry WHERE TotalConfirmed > 5000")
f.write("Country with more than 5000 confirmed cases: %d \n" % len(list(cur)))
cur.execute("SELECT * FROM TotalByCountry WHERE TotalConfirmed > 2000")
f.write("Country with more than 2000 confirmed cases: %d \n" % len(list(cur)))
cur.execute("SELECT * FROM TotalByCountry WHERE TotalConfirmed > 1000")
f.write("Country with more than 1000 confirmed cases: %d \n \n" % len(list(cur)))

cur.execute("SELECT * FROM TotalByCountry WHERE TotalDeaths > 5000")
f.write("Country with more than 5000 deaths: %d \n" % len(list(cur)))
cur.execute("SELECT * FROM TotalByCountry WHERE TotalDeaths > 2000")
f.write("Country with more than 2000 deaths: %d \n" % len(list(cur)))
cur.execute("SELECT * FROM TotalByCountry WHERE TotalDeaths > 1000")
f.write("Country with more than 1000 deaths: %d \n" % len(list(cur)))
cur.execute("SELECT * FROM TotalByCountry WHERE TotalDeaths > 500")
f.write("Country with more than 500 deaths: %d \n \n" % len(list(cur)))

cur.execute("SELECT * FROM TotalByCountry WHERE TotalRecovered > 10000")
f.write("Country with more than 10000 recovered cases: %d \n" % len(list(cur)))
cur.execute("SELECT * FROM TotalByCountry WHERE TotalRecovered > 5000")
f.write("Country with more than 5000 recovered cases: %d \n" % len(list(cur)))
cur.execute("SELECT * FROM TotalByCountry WHERE TotalRecovered > 2000")
f.write("Country with more than 2000 recovered cases: %d \n" % len(list(cur)))
cur.execute("SELECT * FROM TotalByCountry WHERE TotalRecovered > 1000")
f.write("Country with more than 1000 recovered cases: %d \n \n" % len(list(cur)))

cur.execute('''SELECT * FROM TotalByCountry JOIN NewByCountry ON TotalByCountry.Country = NewByCountry.Country WHERE TotalConfirmed > 10000''')
result = cur.fetchall()
for x in result:
    f.write("Country with more than 10000's today's confirmed rate: %f \n" % (float(x[5])/x[1]))




f.close()
