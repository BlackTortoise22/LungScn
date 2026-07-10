from backend.database.db import get_connection


class XrayScanRepository:

    @staticmethod
    def create_scan(
        patient_id,
        uploaded_by,
        image_name,
        image_path
    ):

        connection = get_connection()

        cursor = connection.cursor()

        cursor.execute(
            """
            INSERT INTO xray_scans
            (
                patient_id,
                uploaded_by,
                image_name,
                image_path
            )
            VALUES
            (%s,%s,%s,%s)
            """,
            (
                patient_id,
                uploaded_by,
                image_name,
                image_path
            )
        )

        connection.commit()

        scan_id = cursor.lastrowid

        cursor.close()
        connection.close()

        return scan_id


    @staticmethod
    def get_scan(scan_id):

        connection = get_connection()

        cursor = connection.cursor(dictionary=True)

        cursor.execute(
            """
            SELECT *
            FROM xray_scans
            WHERE scan_id=%s
            """,
            (scan_id,)
        )

        scan = cursor.fetchone()

        cursor.close()
        connection.close()

        return scan