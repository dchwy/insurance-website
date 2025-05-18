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
    st.subheader("📞 Customer Support Dashboard")
    conn = get_connection()
    user = st.session_state.get("user", {})

    # 1. Active Contracts
    st.markdown("### ✅ Active Contracts")
    df_active = pd.read_sql("SELECT * FROM Active_Contracts", conn)
    st.dataframe(df_active)
    log_action(conn, user, "VIEW_ACTIVE_CONTRACTS", "Viewed active contracts")

    # 2. Expiring Contracts
    st.markdown("### ⏳ Contracts Expiring Soon")
    df_exp = pd.read_sql("SELECT * FROM Expiring_Contracts", conn)
    st.dataframe(df_exp)
    log_action(conn, user, "VIEW_EXPIRING_CONTRACTS", "Viewed contracts expiring soon")

    # 3. Pending Claims
    st.markdown("### 🕒 Pending Claims")
    df_pending = pd.read_sql("SELECT * FROM Pending_Claims", conn)
    st.dataframe(df_pending)
    log_action(conn, user, "VIEW_PENDING_CLAIMS", "Viewed pending claims")

    # 4. Lookup contract signer info
    st.markdown("---")
    st.markdown("## 📋 Look up Contract Signer Info")
    with st.form("contract_signer_lookup"):
        contract_id = st.text_input("Enter Contract ID")
        if st.form_submit_button("Lookup"):
            try:
                result = call_procedure(conn, "Get_Contract_Signer_Info", (contract_id,))
                if result:
                    df_result = pd.DataFrame(result, columns=["SignerName", "SignerPhone", "SignerEmail"])
                    st.dataframe(df_result)
                    log_action(conn, user, "LOOKUP_CONTRACT_SIGNER", f"Lookup signer for {contract_id}")
                else:
                    st.warning("⚠️ No result found.")
            except Exception as e:
                st.error(f"❌ Error: {e}")

    conn.close()
