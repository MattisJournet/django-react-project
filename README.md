
# Django React Project 

Voici le projet Django et React, pour React j'ai utilisé NextJS.
J'ai utilisé bootstrap pour sa simplicité et pour avoir un peu de css.
Et enfin j'ai volontairement laissé la db.sqlite pour ne pas avoir à recréer des users a la main




## SWAGGER

```http
  /swagger
```



## Installation
The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/OmegaFrr/django-react-project.git
$ cd django-react-project
```

### Setup for django

```sh
$ cd django_react_project
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ virtualenv venv
$ source venv/bin/activate
```

Then install the dependencies:

```sh
(venv)$ pip install -r requirements.txt
```

Once `pip` has finished downloading the dependencies:
```sh
(venv)$ python manage.py makemigrations
(venv)$ python manage.py migrate
(venv)$ python manage.py test
(venv)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/swagger/`.

#### NB : username: admin and password: admin

### Setup NextJS

```sh
$ cd django-react-project-front
```

Then install the dependencies:

```sh
$ yarn
```

Once `yarn` has finished downloading the dependencies:
```sh
$ yarn dev
or
$ yarn build
$ yarn start
```
And navigate to `http://localhost:3000/`.
