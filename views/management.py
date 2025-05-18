import streamlit as st
import pandas as pd
from utils.db import get_connection, call_procedure
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
        
    # 1. Revenue by Month
    st.markdown("## 📅 Revenue by Month")
    try:
        df_month = pd.read_sql("CALL Revenue_By_Month()", conn)
        st.line_chart(df_month.set_index("Month"))
    except Exception as e:
        st.error(f"❌ Failed to load monthly revenue: {e}")

    # 2. Revenue by Year
    st.markdown("## 🗓 Revenue by Year")
    try:
        conn = get_connection()
        df_year = pd.read_sql("CALL Revenue_By_Year()", conn)
        st.bar_chart(df_year.set_index("Year"))
    except Exception as e:
        st.error(f"❌ Failed to load yearly revenue: {e}")
    finally:
        conn.close()

    # 3. Top Insurance Types by Revenue
    st.markdown("## 🏆 Top Insurance Types by Revenue")
    try:
        conn = get_connection()
        df_type = pd.read_sql("CALL Top_InsuranceType_By_Revenue()", conn)
        st.dataframe(df_type)
    except Exception as e:
        st.error(f"❌ Failed to load insurance type revenue: {e}")
    finally:
        conn.close()


    st.markdown("### 🎯 Overall Claim Success Rate")
    conn = get_connection()
    rate = call_procedure(conn, "Get_ClaimSuccessRate")
    if rate and rate[0][0] is not None:
        st.metric("Claim Success Rate (%)", f"{rate[0][0]:.2f}")
    else:
        st.warning("Không có dữ liệu tỷ lệ thành công.")
    conn.close()
