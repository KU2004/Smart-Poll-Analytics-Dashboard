import pandas as pd
import os
from src.config import DATA_PATH

def load_data():
    if not os.path.exists("data"):
        os.makedirs("data")

    if not os.path.exists(DATA_PATH):
        df = pd.DataFrame(columns=["Respondent_ID","Age","Region","Option","Date"])
        df.to_csv(DATA_PATH, index=False)

    return pd.read_csv(DATA_PATH)


def save_data(df):
    df.to_csv(DATA_PATH, index=False)