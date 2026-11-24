import os


ADMIN_PASSWORD = os.environ.get("ADMIN_PASSWORD", "")


def check_admin(password):
    """true if the password is the admin password"""
    return ADMIN_PASSWORD != "" and password == ADMIN_PASSWORD


def find_user(db, username):
    """The user's row, or None if the username does not exist"""
    return db.execute("SELECT * FROM users WHERE username = ?", (username,)).fetchone()
