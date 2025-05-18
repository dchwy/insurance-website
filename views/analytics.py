import streamlit as st
import pandas as pd
from utils.db import get_connection
from visual_handler import set_background_from_local
def call_procedure(conn, proc_name):
    cursor = conn.cursor()
    cursor.callproc(proc_name)
    result = []
    for res in cursor.stored_results():
        result.extend(res.fetchall())
    cursor.close()
    return result

def render():
    set_background_from_local("assets/background.jpg")
    st.subheader("📊 Business Analyst Dashboard")
    conn = get_connection()

    # 1. Customer & Contract Count
    st.markdown("### 📋 Customer and Contract Summary")
    result = call_procedure(conn, "Customer_And_Contract_Count")
    if result:
        df_summary = pd.DataFrame(result, columns=["TotalCustomers", "TotalContracts"])
        st.metric("Total Customers", df_summary['TotalCustomers'][0])
        st.metric("Total Contracts", df_summary['TotalContracts'][0])

    # 2. Insurance Claims
    st.markdown("### 📄 Insurance Claims")
    df_claims = pd.read_sql("SELECT * FROM View_InsuranceClaim", conn)
    st.dataframe(df_claims)

    # 3. Payouts
    st.markdown("### 💸 Payout Transactions")
    df_payouts = pd.read_sql("SELECT * FROM View_Payouts", conn)
    st.dataframe(df_payouts)

    # 4. Payments
    st.markdown("### 🧾 Payment Records")
    df_payments = pd.read_sql("SELECT * FROM View_Payments", conn)
    st.dataframe(df_payments)

    # 5. Contract by Month
    st.markdown("### 📆 Contracts by Month")
    df_month = pd.read_sql("SELECT * FROM Contract_By_Month", conn)
    st.dataframe(df_month)

    # 6. Product Sales
    st.markdown("### 📦 Product Sales Summary")
    df_product = pd.read_sql("SELECT * FROM Product_Sales_Summary", conn)
    st.dataframe(df_product)

    conn.close()
