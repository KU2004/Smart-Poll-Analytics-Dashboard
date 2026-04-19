def clean_data(df):
    df = df.dropna()

    df["Age"] = df["Age"].astype(str)
    df["Region"] = df["Region"].astype(str)
    df["Option"] = df["Option"].astype(str)

    return df