import plotly.express as px
import os
from src.config import OUTPUT_PATH

def save_fig(fig, name):
    if not os.path.exists(OUTPUT_PATH):
        os.makedirs(OUTPUT_PATH)

    fig.write_image(f"{OUTPUT_PATH}/{name}.png")


def bar_chart(counts):
    fig = px.bar(x=counts.index, y=counts.values,
                 labels={"x":"Option","y":"Votes"},
                 title="Option Distribution")

    save_fig(fig, "bar_chart")
    return fig


def pie_chart(counts):
    fig = px.pie(names=counts.index, values=counts.values,
                 title="Vote Share")

    save_fig(fig, "pie_chart")
    return fig


def region_chart(region_df):
    fig = px.bar(region_df, barmode="stack",
                 title="Region-wise Analysis")

    save_fig(fig, "region_chart")
    return fig


def trend_chart(trend_df):
    fig = px.line(trend_df, x="Date", y="Responses",
                  title="Trend Over Time")

    save_fig(fig, "trend_chart")
    return fig