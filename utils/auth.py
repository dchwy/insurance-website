import hashlib
import mysql.connector
from utils.db import get_connection

def hash_password(password: str) -> str:
    """Hash a password using SHA256."""
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

def verify_user(username: str, password: str):
    """
    Verify user credentials.
    Returns user record with role info if valid, else None.
    """
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    try:
        query = """
            SELECT u.*, r.RoleName
            FROM Users u
            JOIN Roles r ON u.Role_id = r.Role_id
            WHERE u.Username = %s
        """
        cursor.execute(query, (username,))
        user = cursor.fetchone()
        if user and user['Password_hash'] == hash_password(password):
            return user
        return None
    finally:
        cursor.close()
        conn.close()

def get_all_roles():
    """Fetch all roles from the Roles table."""
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute("SELECT Role_id AS RoleID, RoleName FROM Roles")
        return cursor.fetchall()
    finally:
        cursor.close()
        conn.close()