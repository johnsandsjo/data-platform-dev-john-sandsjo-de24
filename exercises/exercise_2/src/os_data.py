import pandas as pd
import matplotlib.pyplot as plt
import duckdb
from pathlib import Path

#Now create your os_data.py app to read in athelete_events.csv as a dataframe, 
#print out df.head(), plot a graph and export it to src folder.

with open("athlete_events.csv") as file:
    df = pd.read_csv(file)
print(df.head())

to_plot_df = duckdb.query("""
             SELECT Sex, mean(Age) FROM df GROUP BY Sex;
             """).df()

fig, ax = plt.subplots(1)
ax.bar(x=to_plot_df["Sex"], height=to_plot_df["mean(Age)"])
fig.savefig(Path(__file__).parent / "avg_age.png")
fig.tight_layout()