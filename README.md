Overview
========
Flask server for [tablet app](https://github.com/emtseng/hcw-hf) designed for home health aides in NYC.

Configuration
=============
- Create a file `secret_keys.py` at the project root (such that you have `hcw-flask/secret_keys.py` not `hcw-flask/hcw-flask/secret_keys.py`)
- Inside the file, define variable `SQLALCHEMY_DATABASE_URI` (e.g. `SQLALCHEMY_DATABASE_URI = "sqlite:///students.sqlite3"`)

Run
===
- Create a [virtualenv](https://virtualenv.pypa.io/en/latest/) (using python3)
- `pip install -r requirements.txt`
- `python manage.py runserver`
- Go to [localhost:5500]

# Database
- Install Postgres on your machine, login and create a database for your project:
    - Installation: (mac: `brew install postgres`; Ubuntu: `sudo apt-get install postgresql postgresql-contrib`)
    - Login into shell using postgres admin user (mac:`psql` or `psql -U postgres`; Ubuntu: `sudo su - postgres`)
    - Create your database (`CREATE DATABASE your_db_name;`) *NB: semi-colon is required.*
    - Create user and strong password (`CREATE USER your_user WITH PASSWORD 'your_password';)
    - Update settings of user role:
        ```
        ALTER ROLE your_user SET client_encoding TO 'utf8';
        ALTER ROLE your_user SET default_transaction_isolation TO 'read committed';
        ALTER ROLE your_user SET timezone TO 'UTC';
        ```
    - Grant user rights: `GRANT ALL PRIVILEGES ON DATABASE your_db_name TO your_user;`
- If you don't already have psycopg2 in your virtualenv, install it using: `pip install psycopg2`
- Make migrations:
    ```
    python manage.py db init # create migrations folder
    python manage.py db migrate
    python manage.py db upgrade
    ```
