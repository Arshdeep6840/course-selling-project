# How to Run the Project

To run this project on your local machine, please follow the steps below.

## Prerequisites

*   Python 3.x
*   pip (Python package installer)
*   Git

## 1. Clone the Repository

First, clone the project repository from GitHub to your local machine:

```bash
git clone https://github.com/Arshdeep6840/course-selling-project.git
cd course-selling-project
```

## 2. Set Up a Virtual Environment

It is highly recommended to use a virtual environment to manage the project's dependencies. Create and activate a virtual environment using the following commands:

```bash
# Create a virtual environment
python -m venv .venv

# Activate the virtual environment
source .venv/bin/activate
```

## 3. Install Dependencies

With the virtual environment activated, install the required packages from the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

## 4. Set Up the Database

This project uses a SQLite database. To set up the database and apply the initial migrations, run the following commands:

```bash
# Apply database migrations
alembic upgrade head
```

## 5. Seed the Database with Sample Data

To populate the database with sample courses and videos, run the `seed.py` script:

```bash
python seed.py
```

This will add 20 demo courses and 100 demo videos to the database.

## 6. Run the Flask Development Server

Finally, you can start the Flask development server to run the application:

```bash
python main.py
```

The application will be accessible at `http://127.0.0.1:5000` in your web browser.

## 7. (Optional) Create a Superuser

To access the admin panel, you can create a superuser account by following these steps:

1.  Run the following command in the terminal:

    ```bash
    python
    ```

2.  In the Python interpreter, run the following commands:

    ```python
    from main import app, db
    from users.models import User

    with app.app_context():
        user = User(username='admin', email='admin@example.com', password='adminpassword', is_admin=True)
        db.session.add(user)
        db.session.commit()
    ```

    You can now log in with the username `admin` and password `adminpassword`.
