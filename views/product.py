import streamlit as st
import pandas as pd
from utils.db import get_connection

def render():
    st.subheader("Product Development Dashboard")
    conn = get_connection()

    st.markdown("### 🛍 Product Sales Summary")
    df1 = pd.read_sql("SELECT * FROM Product_Sales_Summary", conn)
    st.dataframe(df1)

    st.markdown("### 📈 Insurance Type Performance")
    df2 = pd.read_sql("SELECT * FROM InsuranceType_Performance", conn)
    st.dataframe(df2)

    st.markdown("### 📚 Insurance Types Catalog")
    df3 = pd.read_sql("SELECT * FROM View_Insurance_Type", conn)
    st.dataframe(df3)

    conn.close()
