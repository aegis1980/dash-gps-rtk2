from dash import html, dcc,dash_table
import dash_bootstrap_components as dbc
from glass_explore import (LayoutID, callback_helpers, igdb, OG_DESCRIPTION)

NAV_LOGO = 'nav_logo.png'
COFFEE = 'coffee.svg'
LINK_COFFEE = "https://www.buymeacoffee.com/fitc"

nav = dbc.Nav(
    [
        dbc.NavItem(dbc.NavLink( "About",id = LayoutID.NAVLINK_ABOUT)),
        dbc.NavItem(dbc.NavLink("Settings",disabled=True,id = LayoutID.NAVLINK_SETTINGS)),
    ]
)

def navbar(app):
    return dbc.Navbar(
    [
        html.A(
            # Use row and col to control vertical alignment of logo / brand
            dbc.Row(
                [
                    dbc.Col(html.Img(src=app.get_asset_url(NAV_LOGO), height="30px")),
                    dbc.Col(dbc.NavbarBrand("GLASS EXPLORE", className="ms-2")),
                ],
                align="center",
                className="g-0",
            ),
            href="https://floatingintheclouds.com",
            style={"textDecoration": "none"},
        ),
        dbc.NavbarToggler(id="navbar-toggler", n_clicks=0),
            dbc.Collapse(
                nav,
                id="navbar-collapse",
                is_open=False,
                navbar=True,
            ),
    ],
    color="dark",
    dark=True,
)


def modal_about(app):
    return dbc.Modal(
            [
                dbc.ModalHeader(dbc.ModalTitle("Glass Explore")),
                dbc.ModalBody([
                    html.P([OG_DESCRIPTION]),
                    html.P(["App is only intended as a playground - consult manufacturer's published data or use a tool such as LBNL Window to verify."]),
                    dbc.Row([
                        dbc.Col([
                            html.A(
                                html.Img(src=app.get_asset_url(COFFEE), height="60px"), 
                                href=LINK_COFFEE, className="alert-link", target="_blank"
                            ),
                        ],
                        width="auto"
                        ),
                        dbc.Col([
                            html.P([
                                "Glass Explore took me a fair while to write (and check!). Server costs are not free either. If you do find this app useful, please consider ", 
                                html.A("buying me a coffee", href=LINK_COFFEE, className="alert-link", target="_blank")
                            ]),
                            html.P([
                                "I have a few bits and bobs I want to add, but if you have suggestions, contact me on ", 
                                html.A("linkedin", href="https://www.linkedin.com/in/jon-robinson-nz/", className="alert-link", target="_blank")
                            ])
                        ]),
                    ])
                ]),
                dbc.ModalFooter(
                    dbc.Button(
                        "Close", id=LayoutID.MODAL_ABOUT_CLOSE, className="ms-auto", n_clicks=0
                    )
                ),
            ],
            id=LayoutID.MODAL_ABOUT,
            is_open=True,
        )


