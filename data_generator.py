import pandas as pd
import numpy as np
import os

def generate_poll_data(n=6000):

    np.random.seed(42)

    age_groups = ["18-25", "26-35", "36-50", "50+"]
    regions = ["North", "South", "East", "West"]
    options = ["Product A", "Product B", "Product C"]

    # Realistic region bias
    region_bias = {
        "North": [0.5, 0.3, 0.2],
        "South": [0.2, 0.5, 0.3],
        "East":  [0.3, 0.3, 0.4],
        "West":  [0.4, 0.2, 0.4]
    }

    data = []

    for i in range(n):
        age = np.random.choice(age_groups)
        region = np.random.choice(regions)

        # biased option selection
        option = np.random.choice(options, p=region_bias[region])

        date = pd.Timestamp.now() - pd.Timedelta(days=np.random.randint(0, 90))

        data.append({
            "Respondent_ID": i + 1,
            "Age": age,
            "Region": region,
            "Option": option,
            "Date": date
        })

    df = pd.DataFrame(data)

    # create data folder if not exists
    if not os.path.exists("data"):
        os.makedirs("data")

    df.to_csv("data/poll_data.csv", index=False)

    print("✅ 6000 poll records generated successfully!")

    return df


# run directly
if __name__ == "__main__":
    generate_poll_data(6000)