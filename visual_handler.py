import streamlit as st
import base64

def set_background_from_local(image_path: str):
    """
    Dùng ảnh nền từ file local (nội bộ) trong dự án Streamlit.

    Args:
        image_path (str): Đường dẫn tới ảnh (ví dụ: 'assets/background.png')
    """
    with open(image_path, "rb") as image_file:
        encoded = base64.b64encode(image_file.read()).decode()
        css = f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{encoded}");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        """
        st.markdown(css, unsafe_allow_html=True)


def display_footer():

    st.markdown("""
    <footer style="background-color: rgba(0, 0, 0, 0.7); padding: 20px; text-align: center; color: white; position: fixed; bottom: 0; left: 0; width: 100%; z-index: 9999;">
        <div style="font-size: 24px; font-weight: bold;">
            INSURANCE WEBSITE MANAGEMENT™
        </div>
        <div>
            <a href="https://www.facebook.com/profile.php?id=61567855092141&is_tour_dismissed" target="_blank">
                <i class="fab fa-facebook" style="font-size: 24px; margin: 10px;"></i>
            </a>
            <a href="https://www.instagram.com/_calm_kitchen_/" target="_blank">
                <i class="fab fa-instagram" style="font-size: 24px; margin: 10px;"></i>
            </a>
            <a href="https://twitter.com" target="_blank">
                <i class="fab fa-twitter" style="font-size: 24px; margin: 10px;"></i>
            </a>
            <a href="https://www.youtube.com/@gordonramsay" target="_blank">
                <i class="fab fa-youtube" style="font-size: 24px; margin: 10px;"></i>
            </a>
            <a href="https://www.linkedin.com" target="_blank">
                <i class="fab fa-linkedin" style="font-size: 24px; margin: 10px;"></i>
            </a>
        </div>
        <div style="margin-top: 10px;">
            <a href="/about_us" style="margin-right: 20px; text-decoration: none; color: white;">About Us</a>
            <a href="/contact_us" style="text-decoration: none; color: white;">Contact Us</a>
        </div>
        <div style="margin-top: 20px; font-size: 14px; color: #bbb;">
            Copyright © Insurance Website - DSEB 65B
        </div>
    </footer>
    """, unsafe_allow_html=True)
