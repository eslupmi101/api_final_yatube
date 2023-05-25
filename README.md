# API backend for YaTube project

## Overview
YaTube is a social network in which a user can create posts, comment on them and subscribe to other users.

The repository has a v1 API backend that is made on Django REST framework.

## Requirements

1. Python 3.10
2. Django 3.2.16
3. Django REST framework 3.12.4

## Installation

Clone the repository and go to it on the command line:

```
git clone https://github.com/eslupmi101/api_final_yatube.git
```

Create and activate a virtual environment:

```
python3 -m venv env
```

```
source env/bin/activate
```

Install dependencies from a file requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Enter to django project

```
cd yatube_api
```

Perform migrations:

```
python3 manage.py migrate
```

Launch a project:

```
python3 manage.py runserver
```

# Example

Let's take a look at a quick example of using API YaTube. 

First you need to create a user through Django admin.

Get the user's JWT token via endpoint:

```
api/v1/jwt/create/

{
    'username': string,
    'password': string
}
```

Get all posts:

```
api/v1/jwt/posts/
```

Get posts of user:

```
api/v1/posts/username/
```

Create post (available only to authenticated users):

```
api/v1/jwt/posts/
```

Documentation with full functionality can be found at endpoint. 

```
api/v1/redoc/
```
