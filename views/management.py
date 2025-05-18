import streamlit as st
import pandas as pd
from utils.db import get_connection
from views.auditlog_view import render_auditlog
from visual_handler import set_background_from_local
def log_ceo_view(conn, user_id, table_name):
    cursor = conn.cursor()
    cursor.callproc("LogCEOView", (user_id, table_name))
    conn.commit()
    cursor.close()

def render():
    set_background_from_local("assets/background.jpg")
    st.subheader("👑 CEO Dashboard – Full System Overview")
    conn = get_connection()
    user = st.session_state.get("user", {})
    ceo_id = user.get("user_id")

    table_options = [
        "Customers", "InsuranceContracts", "InsuranceClaim", "Payouts",
        "Payments", "Assessments", "PersonIncharge", "Users"
    ]

    selected_tables = st.multiselect("📂 Select tables to view", table_options)

    for table in selected_tables:
        st.markdown(f"### 📄 {table}")
        df = pd.read_sql(f"SELECT * FROM {table}", conn)
        st.dataframe(df)

    render_auditlog()

    conn.close()
