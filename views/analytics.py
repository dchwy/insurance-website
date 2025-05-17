import streamlit as st
import pandas as pd
from utils.db import get_connection

def render():
    st.subheader("Business Analyst Dashboard")
    conn = get_connection()

    # Tổng thanh toán theo hợp đồng
    st.markdown("### 📈 Contract Payment Summary")
    df1 = pd.read_sql("SELECT * FROM Contract_Payment_Summary", conn)
    st.dataframe(df1)

    # Tổng tiền bồi thường
    st.markdown("### 💰 Payout Summary")
    df2 = pd.read_sql("SELECT * FROM Payout_Summary", conn)
    st.dataframe(df2)

    # Số hợp đồng theo loại bảo hiểm
    st.markdown("### 🛍 Product Sales Summary")
    df4 = pd.read_sql("SELECT * FROM Product_Sales_Summary", conn)
    st.dataframe(df4)

    # Số yêu cầu bồi thường theo loại bảo hiểm
    st.markdown("### 📈 Insurance Type Performance")
    df5 = pd.read_sql("SELECT * FROM InsuranceType_Performance", conn)
    st.dataframe(df5)

    conn.close()
