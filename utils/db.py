import mysql.connector
import streamlit as st

def get_connection():
    """
    Create and return a MySQL database connection using Streamlit secrets.
    Make sure you have a `.streamlit/secrets.toml` file like this:

    [mysql]
    host = "localhost"
    user = "root"
    password = "your_password"
    database = "insurance_db"
    """
    return mysql.connector.connect(
        host=st.secrets["mysql"]["host"],
        user=st.secrets["mysql"]["user"],
        password=st.secrets["mysql"]["password"],
        database=st.secrets["mysql"]["database"]
    )
