import streamlit as st
from views import (
    admin, agent, assessor, viewer,
    finance, management, product, audit, analytics
)

def dashboard():
    st.title("📊 Insurance Management Dashboard")

    user = st.session_state.get("user")
    if not user:
        st.warning("You are not logged in.")
        return
        
    st.sidebar.markdown(f"👤 **{user['FullName']}**")
    role_display = user['RoleName'].replace('_', ' ').title()
    st.sidebar.markdown(f"🔰 {role_display}")
    st.sidebar.markdown(f"📧 Email: {user['Email']}")
    st.sidebar.markdown(f"📱 Phone: {user['PhoneNumber']}")


    # 🚪 Nút đăng xuất
    if st.sidebar.button("🚪 Logout"):
        st.session_state.user = None
        st.rerun()

    role = user['RoleName'].strip().lower()

    if role == "it_admin":
        admin.render()
    elif role == "insurance_agent":
        agent.render()
    elif role == "claim_asessor":
        assessor.render()
    elif role == "finance_staff":
        finance.render()
    elif role == "manager_ceo":
        management.render()
    elif role == "product_development":
        product.render()
    elif role == "compliance_audit":
        audit.render()
    elif role == "business_analyst":
        analytics.render()
    elif role == "customer_support":
        viewer.render()
    else:
        st.error(f"Unknown role: {role}. Contact IT.")
