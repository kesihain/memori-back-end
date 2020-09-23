# memori-back-end
This is the back end server that serves the memori mobile app. 
## Features
- can make post request to create new user
- can make post request to create new login session
- can make post request to destroy existing loging session
- can make post request to save multiple locations associated with user (jwt required)
- can make post request to save multiple reminders associated with each location (jwt required)
- can make get request to view locations data
- can make get request to view reminders data
## How to run locally?
**Download Zip or clone repo**
**Create Conda Environment**
```
conda create -n nextagram python=3.7
conda activate nextagram
```
**Install dependencies**

- Python 3.7.2 was tested
- Postgresql 10.3 was tested

1. Delete `peewee-db-evolve==3.7.0` from `requirements.txt` during the first installation.
   Because of how `peewee-db-evolve` created it's build process, we would first need to delete it.
1. Run:
   ```
   pip install -r requirements.txt
   ```
1. Now add `peewee-db-evolve==3.7.0` back into `requirements.txt`
1. Run again:
   ```
   pip install -r requirements.txt
   ```

If you're having trouble installing dependencies

- Remove `certifi==2018.11.29` from requirements.txt

If you're having trouble starting flask

- Restart your terminal as well and reactivate conda source

**Create a `.env` file at the root of the directory**

This project uses `python-dotenv`. When running commands using `flask`, environment variables from `.env` are automatically loaded.

When executing `python` scripts directly e.g. `python start.py`, environment variables are not loaded and will not work except `python migrate.py` _(read the script - `migrate.py` to know why it would load the environment variables `.env`)_

Minimum environment variables that needs to be set

```
FLASK_APP='start' # based on the name of our entry point script
FLASK_ENV='development' # use this in development, otherwise 'production' or 'test'
DATABASE_URL="postgres://localhost:5432/memori"
SECRET_KEY= #generate your own key
```

Use `os.urandom(32)` to generate a random secret key and paste that in `.env`. It's important to keep this `SECRET_KEY` private.

Since this app uses Pooled Connections, you may also want to set:

```
DB_TIMEOUT=300 # 5 minutes
DB_POOL=5
```

_(see `database.py`)_

**Create a Database**

- this application is configured to use Postgresql

```
createdb memori
```

_\*if you name your database something else, tweak the settings in `.env`_

**Ignoring Files from Git**

Before git commiting, remember to ignore key files. Here's an example of `.gitignore`

```
.vscode
*.DS_Store
*__pycache__
*.env
```

---

## Database Migrations

```
python migrate.py
```

\*_this template is configured to use Peewee's PooledConnection, however, migrations using Peewee-DB-Evolve doesn't work well. A hack was used to not use PooledConnection when running migration. Pending investigation. There are no known side effects to run this template in production._

## Starting Server
To access it on mobil you will need to 
1. run `flask run --host 0.0.0.0`
2. Open command prompt run `ipconfig`
3. Check the ipv4 url and use it as the origin for backend api endpoint call url path
Otherwise use `flask run`

## Starting Shell

```
flask shell
```

---

## Deploying to Production

- ensure environment variables are configured appropriately
- migrations will not run in interactive mode when FLASK_ENV is set to 'production'
- It's important to set your own `SECRET_KEY` environment variable and keep that private.

---

## Architecture

All new models should go into it's own file/script within the models directory.

The entry point for a Flask server to start is located at `start.py`

---

## Dependencies

This template was created against `Python 3.7`. Should work with newer versions of Python. Not tested with older versions.

`Peewee` is used as ORM along with a database migration library `peewee-db-evolve`.

This template also comes packaged with Bootstrap 4.1.3 and it's dependencies (jQuery).

A copy of requirements.txt is included in the repository.

```
autopep8==1.4.3
certifi==2018.11.29
Click==7.0
colorama==0.4.1
Flask==1.0.2
Flask-Cors==3.0.7
itsdangerous==1.1.0
Jinja2==2.10
MarkupSafe==1.1.0
peewee==3.8.2
peewee-db-evolve==3.7.0
psycopg2-binary==2.7.7
pycodestyle==2.5.0
python-dotenv==0.10.1
six==1.12.0
Werkzeug==0.14.1
```

Remove `certifi==2018.11.29` if you're having trouble installing dependencies.

---
