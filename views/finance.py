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
        new_status = st.selectbox("New Status", ["Pending", "Paid"])

        if st.form_submit_button("Update Status"):
            if not payout_id.strip():
                st.warning("⚠️ Please enter the Payout ID.")
            else:
                try:
                    conn2 = get_connection()  # 🔁 kết nối mới
                    call_procedure(conn2, "Update_PayoutStatus", (payout_id, new_status))
                    log_action(conn2, user, "UPDATE_PAYOUT_STATUS", f"PayoutID {payout_id} -> {new_status}")
                    st.success("✅ Payout status updated!")
                    st.rerun()
                except Exception as e:
                    st.error(f"❌ Error: {e}")
                finally:
                    conn2.close()
                    
    st.markdown("### 💰 Create New Payment")
    with st.form("create_payment_form"):
        contract_id = st.text_input("Contract ID")
        payment_date = st.date_input("Payment Date")
        payment_method = st.selectbox("Payment Method", ["Tiền mặt", "Chuyển khoản"])
        amount = st.number_input("Amount (VNĐ)", min_value=1000, step=1000)

        if st.form_submit_button("Create Payment"):
            if not contract_id.strip():
                st.warning("⚠️ Please enter the Contract ID.")
            else:
                try:
                    conn = get_connection()
                    cursor = conn.cursor()
                    cursor.callproc("Create_NewPayment", (
                        contract_id, payment_date, payment_method, amount
                    ))
                    conn.commit()  # ✅ ensure the insert is saved
                    cursor.close()

                    log_action(conn, user, "CREATE_PAYMENT", f"{contract_id} - {payment_method} - {amount} VNĐ")
                    st.success("✅ New payment has been recorded.")
                    st.rerun()

                except Exception as e:
                    st.error(f"❌ Error: {e}")
                finally:
                    conn.close()


    conn.close()
