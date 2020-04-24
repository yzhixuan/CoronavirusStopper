import plotly.graph_objects as go
import sqlite3

conn = sqlite3.connect('finalDB.db')
cur = conn.cursor()
cur.execute("SELECT * FROM TotalByCountry WHERE TotalConfirmed > 10000")
result = cur.fetchall()
countryList = []
confirmedList = []
for x in result:
    countryList.append(x[0])
    confirmedList.append(x[1])

fig = go.Figure(data=[go.Pie(labels=countryList, values=confirmedList, textinfo='label+percent')])
fig.show()

