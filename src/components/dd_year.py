from dash import Dash, html, dcc
from dash.dependencies import Input, Output
from typing import Protocol
from . import ids
import i18n


class YearsDataSource(Protocol):
    @property
    def unique_years(self) -> list[str]:
        ...

    @property
    def all_years(self) -> list[str]:
        ...


def render(app: Dash, source: YearsDataSource) -> html.Div:
    @app.callback(
        Output(ids.YEAR_DROPDOWN, "value"),
        Input(ids.SELECT_ALL_YEARS_BUTTON, "n_clicks"),
    )
    def select_all_years(_: int) -> list[str]:
        return source.unique_years

    return html.Div(
        children=[
            html.H6(i18n.t("general.year")),
            dcc.Dropdown(
                id=ids.YEAR_DROPDOWN,
                options=[{"label": year, "value": year} for year in source.all_years],
                value=source.unique_years,
                multi=True,
            ),
            html.Button(
                className="dropdown-button",
                children=["select All"],
                id=ids.SELECT_ALL_YEARS_BUTTON,
                n_clicks=0,
            ),
        ]
    )
