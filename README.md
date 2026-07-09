# LungScan AI

LungScan AI is a Flask-based workspace for managing patients, uploading chest X-rays, reviewing AI-assisted lung disease predictions, and preparing diagnostic reports.

## What is included

- Flask application factory with authentication, dashboard, patient, prediction, report, analytics, and public routes
- MySQL schema for users, patients, scans, predictions, reports, and login logs
- Server-rendered Bootstrap UI with shared layouts and reusable Jinja components
- Safer configuration defaults and database cursor cleanup helpers

## Setup

1. Create and activate a virtual environment.

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install dependencies.

```powershell
pip install -r backend\requirements.txt
```

3. Create a `.env` file from `.env.example` and update the database credentials.

4. Create and seed the database.

```powershell
mysql -u root -p < database\schema.sql
mysql -u root -p < database\seed.sql
```

5. Run the app.

```powershell
python -m backend.app
```

The app runs at `http://localhost:5000`.

## Demo accounts

The seed file includes default users. Replace these credentials before using the app outside local development.

- Admin: `admin@lungscan.com`
- Doctor: `doctor@lungscan.com`

## Project structure

- `backend/app.py` starts the Flask server.
- `backend/__init__.py` creates and configures the app.
- `backend/routes/` contains route blueprints.
- `backend/templates/` contains Jinja pages and shared UI components.
- `backend/static/` contains CSS and JavaScript assets.
- `database/` contains schema and seed SQL files.
