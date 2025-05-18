from utils.db import call_procedure

def log_action(conn, user, action, detail):
    """
    Ghi log hành động của user vào bảng AuditLog, nếu có user_id.
    Không ghi nếu thiếu dữ liệu quan trọng.
    """
    if not user or not user.get("user_id"):
        return  # Không log nếu chưa login

    if not action or not isinstance(action, str):
        return  # Không log nếu action trống hoặc không hợp lệ

    try:
        call_procedure(conn, "LogAction", (
            user["user_id"], action, detail or ""
        ))
    except Exception as e:
        print(f"[LogAction] Failed to log: {e}")
