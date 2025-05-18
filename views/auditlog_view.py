import streamlit as st
import pandas as pd
from utils.db import get_connection

def render_auditlog():
    
    st.subheader("📒 System Audit Log")
    conn = get_connection()
    user = st.session_state.get("user", {})
    role = user.get("role")



    df = pd.read_sql("""
        SELECT a.LogID, u.FullName AS User, a.Action, a.Details, a.Timestamp
        FROM AuditLog a
        JOIN Users u ON a.User_id = u.User_id
        ORDER BY a.Timestamp DESC
    """, conn)

    with st.expander("🔍 Filter Logs", expanded=False):
        name_filter = st.text_input("Filter by user name")
        action_filter = st.text_input("Filter by action keyword")
        date_range = st.date_input("Filter by date range", [])

        if name_filter:
            df = df[df["User"].str.contains(name_filter, case=False)]

        if action_filter:
            df = df[df["Action"].str.contains(action_filter, case=False)]

        if len(date_range) == 2:
            start, end = date_range
            df = df[(df["Timestamp"] >= pd.to_datetime(start)) & (df["Timestamp"] <= pd.to_datetime(end))]

    st.dataframe(df, use_container_width=True)
    conn.close()
