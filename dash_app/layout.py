from dash import html
import dash_bootstrap_components as dbc
from dash_app import (CONFIG,LayoutID)

NAV_LOGO = 'nav_logo.png'

def navbar(app):
    return dbc.Navbar(
    [
        html.A(
            # Use row and col to control vertical alignment of logo / brand
            dbc.Row(
                [
                    dbc.Col(html.Img(src=app.get_asset_url(NAV_LOGO), height="30px")),
                    dbc.Col(dbc.NavbarBrand(CONFIG['details']['title'], className="ms-2")),
                ],
                align="center",
                className="g-0",
            ),
            href="https://floatingintheclouds.com",
            style={"textDecoration": "none"},
        ),
    ],
    color="dark",
    dark=True,
)

