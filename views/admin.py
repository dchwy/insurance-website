import streamlit as st
import pandas as pd
from utils.auth import hash_password, get_all_roles
from utils.db import get_connection
from views.auditlog_view import render_auditlog
from visual_handler import set_background_from_local
# Call stored procedures

def create_user(conn, username, password_hash, full_name, email, phone, role_id, staff_id):
    with conn.cursor() as cursor:
        cursor.callproc("CreateNewUser", [username, password_hash, full_name, email, phone, role_id, staff_id])
    conn.commit()

def update_user_role(conn, user_id, new_role_id):
    with conn.cursor() as cursor:
        cursor.callproc("UpdateUserRole", [user_id, new_role_id])
    conn.commit()

def delete_user(conn, user_id):
    with conn.cursor() as cursor:
        cursor.callproc("DeleteUser", [user_id])
    conn.commit()

def render():
    set_background_from_local("assets/background.jpg")
    st.markdown("""
        <style>
            .custom-email {
                color: #006400 !important;  /* DarkGreen */
                text-decoration: none;
            }
            .custom-email:hover {
                text-decoration: underline;
            }
        </style>
    """, unsafe_allow_html=True)


    st.header("👨‍💻 User Management (Admin)")

    conn = get_connection()
    roles = get_all_roles()
    role_options = {r['RoleName']: r['RoleID'] for r in roles}

    with st.expander("➕ Create New User"):
        with st.form("create_user_form"):
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")
            full_name = st.text_input("Full Name")
            email = st.text_input("Email")
            phone = st.text_input("Phone Number")
            role_name = st.selectbox("Select Role", list(role_options.keys()))
            staff_id = st.text_input("Staff ID (optional)")
            submit = st.form_submit_button("Create Account")

            if submit:
                if not username or not password or not email:
                    st.warning("Username, password and email are required.")
                else:
                    existing = pd.read_sql("SELECT * FROM Users WHERE Username = %s", conn, params=(username,))
                    if not existing.empty:
                        st.error("❌ Username already exists. Please choose another one.")
                    else:
                        try:
                            create_user(conn, username, hash_password(password), full_name, email, phone, role_options[role_name], staff_id or None)
                            st.success("✅ User account created successfully!")
                            st.rerun()
                        except Exception as e:
                            st.error(f"❌ Error: {e}")

    st.markdown("### 👥 Manage All Users")

    df_users = pd.read_sql("""
        SELECT u.User_id, u.Username, u.FullName, u.Email, u.PhoneNumber,
               r.RoleName
        FROM Users u
        JOIN Roles r ON u.Role_id = r.Role_id
        ORDER BY u.User_id DESC
    """, conn)

    for i, row in df_users.iterrows():
        if row['RoleName'] == "it_admin":
            continue
        with st.container():
            col1, col2, col3, col4, col5 = st.columns([2, 3, 2, 3, 1])
            col1.markdown(f"""
                <div style='font-size:18px; font-weight:bold;'>
                    {row['FullName']}
                </div>
            """, unsafe_allow_html=True)

            col2.markdown(f"""
                <div style='font-size:16px; color:#006400;'>
                    {row['Email']}
                </div>
            """, unsafe_allow_html=True)

            col3.markdown(f"""
                <div style='font-size:16px;'>
                    {row['PhoneNumber']}
                </div>
            """, unsafe_allow_html=True)

            current_role = row['RoleName']
            role_keys = list(role_options.keys())
            new_role = col4.selectbox(
                "Change Role",
                role_keys,
                index=role_keys.index(current_role),
                key=f"role_{row['User_id']}"
            )

            if new_role != current_role:
                try:
                    update_user_role(conn, row['User_id'], role_options[new_role])
                    st.success(f"✅ Updated role for {row['FullName']} to {new_role}")
                    st.rerun()
                except Exception as e:
                    st.error(f"❌ Error updating role: {e}")

            if col5.button("🗑", key=f"del_{row['User_id']}"):
                try:
                    delete_user(conn, row['User_id'])
                    st.warning(f"🗑 Deleted user: {row['Username']}")
                    st.rerun()
                except Exception as e:
                    st.error(f"❌ Error deleting user: {e}")
        # Thêm đường phân cách nếu chưa phải dòng cuối
        if i < len(df_users) - 1:
            st.markdown("<hr style='border-top: 1px solid white;'>", unsafe_allow_html=True)


            

    st.markdown("### 📋 View All Tables")
    table_options = [
        "Customers", "InsuranceContracts", "InsuranceClaim", "Payouts",
        "Payments", "Assessments", "PersonIncharge", "Users"
    ]

    selected_tables = st.multiselect("📂 Select tables to view", table_options)

    for table in selected_tables:
        st.markdown(f"### 📄 {table}")
        df = pd.read_sql(f"SELECT * FROM {table}", conn)
        st.dataframe(df)
    conn.close()
