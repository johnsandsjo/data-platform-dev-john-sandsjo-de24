import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

df = pd.read_csv("athlete_events.csv")

print(df.head())

df_sex = df.value_counts("Sex").reset_index()

fig, ax = plt.subplots(1)
ax.bar(x=df_sex["Sex"], height=df_sex["count"])
fig.savefig(Path(__file__).parent /"ex2_encore.png")
fig.tight_layout()