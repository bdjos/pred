
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import os
import sys

PATH = '/var/www/FlaskApp/pred'

if PATH not in sys.path:
    sys.path.insert(0, PATH)
    
import pandasdb

db_name = 'bjos'
table_name = 'forecast2'
#uname = 'bjos'
#apikey = 'xkic7PUmF2h6l4lVKo9c'
#
#plotly.tools.set_credentials_file(username=uname, api_key=apikey)

db = pandasdb.pandasdb(db_name, table_name)
df = db.pd_from_db()

app = dash.Dash()

app.layout = html.Div(children=[
    html.H1(children='Dash Tutorials'),
    dcc.Graph(
        id='example',
        figure={
            'data': [
                {'x': df['Date/Time'], 'y': ['Predicted Demand'], 'type': 'line', 'name': 'Boats'}
            ],
            'layout': {
                'title': 'Basic Dash Example'
            }
        }
    )
])

server = app.server

if __name__ == '__main__':
    app.run_server(debug=True)
