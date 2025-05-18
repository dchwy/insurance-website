import streamlit as st
import pandas as pd
from utils.db import get_connection
from utils.logger import log_action
from visual_handler import set_background_from_local
def call_procedure(conn, proc_name, args=()):
    cursor = conn.cursor()
    cursor.callproc(proc_name, args)
    conn.commit()
    cursor.close()

def render():
    set_background_from_local("assets/background.jpg")
    st.subheader("🧾 Insurance Agent Dashboard")
    conn = get_connection()
    user = st.session_state.get("user", {})
    agent_id = user.get("Staff_id")
    if not agent_id:
        st.error("⚠️ No PersonInchargeID found in session.")
        st.stop()
    # 1. Create Customer
    st.markdown("### 👤 Create New Customer")
    with st.form("create_customer"):
        fn = st.text_input("First Name")
        ln = st.text_input("Last Name")
        address = st.text_input("Address")
        phone = st.text_input("Phone Number")
        gender = st.selectbox("Gender", ["Nam", "Nữ"])
        email = st.text_input("Email")
        dob = st.date_input("Date of Birth")

        if st.form_submit_button("Create Customer"):
            if not all([fn.strip(), ln.strip(), address.strip(), phone.strip(), email.strip()]):
                st.warning("⚠️ Please enter all required fields.")
            else:
                conn2 = get_connection()
                try:
                    cursor = conn2.cursor(dictionary=True)
                    cursor.callproc("Create_Customer", (fn, ln, address, phone, gender, email, dob))
                    conn2.commit()

                    customer_id = None
                    for result in cursor.stored_results():
                        row = result.fetchone()
                        if row and "CustomerID" in row:
                            customer_id = row["CustomerID"]
                            break

                    cursor.close()

                    if customer_id:
                        st.session_state["new_customer_id"] = customer_id
                        log_action(conn2, user, "CREATE_CUSTOMER", f"{fn} {ln} ({email}) - ID: {customer_id}")
                        st.rerun()
                    else:
                        st.error("❌ Failed to retrieve CustomerID.")
                except Exception as e:
                    st.error(f"❌ Error: {e}")
                finally:
                    conn2.close()

    # ✅ Đặt đoạn này sau form, ngoài if
    if "new_customer_id" in st.session_state:
        st.success(f"✅ Customer created with ID: {st.session_state['new_customer_id']}")
        del st.session_state["new_customer_id"]


    # 2. Create Insurance Contract
    st.markdown("### 📄 Create New Insurance Contract")
    with st.form("create_contract"):
        customer_id = st.text_input("Customer ID")
        insurance_type_id = st.text_input("Insurance Type ID")
        sign_date = st.date_input("Sign Date")
        effective = st.date_input("Effective Date")
        expiry = st.date_input("Expiration Date")

        if st.form_submit_button("Create Contract"):
            if not all([customer_id.strip(), insurance_type_id.strip()]):
                st.warning("⚠️ Please enter both Customer ID and Insurance Type ID.")
            else:
                conn2 = get_connection()
                try:
                    cursor = conn2.cursor(dictionary=True)
                    cursor.callproc("Create_Insurance_Contract", (
                        customer_id, insurance_type_id, agent_id, sign_date, effective, expiry
                    ))
                    conn2.commit()

                    contract_id = None
                    for result in cursor.stored_results():
                        row = result.fetchone()
                        if row and "ContractID" in row:
                            contract_id = row["ContractID"]
                            break

                    cursor.close()

                    if contract_id:
                        st.session_state["new_contract_id"] = contract_id
                        log_action(conn2, user, "CREATE_CONTRACT", f"{contract_id} for customer {customer_id}")
                        st.rerun()
                    else:
                        st.error("❌ Failed to retrieve ContractID.")
                except Exception as e:
                    st.error(f"❌ Error: {e}")
                finally:
                    conn2.close()

    # ✅ Hiển thị sau khi rerun
    if "new_contract_id" in st.session_state:
        st.success(f"✅ Contract created with ID: {st.session_state['new_contract_id']}")
        del st.session_state["new_contract_id"]


    # 3. View contracts assigned to this agent
    st.markdown("### 📋 Your Contracts")
    df_contracts = pd.read_sql(f"CALL Contract_By_Person('{agent_id}')", conn)
    st.dataframe(df_contracts)

    # 4. View contract details for customer
    st.markdown("### 🔍 Get Contract Details by Customer ID")
    customer_lookup = st.text_input("Enter Customer ID", key="details_lookup")
    if st.button("View Contract Details"):
        conn = get_connection()  # ✅ Lấy kết nối tươi mới
        try:
            df_detail = pd.read_sql(f"CALL Get_ContractDetails('{customer_lookup}')", conn)
            st.dataframe(df_detail)
        except Exception as e:
            st.error(f"❌ Error: {e}")
        finally:
            conn.close()


    # 5. View payout by contract
    st.markdown("### 💸 Payout Details by Contract ID")
    contract_lookup = st.text_input("Enter Contract ID", key="payout_lookup")

    if st.button("View Payout Details"):
        if not contract_lookup:
            st.warning("⚠️ Please enter a contract ID.")
        else:
            try:
                conn2 = get_connection()  # 🔁 lấy lại kết nối tươi
                df_payout = pd.read_sql(f"CALL Payout_Detail_Summary('{contract_lookup}')", conn2)
                if df_payout.empty:
                    st.info("No payout data found for this contract.")
                else:
                    st.dataframe(df_payout)
            except Exception as e:
                st.error(f"❌ Error while retrieving payout: {e}")
            finally:
                conn2.close()
    #6
    st.markdown("### 👨 Add Insured Person")
    with st.form("add_insured_person"):
        contract = st.text_input("Contract ID", key="ip1")
        first = st.text_input("First Name", key="ip2")
        last = st.text_input("Last Name", key="ip3")
        phone = st.text_input("Phone Number", key="ip4")
        dob = st.date_input("DOB", key="ip5")
        gender = st.selectbox("Gender", ["Nam", "Nữ"], key="ip6")
        email = st.text_input("Email", key="ip7")
        addr = st.text_input("Address", key="ip8")

        if st.form_submit_button("Add Person"):
            if not all([contract.strip(), first.strip(), last.strip()]):
                st.warning("⚠️ Please fill in all required fields.")
            else:
                try:
                    conn2 = get_connection()
                    call_procedure(conn2, "Insert_InsuredPerson", (contract, first, last, phone, dob, gender, email, addr))
                    log_action(conn2, user, "ADD_INSURED_PERSON", f"{first} {last} in contract {contract}")
                    st.success("✅ Insured person added.")
                except Exception as e:
                    st.error(f"❌ Error: {e}")
                finally:
                    conn2.close()
                    
    st.markdown("### 🚗 Add Insured Car")
    with st.form("add_car"):
        contract = st.text_input("Contract ID", key="car1")
        name = st.text_input("Vehicle Name", key="car2")
        value = st.number_input("Vehicle Value", key="car3", min_value=0.0)
        plate = st.text_input("License Plate", key="car4")
        year = st.date_input("Manufacture Year", key="car5")

        if st.form_submit_button("Add Car"):
            if not all([contract.strip(), name.strip(), plate.strip()]):
                st.warning("⚠️ Please fill in all required fields.")
            else:
                try:
                    conn2 = get_connection()
                    call_procedure(conn2, "Insert_InsuredCar", (contract, name, value, plate, year))
                    log_action(conn2, user, "ADD_INSURED_CAR", f"{plate} - {name} in contract {contract}")
                    st.success("✅ Car added.")
                except Exception as e:
                    st.error(f"❌ Error: {e}")
                finally:
                    conn2.close()


    # 8. Add insured home
    st.markdown("### 🏠 Add Insured Home")
    with st.form("add_home"):
        contract = st.text_input("Contract ID", key="home1")
        address = st.text_input("Address", key="home2")
        prop_type = st.selectbox("Property Type", ["Apartment", "House", "Villa"], key="home3")
        area = st.number_input("Area (m²)", key="home4")
        year = st.date_input("Year Built", key="home5")
        value = st.number_input("Property Value", key="home6", min_value=0.0)

        if st.form_submit_button("Add Home"):
            if not contract.strip() or not address.strip():
                st.warning("⚠️ Please fill in all required fields.")
            else:
                try:
                    conn2 = get_connection()
                    call_procedure(conn2, "Insert_InsuredHome", (contract, address, prop_type, area, year, value))
                    log_action(conn2, user, "ADD_INSURED_HOME", f"{address}, type {prop_type}, value {value}")
                    st.success("✅ Home added.")
                except Exception as e:
                    st.error(f"❌ Error: {e}")
                finally:
                    conn2.close()

    # 9. Add beneficiary
    st.markdown("### 👥 Add Beneficiary")
    with st.form("add_beneficiary"):
        contract = st.text_input("Contract ID", key="ben1")
        ben_id = st.text_input("Beneficiary ID", key="ben2")
        first = st.text_input("First Name", key="ben3")
        last = st.text_input("Last Name", key="ben4")
        phone = st.text_input("Phone Number", key="ben5")
        dob = st.date_input("DOB", key="ben6")
        gender = st.selectbox("Gender", ["Nam", "Nữ"], key="ben7")
        email = st.text_input("Email", key="ben8")
        addr = st.text_input("Address", key="ben9")
        percent = st.number_input("Percentage (%)", 0.0, 100.0, key="ben10")

        if st.form_submit_button("Add Beneficiary"):
            if not all([contract.strip(), ben_id.strip(), first.strip(), last.strip()]):
                st.warning("⚠️ Please fill in all required fields.")
            else:
                try:
                    conn2 = get_connection()
                    call_procedure(conn2, "Insert_Beneficiary", (
                        contract, ben_id, first, last, phone, dob, gender, email, addr, percent
                    ))
                    log_action(conn2, user, "ADD_BENEFICIARY", f"{first} {last} - {percent}% in contract {contract}")
                    st.success("✅ Beneficiary added.")
                except Exception as e:
                    st.error(f"❌ Error: {e}")
                finally:
                    conn2.close()


    conn.close()
