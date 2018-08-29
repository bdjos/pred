import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

app = dash.Dash()
df = pd.read_csv('predictions.csv', index_col=['Date/Time']
x = pd.index
y = df['Predicted Demand']

app.layout = html.Div(children=[
    html.H1(children='Dash Tutorials'),
    dcc.Graph(
        id='example',
        figure={
            'data': [
                {'x': x, 'y': y, 'type': 'line', 'name': 'Boats'}
            ],
            'layout': {
                'title': 'Basic Dash Example'
            }
        }
    )
])

server = app.server

if __name__ == '__main__':
    print(x)
    print(y)
