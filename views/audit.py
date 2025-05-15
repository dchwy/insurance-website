import streamlit as st
import pandas as pd
from utils.db import get_connection

def render():
    st.subheader("Compliance & Audit Dashboard")
    conn = get_connection()

    st.markdown("### 📋 Pending Claims")
    df1 = pd.read_sql("SELECT * FROM PendingClaims", conn)
    st.dataframe(df1)

    st.markdown("### 📊 Claim Success Rate Summary")
    df2 = pd.read_sql("SELECT * FROM ClaimSuccessRateSummary", conn)
    st.dataframe(df2)

    st.markdown("### 💳 Contract Payment Summary")
    df3 = pd.read_sql("SELECT * FROM ContractPaymentSummary", conn)
    st.dataframe(df3)

    conn.close()
