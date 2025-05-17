import streamlit as st
import pandas as pd
from utils.db import get_connection

def render():
    st.subheader("Audit & Compliance Dashboard")
    conn = get_connection()

    st.markdown("### 🔍 Claim Status Summary")
    df1 = pd.read_sql("SELECT * FROM Total_Claim_By_Status", conn)
    st.dataframe(df1)

    st.markdown("### 💸 Payout Summary")
    df2 = pd.read_sql("SELECT * FROM Payout_Summary", conn)
    st.dataframe(df2)

    st.markdown("### 🧑‍💼 Person In Charge")
    df3 = pd.read_sql("SELECT * FROM View_PersonIncharge_Admin", conn)
    st.dataframe(df3)

    st.markdown("### 📑 All Insurance Claims (Admin)")
    df4 = pd.read_sql("SELECT * FROM View_InsuranceClaim_Admin", conn)
    st.dataframe(df4)

    conn.close()
