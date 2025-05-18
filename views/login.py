import streamlit as st
from utils.auth import verify_user
from visual_handler import set_background_from_local
from visual_handler import display_footer
def login():
    set_background_from_local("assets/background.jpg")

    if "user" not in st.session_state:
        st.session_state.user = None

    # Bắt đầu chia 3 cột: col1 (form), col_mid (đường chia), col2 (mô tả)
    col1, col_mid, col2 = st.columns([1, 0.05, 1])

    with col1:
        st.markdown("<h2 style='text-align: center;'>🔐 Insurance System Login</h2>", unsafe_allow_html=True)

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

    # Đường thẳng trắng chia giữa 2 cột
    with col_mid:
        st.markdown("""
            <div style="height: 100%; display: flex; justify-content: center;">
                <div style="width: 2px; background-color: white; height: 40vh;"></div>
            </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
            <div style='padding: 2rem; color: white;'>
                <h2>Insurance Management System</h2>
                <p>Track customers, manage contracts, assess claims and process payouts — all in one place.</p>
                <p style="opacity: 0.85; font-size: 0.9rem;">Please contact IT if you do not have an account.</p>
            </div>
        """, unsafe_allow_html=True)

    # CSS đảm bảo input luôn sáng rõ
    st.markdown("""
        <style>
        input, .stTextInput input {
            background-color: white !important;
            color: black !important;
            border: 1px solid #ccc !important;
            border-radius: 6px;
        }
        </style>
    """, unsafe_allow_html=True)
    
        # Nhúng CDN Font Awesome để sử dụng icon mạng xã hội
    st.markdown("""
        <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css" rel="stylesheet">
    """, unsafe_allow_html=True)

    display_footer()