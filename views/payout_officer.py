import streamlit as st
import pandas as pd
from utils.db import get_connection

def render():
    st.subheader("💰 Payout Officer Dashboard")
    conn = get_connection()

    st.markdown("### 💸 Pending Payments")
    df1 = pd.read_sql("SELECT * FROM PendingPayments", conn)
    st.dataframe(df1)

    st.markdown("### 💰 Payout Summary")
    df2 = pd.read_sql("SELECT * FROM PayoutSummary", conn)
    st.dataframe(df2)

    st.markdown("### 📊 Contract Payment Summary")
    df3 = pd.read_sql("SELECT * FROM ContractPaymentSummary", conn)
    st.dataframe(df3)

    conn.close()
