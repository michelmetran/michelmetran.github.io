---
title: "Django: *databases*"
date: 2023-05-04T00:00:00-03:00
last_modified_at: 2023-05-04T00:00:00-03:00

excerpt_separator: "<!--more-->"
categories:
  - IT
  - Front-end
tags:
  - python,
  - pycharm
  - jupyter
  - package
  - pandas
---

É necessário definir as configurações do banco de dados do projeto.
Criei um tópico especial para tratar dessa questão.

<br>

## PostGres

É necessário criar o banco de dados com os seguintes comandos no terminal.

```sql
psql -U postgres
CREATE DATABASE opentesouro OWNER django_user;
DROP DATABASE opentesouro;
```

<br>

No arquivo **settings.py** é necessário definir as seuintes congigurações.

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'sabesp',
        'USER': 'django_user',
        'PASSWORD': '123456789',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

<br>

E, quando for utilizado o banco de dados _PostGres_, é necessário adicionar no arquivo _requirements.txt_ o

```
psycopg2==2.8.5
```

<br>

## PostGre

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'sabesp',
        'USER': 'django_user',
        'PASSWORD': '123456789',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

<br>

## MySQL

No requirements.txt deve constar:

```
mysqlclient==1.4.6
sqlalchemy~=1.3.18
sqlparse==0.3.1
```

Code

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'read_default_file': '/home/myusername/mysql_django.cnf',
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
            'isolation_level': 'read committed',
        },
    }
}
```

**Referência**

- https://averyuslaner.com/configuring-mysql-django/

<br>

## SQLite

```python
DATABASES = DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

No requirements.txt deve constar:

```

```

<br>

## Outros

- [How to Reset Migrations](https://simpleisbetterthancomplex.com/tutorial/2016/07/26/how-to-reset-migrations.html)
- [YouTube: Python Django with Firebase: Database Rules allow only Authenticated Users to Read | Write access](https://www.youtube.com/watch?v=yhYCoejo16g)
