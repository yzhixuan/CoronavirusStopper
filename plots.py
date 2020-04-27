import requests
import sqlite3
import json
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

conn = sqlite3.connect('finalDB.db')
cur = conn.cursor()

top_4_countries = []
total = []
active_num = []
critical_num = []

result = cur.execute("SELECT * FROM Covidinfo WHERE NOT Country = 'USA' AND (TestsPerOneMillion > 0) ORDER BY Critical DESC LIMIT 4")
for row in result:
    top_4_countries.append(row[0])
    total.append(row[1])
    active_num.append(row[2])
    critical_num.append(row[3])

fig = plt.figure(figsize = (10,5))
ax1 = fig.add_subplot(131,facecolor='lightblue')
ax2 = fig.add_subplot(132,facecolor='lightblue')
ax3 = fig.add_subplot(133,projection="polar",facecolor='lightblue')
ax1.bar(top_4_countries,total)
ax2.bar(top_4_countries,active_num)
ax3.bar(top_4_countries,critical_num)
ax1.title.set_text('Number of Total Cases')
ax2.title.set_text('Number of Active Cases')
ax3.title.set_text('Number of Critical Cases')
ax1.tick_params(axis='y', labelsize=6)
ax2.tick_params(axis='y', labelsize=6)
ax3.tick_params(axis='y', labelsize=6)
plt.show()


cur.close()