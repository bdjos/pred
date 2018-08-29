# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 15:20:21 2018

@author: BJoseph
"""

import dash
from dash.dependencies import Output, Event
import dash_core_components as dcc
import dash_html_components as html
import plotly
import random
import plotly.graph_objs as go
from collections import deque
import predict
import pandas as pd

app = dash.Dash(__name__)
df = pd.read_csv('predictions.csv', index_col=['Date/Time'])

X = deque(maxlen = 20)
Y = deque(maxlen = 20)
X.append(1)
Y.append(1)

app.layout = html.Div(children = [
        html.H1('IESO Prediction'),
        dcc.Graph(id='live-graph',
                  animate=True),        
        dcc.Interval(
                id='graph-update',
                interval=1000
                )
        ])

@app.callback(Output('live-graph', 'figure'),
              events = [Event('graph-update', 'interval')])
def update_graph():
    global X
    global Y
    X.append(X[-1] + 1)
    Y.append(Y[-1] + (Y[-1]*random.uniform(-0.1, 0.1)))
    
    data = go.Scatter(
            x = list(X),
            y = list(Y),
            name = 'Scatter',
            mode = 'lines+markers'
            )
    return {'data': [data], 'layout': go.Layout(xaxis = dict(range=[min(X), max(X)]),
                                                yaxis = dict(range=[min(Y), max(Y)]))}


server = app.server

if __name__ == '__main__':
    app.run_server(debug=True)