import streamlit as st
from utils.auth import verify_user

def login():
    st.title("🔐 Insurance System Login")

    if "user" not in st.session_state:
        st.session_state.user = None

    with st.form("login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submitted = st.form_submit_button("Login")

        if submitted:
            user = verify_user(username, password)
            if user:
                st.session_state.user = user
                st.success(f"Welcome, {user['FullName']} ({user['RoleName']})")
                st.rerun()
            else:
                st.error("Invalid credentials or inactive account.")

    st.info("Please contact IT if you do not have an account.")
