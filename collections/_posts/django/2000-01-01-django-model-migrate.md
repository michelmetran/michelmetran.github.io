---
title: "Django: <i>model and migrate</i>"
date: 2019-06-13T15:34:30-04:00
last_modified_at: 2022-06-28T00:00:00-03:00
excerpt_separator: "<!--more-->"
categories:
  - IT
  - Front-end
tags:
  - python
  - pycharm
  - jupyter
  - package
  - pandas
---

# Models.py

- https://docs.djangoproject.com/en/3.0/ref/models/

```python
class Evento(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    data_evento = models.DateTimeField(verbose_name='Data do Evento')
    data_criacao = models.DateTimeField(auto_now=True, verbose_name='Data da Criação')

    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    id_outr = models.UUIDField(primary_key=True, default=uuid4, editable=false)

    class Meta:
        db_table = 'evento'

    def __str__(self):
        return self.titulo
```

<br>

Algumas das opções que podem ser contidas no banco de dados são:

```python
auto_created=True,
primary_key=True,
serialize=False,
verbose_name='ID'
```

<br>

---

# _Migrations_

<br>

## _Make Migrations_

Não migra os models às cegas

```bash
python manage.py makemigrations
python manage.py makemigrations {app name}
python manage.py makemigrations core
```

<br>

## _SQL Migrate_

Gera os códigos que deverão ser gerados para criar as tabelas no banco de dados...
Mais transparência...

```bash
python manage.py sqlmigrate
python manage.py sqlmigrate core 0001
```

<br>

## _Migrate_

```bash
python manage.py migrate
```
