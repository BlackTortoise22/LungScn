from backend.database.db import get_connection


class PredictionRepository:

    @staticmethod
    def create_prediction(
        scan_id,
        disease,
        confidence,
        heatmap_path=None,
        explanation=None,
        model_version=None
    ):

        connection = get_connection()

        cursor = connection.cursor()

        cursor.execute(
            """
            INSERT INTO predictions
            (
                scan_id,
                disease,
                confidence,
                heatmap_path,
                explanation,
                model_version
            )
            VALUES
            (%s,%s,%s,%s,%s,%s)
            """,
            (
                scan_id,
                disease,
                confidence,
                heatmap_path,
                explanation,
                model_version
            )
        )

        connection.commit()

        prediction_id = cursor.lastrowid

        cursor.close()
        connection.close()

        return prediction_id


    @staticmethod
    def get_prediction(prediction_id):

        connection = get_connection()

        cursor = connection.cursor(dictionary=True)

        cursor.execute(
            """
            SELECT *
            FROM predictions
            WHERE prediction_id=%s
            """,
            (prediction_id,)
        )

        prediction = cursor.fetchone()

        cursor.close()
        connection.close()

        return prediction


    @staticmethod
    def get_predictions_by_scan(scan_id):

        connection = get_connection()

        cursor = connection.cursor(dictionary=True)

        cursor.execute(
            """
            SELECT *
            FROM predictions
            WHERE scan_id=%s
            ORDER BY predicted_at DESC
            """,
            (scan_id,)
        )

        predictions = cursor.fetchall()

        cursor.close()
        connection.close()

        return predictions