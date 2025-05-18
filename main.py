import streamlit as st
from views import login, dashboard

def init_session_keys():
    defaults = {
        "user": None,
        "role": None,
        "staff_id": None
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v

def main():
    st.set_page_config(page_title="Insurance Management", layout="wide")
    init_session_keys()

    if st.session_state["user"] is None:
        login.login()
    else:
        dashboard.dashboard()

if __name__ == "__main__":
    main()
