import pandas as pd

def calculate_summary(df):
    counts = df["Option"].value_counts()
    percentage = (counts / len(df)) * 100

    return pd.DataFrame({
        "Count": counts,
        "Percentage": percentage
    })


def region_analysis(df):
    return pd.crosstab(df["Region"], df["Option"])


def trend_analysis(df):
    df["Date"] = pd.to_datetime(df["Date"])
    trend = df.groupby(df["Date"].dt.date)["Option"].count().reset_index()
    trend.columns = ["Date","Responses"]
    return trend