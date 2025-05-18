import streamlit as st
from views import login, dashboard

def main():
    st.set_page_config(page_title="Insurance Management", layout="wide")

    if "user" not in st.session_state:
        st.session_state["user"] = None

    if st.session_state["user"] is None:
        login.login()
    else:
        dashboard.dashboard()

if __name__ == "__main__":
    main()
