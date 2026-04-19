def apply_filters(df, regions, ages):
    return df[
        (df["Region"].isin(regions)) &
        (df["Age"].isin(ages))
    ]