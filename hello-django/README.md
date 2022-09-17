Hello Django

url: https://enigmatic-mesa-20649.herokuapp.com/

# Install Django

https://djangoforbeginners.com/initial-setup/

## First Django Project

A Django project can have almost any name but we will use django_project in this book. To create a new Django project use the command django-admin startproject django_project .

```console
(.venv) > django-admin startproject django_project .
```
It’s worth pausing here to explain why you should add a period (`.`) to the end of the previous command. If you just run `django-admin startproject django_project` then by default Django will create this directory structure:


```console
django_project/
    ├── django_project
    │   ├── __init__.py
    │   ├── asgi.py
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    ├── manage.py
    └── .venv/
```

Do you see the multiple `django_project` directories? First a top-level `django_project` directory is created and then *another* one within it that contains the files we need for our Django project. This feels redundant to me which is why I prefer adding a period to the end which installs Django in the current directory.

```console
├── django_project
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
└── .venv/
```

Now let’s confirm everything is working by running Django’s internal web server via the runserver command. This is suitable for local development purposes, but when it comes time to deploy our project’s online we will switch to a more robust WSGI server like Gunicorn.

```
# Windows
(.venv) > python manage.py runserver

# macOS
(.venv) % python3 manage.py runserver

Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

You have 18 unapplied migration(s). Your project may not work properly until
you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.

December 12, 2021 - 15:26:23
Django version 4.0.0, using settings 'django_project.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-BREAK.
```
Don’t worry about the text in red about `18 unapplied migrations`. We’ll get to that shortly. The important part, for now, is to visit `http://127.0.0.1:8000/` in your web browser.

If you are on Windows you’ll see the final line says to use `CONTROL-BREAK` to quit whereas on macOS it is `CONTROL-C`. Newer Windows keyboards often do not have a Pause/Break key in which case using the c key usually works.

The complete Django flow looks like this:

`
HTTP Request -> URL -> View -> Model and Template -> HTTP Response
`


PG Admin config path

```console
sudo vim /var/lib/pgsql/data/pg_hba.conf

```

postgresql config path

```console
sudo vim /var/lib/pgsql/data/postgresql.conf
```

```console
sudo service postgresql restart
sudo service postgresql stop

sudo systemctl status postgresql
sudo systemctl restart postgresql

```

## drf-yasg - Yet Another Swagger Generator
drf-yasg is a Swagger generation tool implemented without using the schema generation provided by Django Rest Framework.

**open Swagger UI**

```console
#google chrome
google-chrome http://localhost:8000/swagger/
#firefox 
firefox localhost:8000/swagger/
```

## Config database

Config your database:
`DATABASES` in **django_project/settings.py**

## Create database

Run the following commands:

```console
docker exec -it django-docker-sample_db_1 /bin/bash
```

```console
bash /usr/src/creat_scripts.sh
```

```console
bash /usr/src/import_data.sh
```

Exit container:

```console
exit
```

Hero information use `pages_hero` table (table of model django).

Player information used `player` table (table of database).

## Run services

```console
docker-compose up
```


## Model serializer
To convert the Model object to an API-appropriate format like JSON, Django REST framework uses the ModelSerializer class to convert any model to serialized JSON objects:


## Link
http://127.0.0.1:8000/players/19813.0/

http://127.0.0.1:8000/heroes/13/

http://localhost:8000/redoc/

http://localhost:8000/swagger/

http://127.0.0.1:8000/api/heroes

http://127.0.0.1:8000/api/heroes/5

http://127.0.0.1:8000/api/players/4320

~http://127.0.0.1:8000/api/players(too late)