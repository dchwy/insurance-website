import streamlit as st
import pandas as pd
import uuid
from utils.auth import hash_password, get_all_roles
from utils.db import get_connection

def render():
    st.header("👨‍💻 User Management (Admin)")

    conn = get_connection()
    roles = get_all_roles()
    role_options = {r['RoleName']: r['RoleID'] for r in roles}

 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #    # 
    with st.expander("➕ Create New User"):
        with st.form("create_user_form"):
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")
            full_name = st.text_input("Full Name")
            email = st.text_input("Email")
            phone = st.text_input("Phone Number")
            role_name = st.selectbox("Select Role", list(role_options.keys()))
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
                            with conn.cursor() as cursor:
                                cursor.execute("""
                                    INSERT INTO Users (UserID, Username, PasswordHash, FullName, Email, PhoneNumber, RoleID, Status)
                                    VALUES (%s, %s, %s, %s, %s, %s, %s, 'active')
                                """, (
                                    str(uuid.uuid4()), username, hash_password(password),
                                    full_name, email, phone, role_options[role_name]
                                ))
                                conn.commit()
                                st.success("✅ User account created successfully!")
                                st.rerun()
                        except Exception as e:
                            conn.rollback()
                            st.error(f"❌ Error: {e}")


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
    st.markdown("### 👥 Manage All Users")

    df_users = pd.read_sql("""
        SELECT u.UserID, u.Username, u.FullName, u.Email, u.PhoneNumber,
                r.RoleName, u.Status, u.CreatedAt

        FROM Users u
        JOIN Roles r ON u.RoleID = r.RoleID
        ORDER BY u.CreatedAt DESC
    """, conn)

    st.markdown("#### 🧾 User Table")
    st.write("You can change role or delete users below:")

    for i, row in df_users.iterrows():
        if row['RoleName'] == "it_admin":
            continue  
        with st.container():
            col1, col2, col3, col4, col5 = st.columns([2, 3, 2, 3, 1])

            col1.markdown(f"**{row['FullName']}**")
            col2.markdown(row['Email'])
            col3.markdown(row['PhoneNumber'])

            current_role = row['RoleName']
            role_keys = list(role_options.keys())
            new_role = col4.selectbox(
                "Change Role",
                role_keys,
                index=role_keys.index(current_role),
                key=f"role_{row['UserID']}"
            )

            if new_role != current_role:
                with conn.cursor() as cursor:
                    cursor.execute(
                        "UPDATE Users SET RoleID = %s WHERE UserID = %s",
                        (role_options[new_role], row['UserID'])
                    )
                    conn.commit()
                    st.success(f"✅ Updated role for {row['FullName']} to {new_role}")
                    st.rerun()

            if col5.button("🗑", key=f"del_{row['UserID']}"):
                with conn.cursor() as cursor:
                    cursor.execute("DELETE FROM Users WHERE UserID = %s", (row['UserID'],))
                    conn.commit()
                    st.warning(f"🗑 Deleted user: {row['Username']}")
                    st.rerun()

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
    st.markdown("## 📂 All System Data Views")

    all_views = [
        "ActiveContracts", "PendingClaims", "PayoutSummary", "PendingPayments",
        "CustomerContractCount", "ContractPaymentSummary", "ExpiringContracts",
        "ClaimSuccessRateSummary", "ContractPerformanceSummary",
        "ProductSalesSummary", "InsuranceTypePerformanceSummary"
    ]

    for view_name in all_views:
        with st.expander(f"📄 View: {view_name}"):
            try:
                df = pd.read_sql(f"SELECT * FROM {view_name}", conn)
                st.dataframe(df)
            except Exception as e:
                st.error(f"❌ Failed to load view `{view_name}`: {e}")

    conn.close()
