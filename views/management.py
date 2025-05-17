import streamlit as st
import pandas as pd
from utils.db import get_connection

def render():
    st.subheader("Executive (CEO) Dashboard")
    conn = get_connection()

    st.markdown("### 📊 Contract Statistics by Month")
    df1 = pd.read_sql("SELECT * FROM Contract_By_Month", conn)
    st.dataframe(df1)

    st.markdown("### 🛍 Product Sales Summary")
    df2 = pd.read_sql("SELECT * FROM Product_Sales_Summary", conn)
    st.dataframe(df2)

    st.markdown("### 📈 Insurance Type Performance")
    df3 = pd.read_sql("SELECT * FROM InsuranceType_Performance", conn)
    st.dataframe(df3)

    st.markdown("### 📉 Expiring Contracts (30 Days)")
    df4 = pd.read_sql("SELECT * FROM Expiring_Contracts", conn)
    st.dataframe(df4)

    st.markdown("### 💸 Payout Summary")
    df5 = pd.read_sql("SELECT * FROM Payout_Summary", conn)
    st.dataframe(df5)

    conn.close()
