from flask_bcrypt import generate_password_hash
from backend.database.db import get_connection

connection = get_connection()
cursor = connection.cursor(dictionary=True)

email = "admin@lungscan.com"

cursor.execute(
    "SELECT * FROM users WHERE email=%s",
    (email,)
)

existing_user = cursor.fetchone()

if existing_user:
    print("✅ Admin already exists.")

else:
    password = generate_password_hash("admin123").decode("utf-8")

    cursor.execute("""
        INSERT INTO users
        (full_name, email, password, role)

        VALUES
        (%s, %s, %s, %s)
    """,
    (
        "Administrator",
        email,
        password,
        "Admin"
    ))

    connection.commit()

    print("✅ Admin created successfully.")

cursor.close()
connection.close()