
import sqlite3

conn = sqlite3.connect('finalDB.db')
cur = conn.cursor()
f = open("CalculationOutput.txt", "w")

cur.execute("SELECT * FROM TotalByCountry")
f.write("Total Number of Country: %d \n" % len(list(cur)))

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
