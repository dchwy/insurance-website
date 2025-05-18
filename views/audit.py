import streamlit as st
import pandas as pd
from utils.db import get_connection
from visual_handler import set_background_from_local
def render():
    set_background_from_local("assets/background.jpg")
    st.subheader("🛡 Compliance & Audit Dashboard")
    conn = get_connection()

    # 1. View: Payout Summary
    st.markdown("### 💸 Payout Summary by Contract")
    df_payout = pd.read_sql("SELECT * FROM Payout_Summary", conn)
    st.dataframe(df_payout)

    # 2. View: Contract Payment Summary
    st.markdown("### 🧾 Total Payments by Contract")
    df_payment = pd.read_sql("SELECT * FROM Contract_Payment_Summary", conn)
    st.dataframe(df_payment)

    # 3. View: Unpaid Contracts
    st.markdown("### ⚠️ Unpaid Contracts")
    df_unpaid = pd.read_sql("SELECT * FROM Unpaid_Contracts", conn)
    st.dataframe(df_unpaid)

    # 4. View: Audit Log
    st.markdown("### 📋 Audit Log")
    df_log = pd.read_sql("SELECT * FROM AuditLog ORDER BY Timestamp DESC", conn)
    st.dataframe(df_log)

    conn.close()
