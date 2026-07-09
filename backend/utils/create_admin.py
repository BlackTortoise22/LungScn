from flask_bcrypt import generate_password_hash

from backend.database.db import db_cursor


def create_admin():
    email = "admin@lungscan.com"

    with db_cursor() as cursor:
        cursor.execute(
            "SELECT * FROM users WHERE email=%s",
            (email,),
        )

        if cursor.fetchone():
            print("Admin already exists.")
            return

        password = generate_password_hash("admin123").decode("utf-8")

        cursor.execute(
            """
            INSERT INTO users
            (full_name, email, password, role)
            VALUES
            (%s, %s, %s, %s)
            """,
            (
                "Administrator",
                email,
                password,
                "Admin",
            ),
        )

    print("Admin created successfully.")


if __name__ == "__main__":
    create_admin()
