# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 15:20:21 2018

@author: BJoseph
"""

import dash
import dash_core_components as dcc
import dash_html_components as html
import predict
import pandas as pd

app = dash.Dash()
df = predict.predict()


app.layout = html.Div(children = [
        html.H1('Dash Tutorials'),
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

if __name__ == '__main__':
    app.run_server()