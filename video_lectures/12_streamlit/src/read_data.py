import pandas as pd
from pathlib import Path

def read_data():
    data_path = Path(__file__).parents[1] / "data"

    df = pd.read_excel(data_path/"resultat-ansokningsomgang-2024.xlsx", sheet_name="Tabell 3", skiprows=5)

    return df

if __name__ == "__main__":
    df = read_data()
    print(df.columns)