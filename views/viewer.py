import streamlit as st
import pandas as pd
from utils.db import get_connection

def render():
    st.subheader("Customer Support Dashboard")
    conn = get_connection()

    st.markdown("### 📅 Expiring Contracts (Next 30 Days)")
    df1 = pd.read_sql("SELECT * FROM Expiring_Contracts", conn)
    st.dataframe(df1)

    st.markdown("### 👥 Customer Contract Count")
    df2 = pd.read_sql("SELECT * FROM Customer_Contract_Count", conn)
    st.dataframe(df2)

    st.markdown("### 📇 Customer Information")
    df3 = pd.read_sql("SELECT * FROM View_Customers_Admin", conn)
    st.dataframe(df3)

    conn.close()
