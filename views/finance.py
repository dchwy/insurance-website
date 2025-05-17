import streamlit as st
import pandas as pd
from utils.db import get_connection

def render():
    st.subheader("Finance Department Dashboard")
    conn = get_connection()

    st.markdown("### 💰 Contract Payment Summary")
    df1 = pd.read_sql("SELECT * FROM Contract_Payment_Summary", conn)
    st.dataframe(df1)

    st.markdown("### 🧾 Unpaid Contracts")
    df2 = pd.read_sql("SELECT * FROM Unpaid_Contracts", conn)
    st.dataframe(df2)

    st.markdown("### 💸 Payout Summary")
    df3 = pd.read_sql("SELECT * FROM Payout_Summary", conn)
    st.dataframe(df3)

    st.markdown("### 📂 Payments")
    df4 = pd.read_sql("SELECT * FROM View_Payments", conn)
    st.dataframe(df4)

    st.markdown("### 📋 Payouts")
    df5 = pd.read_sql("SELECT * FROM View_Payouts", conn)
    st.dataframe(df5)

    conn.close()
