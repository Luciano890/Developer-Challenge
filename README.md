# Developer Challenge

## by Luciano Chavarria

* [x] Registering and managing property owners and their properties
* [x] Creation of models for owners: id, individuals or companies; estates: cadastral identification number, address or name, real estate registration number, type of property.
* [x] allows you to search and filter data

### Table of Contents:

1. [About the project](#About-the-project)
2. [Getting Started](#Getting-Started)
    - [Prerequisites](#Prerequisites)
    - [Installation](#Installation)
3. [Usage](#Usage)
4. [Contact](#Contact)

---

## About the project

This is a very simple app with a login and registration system, made in Django for ARkandha's developer challenge.

---

## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

* PostgresSQL

### Installation

1. Clone the repo

`git clone https://github.com/Luciano890/Developer-Challenge.git`

2. In the clone folder create a virtual environment

```cmd
py -m venv venv
# or
python -m venv venv
# or
python3 -m venv venv
```

3. Install requirements

`pip install -r requirements/requirements.txt`

4. Create database on PostgresSQL

`CREATE DATABASE estatesdb;`

5. Enter at DeveloperChallenge folder and configure database settings on local_settings.py or settings.py

```python
# settings.py

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'estatesdb',
        'USER': 'postgres', #your user
        'PASSWORD': '1234', #your password
        'HOST': 'localhost', #your localhost
        'PORT': '', #your port
    }
}
```

6. From todo_django run

```cmd
py manage.py makemigrations
py manage.py migrate
# or
python manage.py makemigrations
python manage.py migrate
# or
python3 manage.py makemigrations
python3 manage.py migrate
```

7. Create a superuser

```cmd
 py manage.py createsuperuser
 # or
 python manage.py createsuperuser
 # or
 python3 manage.py createsuperuser
```

8. Run server

```cmd
py manage.py runserver
# or
python manage.py runserver
# or
python3 manage.py runserver
```
---

## Usage

Once the app is installed, you can access the `localhost:8000/admin` path and enter the administrator with the super user, you can also enter the app with that user by going to `localhost:8000/register` or loging at `localhost:8000/login`

---

## Contact

Project Link: https://github.com/Luciano890/Developer-Challenge.git
