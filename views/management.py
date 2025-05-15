import streamlit as st
import pandas as pd
from utils.db import get_connection

def render():
    st.subheader("Management Dashboard")
    conn = get_connection()

    st.markdown("### 📈 Contract Performance Summary")
    df1 = pd.read_sql("SELECT * FROM ContractPerformanceSummary", conn)
    st.dataframe(df1)

    st.markdown("### ⏳ Expiring Contracts")
    df2 = pd.read_sql("SELECT * FROM ExpiringContracts", conn)
    st.dataframe(df2)

    st.markdown("### 📊 Claim Success Rate")
    df3 = pd.read_sql("SELECT * FROM ClaimSuccessRateSummary", conn)
    st.dataframe(df3)

    st.markdown("### 💰 Payout Summary")
    df4 = pd.read_sql("SELECT * FROM PayoutSummary", conn)
    st.dataframe(df4)

    conn.close()
