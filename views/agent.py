import streamlit as st
import pandas as pd
from utils.db import get_connection

def render():
    st.subheader("Insurance Agent Dashboard")
    conn = get_connection()

    st.markdown("### 📄 Active Contracts")
    df1 = pd.read_sql("SELECT * FROM ActiveContracts", conn)
    st.dataframe(df1)

    st.markdown("### 💸 Pending Payments")
    df2 = pd.read_sql("SELECT * FROM PendingPayments", conn)
    st.dataframe(df2)

    st.markdown("### 👥 Customer Contract Count")
    df3 = pd.read_sql("SELECT * FROM CustomerContractCount", conn)
    st.dataframe(df3)

    conn.close()
