from dash import Dash, html, dcc
from dash.dependencies import Input, Output
from . import ids
import pandas as pd
from ..data.source import DataSource


def render(app: Dash, source: DataSource) -> html.Div:
    @app.callback(
        Output(ids.CATEGORY_DROPDOWN, "value"),
        Input(ids.SELECT_ALL_CATEGORIES_BUTTON, "n_clicks"),
    )
    def select_all_categories(_: int) -> list[str]:
        return source.unique_categories

    return html.Div(
        children=[
            html.H6("Categories"),
            dcc.Dropdown(
                id=ids.CATEGORY_DROPDOWN,
                options=[{"label": category, "value": category} for category in source.all_categories],
                value=source.unique_categories,
                multi=True,
            ),
            html.Button(
                className="dropdown-button",
                children=["select All"],
                id=ids.SELECT_ALL_CATEGORIES_BUTTON,
                n_clicks=0,
            ),
        ]
    )
