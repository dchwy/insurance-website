import streamlit as st
import pandas as pd
from utils.db import get_connection
from utils.logger import log_action  # ✅ thêm phần này
from visual_handler import set_background_from_local
def call_procedure(conn, proc_name, args=()):
    cursor = conn.cursor()
    cursor.callproc(proc_name, args)
    conn.commit()
    cursor.close()

def render():
    set_background_from_local("assets/background.jpg")
    st.subheader("🧾 Claim Assessor Dashboard")
    conn = get_connection()
    user = st.session_state.get("user", {})

    # 1. View: Pending Claims
    st.markdown("### 🕒 Pending Claims")
    pending = pd.read_sql("SELECT * FROM Pending_Claims", conn)
    st.dataframe(pending)

    # 2. View: Damage Assessments
    st.markdown("### 📝 Damage Assessments")
    assessments = pd.read_sql("SELECT * FROM View_Assessment", conn)
    st.dataframe(assessments)

    # 3. View: All Insurance Claims
    st.markdown("### 📄 All Insurance Claims")
    claims = pd.read_sql("SELECT * FROM View_InsuranceClaim", conn)
    st.dataframe(claims)

    # 5. Create new payout
    st.markdown("---")
    st.markdown("## 💸 Create Payout after Approved Assessment")
    with st.form("create_payout"):
        claim_id = st.text_input("Claim ID for payout", key="payout_claim_id")
        amount = st.number_input("Amount", min_value=0.0)
        payout_date = st.date_input("Payout Date")
        method = st.selectbox("Payout Method", ["Chuyển khoản", "Tiền Mặt"])
        status = st.selectbox("Payout Status", ["Pending", "Paid"])

        if st.form_submit_button("Create Payout"):
            call_procedure(conn, "Create_NewPayout", (
                amount, payout_date, method, status, claim_id
            ))
            log_action(conn, user, "CREATE_PAYOUT", f"{claim_id} - {amount} - {status}")
            st.success("✅ Payout created successfully!")
            st.rerun()

    conn.close()


    st.markdown("### ➕ Add New Assessment")
    with st.form("insert_assessment"):
        aid = st.text_input("Assessment ID")
        claim_id = st.text_input("Claim ID")
        date = st.date_input("Assessment Date")
        severity = st.selectbox("Severity Level", ["Low", "Medium", "High"])
        review = st.date_input("Review Date")
        notes = st.text_area("Notes")

        if st.form_submit_button("Submit Assessment"):
            if not all([aid.strip(), claim_id.strip(), notes.strip()]):
                st.warning("⚠️ Please fill in all required fields.")
            else:
                try:
                    conn = get_connection()
                    cursor = conn.cursor()
                    cursor.callproc("Insert_Assessment", (
                        aid, claim_id, date, severity, review, notes
                    ))
                    conn.commit()  # ✅ thêm commit
                    cursor.close()

                    log_action(conn, user, "INSERT_ASSESSMENT", f"{aid} for Claim {claim_id}")
                    st.success("✅ Assessment added.")
                    st.rerun()
                except Exception as e:
                    st.error(f"❌ Error: {e}")
                finally:
                    conn.close()


    st.markdown("### 🔄 Update Assessment Result")
    with st.form("update_assessment_result"):
        assessment_id = st.text_input("Assessment ID")
        new_result = st.selectbox("New Result", ["Approved", "Rejected", "Pending"])

        if st.form_submit_button("Update Result"):
            if not assessment_id.strip():
                st.warning("⚠️ Please enter the Assessment ID.")
            else:
                try:
                    conn = get_connection()
                    cursor = conn.cursor()
                    cursor.callproc("Update_Assessment_Result", (assessment_id, new_result))
                    conn.commit()  # ✅ thêm commit
                    cursor.close()

                    log_action(conn, user, "UPDATE_ASSESSMENT_RESULT", f"{assessment_id} → {new_result}")
                    st.success("✅ Assessment result updated.")
                    st.rerun()
                except Exception as e:
                    st.error(f"❌ Error: {e}")
                finally:
                    conn.close()