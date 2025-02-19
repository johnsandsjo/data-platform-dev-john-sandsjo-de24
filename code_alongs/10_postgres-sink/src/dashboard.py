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
    currency = {
        "SEK": 10000000,
        "NOK" : -1000000,
    }
    df = load_data("SELECT * FROM bitcoin;")
    df["price SEK"] = df["price_usd"]*currency["SEK"]
    df["price NOK"] = df["price_usd"]*currency["NOK"]
    btc_df = df[df['coin'] == 'Bitcoin']
    eth_df = df[df['coin'] == 'Ethereum']

    st.markdown("# Latest Price")

    crypto_choice = st.selectbox("Choose currency", df["coin"].unique())
    currency_choice = st.selectbox("Choose currency", ['SEK', 'NOK'])
    price_column = f"price {currency_choice}"
    if crypto_choice == "Bitcoin":
        current_df = btc_df
    elif crypto_choice == "Ethereum":
        current_df = eth_df
    st.metric(f"{crypto_choice}", f"{current_df[price_column].iloc[-1]:,.2f} {currency_choice}", border=True)
    st.dataframe(current_df)

    

#df = load_data("SELECT * FROM bitcoin;")
#print(df)

if __name__ == '__main__':
    layout()