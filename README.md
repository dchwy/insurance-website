## 🚀 Getting Started

### 1. Clone the project

```bash
git clone https://github.com/dchwy/insurance-website.git
cd insurance-website
```

### 2. Install Required Libraries
```
pip install -r requirements.txt
```
### 3. Configure MySQL Connection (.streamlit/secrets.toml)

Inside a folder named .streamlit, has a file named secrets.toml with the following content:
```
[mysql]
host = "localhost"
user = "root"
password = "your_mysql_password"
database = "insurance_db"
```
Replace "your_mysql_password" with your actual MySQL root password,

Name our database in SQL is: insurance_db
