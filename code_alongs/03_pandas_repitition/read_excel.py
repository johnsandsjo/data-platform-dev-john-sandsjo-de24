#här kör vi via python script
import pandas as pd
from pathlib import Path

# print(Path(__file__).parent / "data")
data_path = Path(__file__).parent / "data"

df = pd.read_excel(data_path / "calories.xlsx")
print(df.head())