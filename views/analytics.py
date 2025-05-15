import streamlit as st
import pandas as pd
from utils.db import get_connection

def render():
    st.subheader("Business Analyst Dashboard")
    conn = get_connection()

    st.markdown("### 📈 Contract Performance Summary")
    df1 = pd.read_sql("SELECT * FROM ContractPerformanceSummary", conn)
    st.dataframe(df1)

    st.markdown("### 💰 Payout Summary")
    df2 = pd.read_sql("SELECT * FROM PayoutSummary", conn)
    st.dataframe(df2)

    st.markdown("### 📊 Claim Success Rate Summary")
    df3 = pd.read_sql("SELECT * FROM ClaimSuccessRateSummary", conn)
    st.dataframe(df3)

    st.markdown("### 🛍 Product Sales Summary")
    df4 = pd.read_sql("SELECT * FROM ProductSalesSummary", conn)
    st.dataframe(df4)

    st.markdown("### 📈 Insurance Type Performance Summary")
    df5 = pd.read_sql("SELECT * FROM InsuranceTypePerformanceSummary", conn)
    st.dataframe(df5)

    conn.close()
