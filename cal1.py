import part2
import sqlite3

conn = sqlite3.connect('/Users/yzhixuan/Desktop/CoronavirusStopper/final1.db')
cur = conn.cursor()
f = open("/Users/yzhixuan/Desktop/CoronavirusStopper/README.txt", "w")

cur.execute("SELECT * FROM Covidinfo WHERE Active> 10000")
f.write("Country with over 2000 people actively ill: %d \n" % len(list(cur)))
cur.execute("SELECT * FROM Covidinfo WHERE Active> 5000")
f.write("Country with over 1000 people actively ill: %d \n" % len(list(cur)))
cur.execute("SELECT * FROM Covidinfo WHERE Active> 100")
f.write("Country with over 100 people actively ill: %d \n" % len(list(cur)))

cur.execute("SELECT * FROM Covidinfo WHERE Critical> 2000")
f.write("Country with over 2000 people critically ill: %d \n" % len(list(cur)))
cur.execute("SELECT * FROM Covidinfo WHERE Critical> 1000")
f.write("Country with over 1000 people critically ill: %d \n" % len(list(cur)))
cur.execute("SELECT * FROM Covidinfo WHERE Critical> 100")
f.write("Country with over 100 people critically ill: %d \n" % len(list(cur)))

cur.execute("SELECT CAST(Critical AS float)/CAST(Cases AS float) AS Rate FROM Covidinfo WHERE Rate > 0.1")
f.write("Country with over 10 percent patients critically ill: %d \n" % len(list(cur)))
cur.execute("SELECT CAST(Critical AS float)/CAST(Cases AS float) AS Rate FROM Covidinfo WHERE Rate > 0.05")
f.write("Country with over 5 percent patients critically ill: %d \n" % len(list(cur)))
cur.execute("SELECT CAST(Critical AS float)/CAST(Cases AS float) AS Rate FROM Covidinfo WHERE Rate > 0.005")
f.write("Country with over 0.5 percent patients critically ill: %d \n" % len(list(cur)))

cur.execute("SELECT * FROM Covidinfo WHERE TestsPerOneMillion > 10000")
f.write("Country where every one million people there are over 10000 tested: %d \n" % len(list(cur)))
cur.execute("SELECT * FROM Covidinfo WHERE TestsPerOneMillion > 5000")
f.write("Country where every one million people there are over 5000 tested: %d \n" % len(list(cur)))
cur.execute("SELECT * FROM Covidinfo WHERE TestsPerOneMillion > 1000")
f.write("Country where every one million people there are over 1000 tested: %d \n" % len(list(cur)))

f.close()