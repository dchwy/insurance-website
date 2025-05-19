import streamlit as st
import pandas as pd
from utils.db import get_connection
from utils.logger import log_action
from visual_handler import set_background_from_local
def call_procedure(conn, proc_name, args=()):
    cursor = conn.cursor()
    cursor.callproc(proc_name, args)
    results = []
    for result in cursor.stored_results():
        results.extend(result.fetchall())
    cursor.close()
    return results

def render():
    set_background_from_local("assets/background.jpg")
    st.subheader("🧪 Product Development Dashboard")
    conn = get_connection()
    user = st.session_state.get("user", {})

    # 1. View: Insurance Type Catalog
    st.markdown("### 📚 Insurance Types")
    df_types = pd.read_sql("SELECT * FROM View_Insurance_Type", conn)
    st.dataframe(df_types)

    # 2. View: Claim Volume
    st.markdown("### 📊 Claim Volume by Insurance Type")
    df_perf = pd.read_sql("SELECT * FROM InsuranceType_Performance", conn)
    st.dataframe(df_perf)

    # 3. View: Product Sales
    st.markdown("### 💼 Product Sales Summary")
    df_sales = pd.read_sql("SELECT * FROM Product_Sales_Summary", conn)
    st.dataframe(df_sales)



    # 5. Claim approval rate
    st.markdown("### 📈 Claim Approval Rate by Insurance Type")
    result = call_procedure(conn, "Claim_Approval_Rate_By_InsuranceType")
    if result:
        df_result = pd.DataFrame(result, columns=[
            "InsuranceTypeID", "InsuranceName", "TotalClaims", "ApprovedClaims", "ApprovalRatePercent"
        ])
        st.dataframe(df_result)
        log_action(conn, user, "VIEW_CLAIM_APPROVAL_RATE", "Viewed approval rate by insurance type")

    # 6. Total payout
    st.markdown("### 💸 Total Payout by Insurance Type")
    payout = call_procedure(conn, "TotalPayout_By_InsuranceType")
    if payout:
        df_payout = pd.DataFrame(payout, columns=[
            "InsuranceTypeID", "InsuranceName", "TotalPayoutAmount"
        ])
        st.dataframe(df_payout)
        log_action(conn, user, "VIEW_PAYOUT_TOTAL", "Viewed payout summary")

    # 7. Total payment
    st.markdown("### 🧾 Total Payments by Insurance Type")
    payment = call_procedure(conn, "TotalPayment_By_InsuranceType")
    if payment:
        df_payment = pd.DataFrame(payment, columns=[
            "InsuranceTypeID", "InsuranceName", "TotalPaymentAmount"
        ])
        st.dataframe(df_payment)
        log_action(conn, user, "VIEW_PAYMENT_TOTAL", "Viewed payment summary")

    # 4
    st.markdown("## ➕ Add New Insurance Type")

    with st.form("add_insurance_type"):
        type_id = st.text_input("Insurance Type ID")
        name = st.text_input("Insurance Name")
        description = st.text_area("Description")

        if st.form_submit_button("Add Type"):
            if not all([type_id.strip(), name.strip(), description.strip()]):
                st.warning("⚠️ Please fill in all required fields.")
            else:
                try:
                    conn = get_connection()
                    cursor = conn.cursor()
                    cursor.callproc("Insert_InsuranceType", (type_id, name, description))
                    conn.commit()  # ✅ Ensure data is saved
                    cursor.close()

                    log_action(conn, user, "ADD_INSURANCE_TYPE", f"{type_id} - {name}")
                    st.success("✅ Insurance type added.")
                    st.rerun()

                except Exception as e:
                    error_msg = str(e)
                    if "Duplicate entry" in error_msg or "already exists" in error_msg:
                        st.error("❌ Insurance Type ID already exists. Please choose a unique ID.")
                    else:
                        st.error(f"❌ Error: {error_msg}")
                finally:
                    conn.close()


    # 8. Overall claim success rate
    st.markdown("### 🎯 Overall Claim Success Rate")
    rate = call_procedure(conn, "Get_ClaimSuccessRate")
    if rate:
        st.metric("Claim Success Rate (%)", f"{rate[0][0]:.2f}")
        log_action(conn, user, "VIEW_CLAIM_SUCCESS_RATE", "Viewed overall claim success rate")

    conn.close()
