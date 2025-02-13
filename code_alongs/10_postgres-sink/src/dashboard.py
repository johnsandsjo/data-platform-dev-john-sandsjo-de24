import streamlit as st
from streamlit_autorefresh import st_autorefresh
from sqlalchemy import create_engine
import pandas as pd
from constants import (
    POSTGRES_DBNAME,
    POSTGRES_HOST,
    POSTGRES_PASSWORD,
    POSTGRES_PORT,
    POSTGRES_USER,
)

connection_string = f"postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DBNAME}"

engine = create_engine(connection_string)

def load_data(query):
    with engine.connect() as conn:
        df = pd.read_sql(query, conn)
        df = df.set_index("timestamp")
        return df

count = st_autorefresh(interval=10*1000, limit= 100, key="data_refresh")

def layout():
    df = load_data("SELECT * FROM bitcoin;")
    st.markdown("# Coin Data Got Damn it!")

    st.dataframe(df.tail())

#df = load_data("SELECT * FROM bitcoin;")
#print(df)

if __name__ == '__main__':
    layout()