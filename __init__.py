import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

app = dash.Dash()
x = [1,2,3]
y = [10,11,12]

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
    app.run_server(debug=True)
