import streamlit as st
import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host=st.secrets["mysql"]["host"],
        port=st.secrets["mysql"]["port"],
        user=st.secrets["mysql"]["user"],
        password=st.secrets["mysql"]["password"],
        database=st.secrets["mysql"]["database"]
    )


def call_procedure(conn, proc_name, args=()):
    cursor = conn.cursor()
    cursor.callproc(proc_name, args)
    conn.commit()
    cursor.close()
