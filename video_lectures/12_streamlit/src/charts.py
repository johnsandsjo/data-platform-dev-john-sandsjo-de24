import duckdb
from read_data import read_data
import streamlit as st

df = read_data()

def approved_by_area_bar():
    df = duckdb.query(
        """
                SELECT 
                    utbildningsområde, COUNT(*) AS Beviljade
                FROM 
                    df 
                WHERE 
                    beslut = 'Beviljad'
                GROUP BY 
                    utbildningsområde
                ORDER BY 
                    Beviljade
                DESC
        """
    ).df()

    st.bar_chart(df, x="Utbildningsområde", y = "Beviljade")