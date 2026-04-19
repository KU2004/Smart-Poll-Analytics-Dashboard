def calculate_metrics(summary):

    total_votes = summary["Count"].sum()
    top_option = summary["Count"].idxmax()
    top_percent = summary["Percentage"].max()

    return total_votes, top_option, round(top_percent,2)