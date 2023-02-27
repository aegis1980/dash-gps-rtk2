import json
import time

import dash
import dash_bootstrap_components as dbc
import numpy as np
import pandas as pd
from dash import Input, Output, State, ctx, dcc, html
from dash.exceptions import PreventUpdate
import dash_app
from dash_app import (CONFIG,LayoutID, Mqtt ,layout)

import dash_mqtt

app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    index_string=dash.dash._default_index.replace('<html>', '<html lang="en" prefix="og: http://ogp.me/ns#">'),
    meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1"},
        {"property" : "og:title", "content": "Glass Explore"},
        {"name":"image" ,  "property":"og:image" ,  "content":"https://floatingintheclouds.com/wp-content/uploads/2022/09/glass-explore.png" },
        {"name":"author" ,  "content":"Jon Robinson" },
        {"property" : "og:description", "content": CONFIG['details']['description']},
        {"property" : "og:url", "content": CONFIG['details']['url']}
    ],
)

app.layout = html.Div([
    dcc.Location(LayoutID.URL),
    layout.navbar(app),
    dbc.Container([
        dbc.Row([
            dbc.Col([
                html.H1('MQTT echo'),
                dbc.Input(
                    id='message_to_send',
                    placeholder='message to send',
                    debounce = True),
                dbc.Button('Send',id='send'),
                html.Div(id='return_message')

            ])
        ])
    ], fluid=True),
    dash_mqtt.DashMqtt(
        id=LayoutID.MQTT,
        broker_url=Mqtt.BROKER_URL,
        broker_port = Mqtt.BROKER_PORT,
        #broker_path = Mqtt.BROKER_PATH,
        topics=[Mqtt.TOPIC_NMEA,Mqtt.TOPIC_STATUS]
    ),
])


@app.callback(
        Output(LayoutID.MQTT, 'message'),
        Input('send', 'n_clicks'),
        State('message_to_send', 'value')
    )
def publish_message(n_clicks, message_payload):
    if n_clicks:
        return {
            'topic': Mqtt.TOPIC_STATUS,
            'payload' : message_payload
        }
    return dash.no_update


@app.callback(
        Output('return_message', 'children'),
        Input(LayoutID.MQTT, 'incoming')
    )
def incoming(message):
    return message['payload']

app.title = CONFIG['details']['title']


if __name__ == "__main__":
    app.run_server(debug=True, use_reloader=True)  



