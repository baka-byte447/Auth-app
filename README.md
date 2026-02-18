# Flask Authentication App

A minimalist authentication application built with Flask. This project demonstrates basic user registration, login, and session management using Flask and SQLAlchemy.

## Features

- User registration and login
- Password hashing with `bcrypt`
- Persisting user data with `Flask-SQLAlchemy`
- Simple templates using Jinja2

## Requirements

See `requirements.txt` for the list of dependencies. Install them with:

```bash
pip install -r requirements.txt
```

## Running the Application

1. Create and activate a Python virtual environment.
2. Ensure the `requirements.txt` dependencies are installed.
3. Set environment variables if needed (e.g., `FLASK_APP=app.py`, `FLASK_ENV=development`).
4. Run the application:

```bash
flask run
```

or using the provided `activate.bat` on Windows:

```bash
activate.bat
python app.py
```

## Templates

The app uses a handful of simple HTML templates located in the `templates/` directory:

- `base.html` – common layout
- `index.html` – home page
- `register.html` – registration form
- `login.html` – login form
- `dashboard.html` – protected user dashboard
