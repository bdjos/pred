import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import os

PATH = os.getcwd()
app = dash.Dash()
df = pd.read_csv(f'{PATH}/predictions.csv', index_col='Date/Time')

app.layout = html.Div(children=[
    html.H1(children='Dash Tutorials'),
    dcc.Graph(
        id='example',
        figure={
            'data': [
                {'x': df.index, 'y': df['Predicted Demand'], 'type': 'line', 'name': 'Boats'},
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
