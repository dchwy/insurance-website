import streamlit as st
import pandas as pd
from utils.db import get_connection

def render():
    st.subheader("Claim Assessor Dashboard")
    conn = get_connection()

    # Yêu cầu bồi thường đang chờ xử lý
    st.markdown("### 🕒 Pending Claims")
    df1 = pd.read_sql("SELECT * FROM Pending_Claims", conn)
    st.dataframe(df1)

    # Thông tin đánh giá thiệt hại
    st.markdown("### 📝 Damage Assessments")
    df2 = pd.read_sql("SELECT * FROM View_Assessment", conn)
    st.dataframe(df2)

    # Toàn bộ yêu cầu bồi thường
    st.markdown("### 📄 All Insurance Claims")
    df3 = pd.read_sql("SELECT * FROM View_InsuranceClaim", conn)
    st.dataframe(df3)

    conn.close()
