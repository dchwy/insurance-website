import streamlit as st
import pandas as pd
from utils.db import get_connection

def render():
    st.subheader("Sales & Marketing Dashboard")
    conn = get_connection()

    st.markdown("### 📈 Contract Performance Summary")
    df1 = pd.read_sql("SELECT * FROM ContractPerformanceSummary", conn)
    st.dataframe(df1)

    st.markdown("### 👥 Customer Contract Count")
    df2 = pd.read_sql("SELECT * FROM CustomerContractCount", conn)
    st.dataframe(df2)

    st.markdown("### 🛍 Product Sales Summary")
    df3 = pd.read_sql("SELECT * FROM ProductSalesSummary", conn)
    st.dataframe(df3)

    conn.close()
