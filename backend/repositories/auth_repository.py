from backend.database.db import get_connection


class AuthRepository:

    @staticmethod
    def get_user_by_email(email):

        connection = get_connection()

        cursor = connection.cursor(dictionary=True)

        cursor.execute(
            """
            SELECT *
            FROM users
            WHERE email=%s
            """,
            (email,)
        )

        user = cursor.fetchone()

        cursor.close()
        connection.close()

        return user

    @staticmethod
    def get_user_by_id(user_id):

        connection = get_connection()

        cursor = connection.cursor(dictionary=True)

        cursor.execute(
            """
            SELECT *
            FROM users
            WHERE user_id=%s
            """,
            (user_id,)
        )

        user = cursor.fetchone()

        cursor.close()
        connection.close()

        return user