import streamlit as st
import pandas as pd
from utils.db import get_connection

def render():
    st.subheader("Insurance Agent Dashboard")
    conn = get_connection()

    # Hợp đồng đang hoạt động
    st.markdown("### 📄 Active Contracts")
    df1 = pd.read_sql("SELECT * FROM Active_Contracts", conn)
    st.dataframe(df1)

    # Hợp đồng chưa thanh toán
    st.markdown("### 💸 Unpaid Contracts")
    df2 = pd.read_sql("SELECT * FROM Unpaid_Contracts", conn)
    st.dataframe(df2)

    # Số hợp đồng theo khách hàng
    st.markdown("### 👥 Customer Contract Count")
    df3 = pd.read_sql("SELECT * FROM Customer_Contract_Count", conn)
    st.dataframe(df3)

    conn.close()
