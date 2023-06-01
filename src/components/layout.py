from dash import Dash, html
from . import bar_chart, dd_year, dd_month, dd_category, pie_chart
from ..data.source import DataSource
import pandas as pd


def create_layout(app: Dash, source: DataSource) -> html.Div:
    return html.Div(
        className="app-div",
        children=[
            html.H1(app.title),
            html.Hr(),
            html.Div(
                className="dropdown_container",
                children=[dd_year.render(app, source), dd_month.render(app, source), dd_category.render(app, source)],
            ),
            bar_chart.render(app, source),
            pie_chart.render(app, source),
        ],
    )
