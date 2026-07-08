from flask import Flask

from backend.database.db import get_connection

app = Flask(__name__)


@app.route("/")
def home():

    try:

        connection = get_connection()

        if connection.is_connected():

            connection.close()

            return "✅ LungScan successfully connected to MySQL."

    except Exception as e:

        return f"Database Connection Error: {e}"


if __name__ == "__main__":

    app.run(debug=True)