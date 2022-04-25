from dash import Dash, dash_table, html, dcc
import plotly.express as px
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/solar.csv')

app = Dash(__name__)

fig1 = px.bar(df, x='State', y='Number of Solar Plants', color='State', barmode='group')
fig2 = px.scatter(df, x='State', y='Average MW Per Plant', color='State')
fig3 = px.bar(df, x='State', y=['Average MW Per Plant', 'Installed Capacity (MW)', 'Generation (GWh)'])

app.layout = html.Div(children=[
    html.H1(children='Solar Energy in the United State'),

    html.Div(children='''
        A static dashboard
    '''),
    dash_table.DataTable(df.to_dict('records'), [{"name": i, "id": i} for i in df.columns]),
    dcc.Graph(
        id='solar-graph',
        figure=fig1
    ),
    dcc.Graph(
        id='solar-cap-graph',
        figure=fig2
    ),
    dcc.Graph(
        id='solar-total-graph',
        figure=fig3
    )
])
if __name__ == '__main__':
    app.run_server(debug=True)