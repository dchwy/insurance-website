import streamlit as st
import pandas as pd
from utils.db import get_connection

def render():
    st.subheader("Product Development Dashboard")
    conn = get_connection()

    st.markdown("### 💰 Payout Summary")
    df1 = pd.read_sql("SELECT * FROM PayoutSummary", conn)
    st.dataframe(df1)

    st.markdown("### 📊 Claim Success Rate")
    df2 = pd.read_sql("SELECT * FROM ClaimSuccessRateSummary", conn)
    st.dataframe(df2)

    st.markdown("### 📈 Insurance Type Performance")
    df3 = pd.read_sql("SELECT * FROM InsuranceTypePerformanceSummary", conn)
    st.dataframe(df3)

    conn.close()
