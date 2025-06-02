## 📌 Overview
This project is a comprehensive Database Management System (DBMS) solution for managing insurance-related operations including customer profiles, insurance contracts, claims, assessments, payouts, etc...

## 🗃️ Technologies Used
Database: MySQL

Language: Python

Tools: MySQL Workbench, mysql-connector-python

Security: Role-based access, data encryption

## 👥 Team
This project was developed by a team of 4 students from DSEB - NATIONAL ECONOMICS UNIVERSITY:
* NGuyen Danh Dung
* Pham Khanh Duong
* Bui Viet Huy
* Do Cong Huy

## 🚀 Setup & Run

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/insurance-dbms.git
cd insurance-dbms
```

### 2. Set up the database

* Import the SQL schema and sample data into your MySQL server:

```bash
mysql -u your_username -p < schema.sql
```

### 3. Configure Python environment

* Install required dependencies:

```bash
pip install -r requirements.txt
```

* Update the database connection settings in `config.py`:

```python
DB_CONFIG = {
    'host': 'localhost',
    'user': 'your_username',
    'password': 'your_password',
    'database': 'insurance_db'
}
```

### 4. Run the application

```bash
python3 app/main.py
```
[[HERE IS THE LINK FOR USER](https://insurance-demo-w.streamlit.app/)]
[Testing Accounts](https://docs.google.com/spreadsheets/d/1IuyoQLqaKyXApejXfgvRytfD7C2lYDxo9do4ZZawtsA/edit?usp=sharing)
