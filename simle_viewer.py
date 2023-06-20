import dash_bootstrap_components as dbc
from dash import dash, html, dcc, dash_table
import plotly.express as px

app = dash.Dash(external_stylesheets=[dbc.themes.FLATLY])

import pandas as pd
df_sample = pd.read_csv("sample.csv")

header = html.Div(
    [
        dbc.Row(
            [
                html.H3("Simple Viewer", style={"margin-top":"12px", "margin-bottom":"12px", "margin-left":"24px"}
                ),
            ],
            className="bg-primary text-white font-italic"
        )
    ]
)

contents_points_analysis = html.Div(
    [
        dbc.Row(
            [
                html.H4("得点分析",
                        style={"margin-top":"24px","margin-left": "24px"},),
            ],
            className="bg-white",
        ),
        dbc.Row(
            [
                dbc.Col(
                    dcc.Graph(figure=px.bar(df_sample, x="term", y="point", color="aaxx", barmode="relative", color_discrete_map={"Alice":"lightcyan", "Bob":"cyan", "Cart":"royalblue"})),
                    width=7,
                ),
                dbc.Col(
                    dcc.Graph(figure=px.pie(df_sample, values="point", names="aaxx", color="aaxx", color_discrete_map={"Alice":"lightcyan", "Bob":"cyan", "Cart":"royalblue"})),
                    width=3,
                ),
            ],
            justify="center",
            className="bg-white"
        ),
    ],
    style={"border":"1px black solid"}
)

contents_accuracy_analysis = html.Div(
    [
        
        dbc.Row(
            [
                html.H4("得点推移",
                        style={"margin-top":"24px","margin-left": "24px"},),
            ],
            className="bg-white"
        ),
        dbc.Row(
            [
                dbc.Col(
                    dcc.Graph(figure=px.line(df_sample, x="term", y="point", color="aaxx", color_discrete_map={"Alice":"lightcyan", "Bob":"cyan", "Cart":"royalblue"})),
                    width=5,
                ),
                dbc.Col(
                    dcc.Graph(figure=px.line(df_sample, x="term", y="point", color="aaxx", color_discrete_map={"Alice":"lightcyan", "Bob":"cyan", "Cart":"royalblue"})),
                    width=5,
                ),
            ],
            justify="center",
            className="bg-white"
        ),
    ],
    style={"border":"1px black solid"}
)

app.layout = dbc.Container(
    [
        header,
        contents_points_analysis,
        contents_accuracy_analysis,
    ],
    fluid=True
)

if __name__ == "__main__":
    app.run_server(debug=True, port=1234)