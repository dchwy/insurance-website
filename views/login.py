import streamlit as st
from utils.auth import verify_user
from visual_handler import set_background_from_local
from visual_handler import display_footer

def init_session_keys():
    defaults = {
        "user": None,
        "role": None,
        "staff_id": None
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v
            
            
def login():
    set_background_from_local("assets/background.jpg")

    init_session_keys()

    # Tiêu đề lớn nằm trên đầu, căn giữa toàn bộ trang
    st.markdown("<h1 style='text-align: center; color: white; margin-top: -2rem; margin-bottom: 0rem;'>Insurance Management System</h1>", unsafe_allow_html=True)

    # Tạo cột duy nhất căn giữa trang, độ rộng 40%
    col = st.columns([1, 2, 1])[1]  # cột giữa rộng hơn, 2 phần, 2 cột 2 bên là 1 phần

    with col:
        st.markdown("<h3 style='text-align: center; color: white; margin-top: 0rem;'>🔐 Insurance System Login</h3>", unsafe_allow_html=True)
        st.markdown("""
            <style>
            .login-form-container {
                max-width: 200px !important;
                margin-left: auto !important;
                margin-right: auto !important;
                border-radius: 20px !important;
                background-color: rgba(255,255,255,0.15) !important;
            }
            .login-form-container .stTextInput>div>div>input {
                width: 50% !important;
                border-radius: 15px !important;
                padding: 8px !important;
                box-sizing: border-box !important;
            }
            .login-form-container button[kind="primary"] {
                width: 50% !important;
                border-radius: 15px !important;
                padding: 10px 0 !important;
                font-size: 16px !important;
            }
            </style>
            <div class="login-form-container">
            """, unsafe_allow_html=True)


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

            # Dòng contact IT nằm dưới nút Login
            st.markdown("<p style='color: white; text-align: center; margin-top: 10px;'>Please contact IT if you do not have an account.</p>", unsafe_allow_html=True)

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