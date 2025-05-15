import streamlit as st
import pandas as pd
from utils.db import get_connection

def render():
    st.subheader("Viewer Dashboard")
    conn = get_connection()

    st.markdown("### 📋 Pending Claims")
    df1 = pd.read_sql("SELECT * FROM PendingClaims", conn)
    st.dataframe(df1)

    st.markdown("### 📈 Contract Performance Summary")
    df2 = pd.read_sql("SELECT * FROM ContractPerformanceSummary", conn)
    st.dataframe(df2)

    conn.close()
