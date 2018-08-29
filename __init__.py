# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 15:20:21 2018

@author: BJoseph
"""

import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import predict
import pandas as pd

app = dash.Dash()
df = pd.read_csv('predictions.csv', index_col=['Date/Time'])


app.layout = html.Div(children = [
        html.H1('IESO Prediction'),
        dcc.Graph(id='example',
                  figure ={
                          'data': [
                                  {'x': df.index, 'y': df['Predicted Demand'], 'type': 'line', 'name': 'Demand'}
                          ],
                          'layout': {
                                  'title': 'Basic Dash Example'
                                  }
                  })
        ])

#@app.callback(
#        Output(component_id='output', component_property='children'),
#        [Input(component_id='input', component_property='value')])
#def update_value(input_data):
#    return "Input: {}.format(input_data)"

server = app.server

if __name__ == '__main__':
    app.run_server(debug=True)