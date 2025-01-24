from pathlib import Path
import pandas as pd

datapath = Path(__file__).parent/"data"

df = pd.read_csv(datapath/"prog_book.csv")

print(df.head())

print(df.info())

df.head().to_csv(datapath/ "prog_book_head.csv")