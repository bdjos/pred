import plotly
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import os
import pandasdb

db_name = 'bjos'
table_name = 'forecast2'
uname = 'bjos'
apikey = 'xkic7PUmF2h6l4lVKo9c'

plotly.tools.set_credentials_file(username=uname, api_key=apikey)

db = pandasdb.pandasdb(db_name, table_name)
df = db.pd_from_db()

app = dash.Dash()

app.layout = html.Div(children=[
    html.H1(children='Ontario Demand Prediction'),
    dcc.Graph(
        id='example',
        figure={
            'data': [
                {'x': df['Date/Time'], 'y': df['Predicted Demand'], 'type': 'line', 'name': 'Predicted Demand'}
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
