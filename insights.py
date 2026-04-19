def generate_insights(summary):

    top_option = summary["Count"].idxmax()
    top_percent = summary["Percentage"].max()

    return {
        "top_option": top_option,
        "top_percent": round(top_percent,2)
    }