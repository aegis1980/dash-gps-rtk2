import json
import time

import dash
import dash_bootstrap_components as dbc
import numpy as np
import pandas as pd
from dash import Input, Output, State, ctx, dcc, html
from dash.exceptions import PreventUpdate
import dash_app
from dash_app import (LayoutID, layout)



#my_bcm = caching.background_callback_manager()

app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    #background_callback_manager=my_bcm,
    index_string=dash.dash._default_index.replace('<html>', '<html lang="en" prefix="og: http://ogp.me/ns#">'),
    meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1"},
        {"property" : "og:title", "content": "Glass Explore"},
        {"name":"image" ,  "property":"og:image" ,  "content":"https://floatingintheclouds.com/wp-content/uploads/2022/09/glass-explore.png" },
        {"name":"author" ,  "content":"Jon Robinson" },
        {"property" : "og:description", "content": OG_DESCRIPTION},
        {"property" : "og:url", "content": dash_app.OG_URL}
    ],
)

app.layout = html.Div([
    dcc.Location(LayoutID.URL),
    layout.navbar(app),
    dbc.Container([
        dbc.Row([
            dbc.Col([
                layout.tabs
            ], xl = 8),
            dbc.Col([
                dbc.Row(dbc.Col(html.Div(id=LayoutID.DIV_BUILDUP_SVG_CONTAINER),className="mb-2")),
                dbc.Row(dbc.Col(layout.card_selected_layer)),
                dbc.Row(dbc.Col(layout.card_gas_layer)),
                dbc.Row(dbc.Col(layout.card_other_layer)),
                dbc.Row(dbc.Col(dbc.Spinner(layout.results_table, color="dark", type="grow")))
            ],xl = 4)
        ]),
        layout.modal_about(app),
        layout.modal_settings,
       
    ], fluid=True )])




@app.callback(
    Output(LayoutID.MODAL_ABOUT, "is_open"),
    [Input(LayoutID.MODAL_ABOUT_CLOSE, "n_clicks"),Input(LayoutID.NAVLINK_ABOUT, "n_clicks")],
    [State(LayoutID.MODAL_ABOUT, "is_open")],
)
def toggle_about_modal(n1, n2, is_open):
    if n1 :
        return not is_open
    if n2 :
        return not is_open
    return is_open


@app.callback(
    Output(LayoutID.MODAL_SETTINGS, "is_open"),
    [Input(LayoutID.MODAL_SETTINGS_CLOSE, "n_clicks"),Input(LayoutID.NAVLINK_SETTINGS, "n_clicks")],
    [State(LayoutID.MODAL_SETTINGS, "is_open")],
)
def toggle_settings_modal(n1, n2, is_open):
    if n1 :
        return not is_open
    if n2 :
        return not is_open
    return is_open





app.title = "Glass Explore"


if __name__ == "__main__":
    app.run_server(debug=True, use_reloader=True)  



