import streamlit as st
import pandas as pd
from utils.db import get_connection
from utils.logger import log_action  # nếu bạn dùng log_action để ghi log
from visual_handler import set_background_from_local
def call_procedure(conn, proc_name, args=()):
    cursor = conn.cursor()
    cursor.callproc(proc_name, args)
    conn.commit()
    cursor.close()

def render():
    set_background_from_local("assets/background.jpg")
    st.subheader("💰 Finance Dashboard")
    conn = get_connection()
    user = st.session_state.get("user", {})

    # 1. View: Payout Summary
    st.markdown("### 💸 Payout Summary by Contract")
    df1 = pd.read_sql("SELECT * FROM Payout_Summary", conn)
    st.dataframe(df1)

    # 2. View: Contract Payment Summary
    st.markdown("### 🧾 Total Payments by Contract")
    df2 = pd.read_sql("SELECT * FROM Contract_Payment_Summary", conn)
    st.dataframe(df2)

    # 3. View: Unpaid Contracts
    st.markdown("### ⚠️ Unpaid Contracts")
    df3 = pd.read_sql("SELECT * FROM Unpaid_Contracts", conn)
    st.dataframe(df3)

    # 4. Update Payout Status
    st.markdown("---")
    st.markdown("## 🔄 Update Payout Status")
    with st.form("update_payout_status"):
        payout_id = st.text_input("Payout ID")
        new_status = st.selectbox("New Status", ["Pending", "Paid", "Rejected"])

        if st.form_submit_button("Update Status"):
            call_procedure(conn, "Update_PayoutStatus", (payout_id, new_status))
            log_action(conn, user, "UPDATE_PAYOUT_STATUS", f"PayoutID {payout_id} -> {new_status}")
            st.success("✅ Payout status updated!")
            st.rerun()

    conn.close()
