import plotly.express as px
import sqlite3

cconn = sqlite3.connect('finalDB.db')
cur=conn.cursor()
cur.execute('SELECT state, positive, recovered, death From USstatescurrent')
states=[]
positive=[]

for row in cur:
    states.append(row[0])
    positive.append(row[1])



#fig = px.choropleth(locations=states, locationmode="USA-states", color=positive , scope="usa")
#fig.show()
import plotly.graph_objects as go

# Load data frame and tidy it.
import pandas as pd
#df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2011_us_ag_exports.csv')

fig = go.Figure(data=go.Choropleth(
    locations=states, # Spatial coordinates
    z = positive, # Data to be color-coded
    locationmode = 'USA-states', # set of locations match entries in `locations`
    colorscale = 'Reds',
    colorbar_title = "positive cases",
))

fig.update_layout(
    title_text = 'Poitive cases of Coronavirus in states on April 22nd',
    geo_scope='usa', # limite map scope to USA
)

fig.show()
