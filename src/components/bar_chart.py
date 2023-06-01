import pandas as pd
from . import ids
from dash import Dash, dcc, html
from dash.dependencies import Input, Output
from ..data.loader import DataSchema
from ..data.source import DataSource
import plotly.express as px
import i18n


def render(app: Dash, source: DataSource) -> html.Div:
    @app.callback(
        Output(ids.BAR_CHART, "children"),
        [
            Input(ids.YEAR_DROPDOWN, "value"),
            Input(ids.MONTH_DROPDOWN, "value"),
            Input(ids.CATEGORY_DROPDOWN, "value"),
        ],
    )
    def update_bar_chart(years: list[str], months: list[str], categories: list[str]) -> html.Div:
        filtered_data = source.filter(years, months, categories)

        if not filtered_data.row_count:
            return html.Div(i18n.t("general.no_data"), id=ids.BAR_CHART)

        fig = px.bar(
            filtered_data.create_pivot_table(),
            x=DataSchema.CATEGORY,
            y=DataSchema.AMOUNT,
            color="category",
            labels={
                "category": i18n.t("general.category"),
                "amount": i18n.t("general.amount"),
            },
        )

        return html.Div(dcc.Graph(figure=fig), id=ids.BAR_CHART)

    return html.Div(id=ids.BAR_CHART)
