from backend.database.db import db_cursor


class AuthRepository:

    @staticmethod
    def get_user_by_email(email):
        with db_cursor() as cursor:
            cursor.execute(
                """
                SELECT *
                FROM users
                WHERE email=%s
                """,
                (email,)
            )

            return cursor.fetchone()

    @staticmethod
    def get_user_by_id(user_id):
        with db_cursor() as cursor:
            cursor.execute(
                """
                SELECT *
                FROM users
                WHERE user_id=%s
                """,
                (user_id,)
            )

            return cursor.fetchone()
