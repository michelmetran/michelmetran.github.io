---
title: "Django: *Resources*"
excerpt_separator: "<!--more-->"
tags: [python, pycharm, jupyter, package, pandas]
---

## Pandas

- [Converting Django QuerySet to pandas DataFrame](https://stackoverflow.com/questions/11697887/converting-django-queryset-to-pandas-dataframe)

<br>

---

## Plotly

- [Easy Django Plotly](https://www.codingwithricky.com/2019/08/28/easy-django-plotly/)

<br>

---

## Pandas to Model

- [**StackOverflow**: Saving a Pandas DataFrame to a Django Model](https://stackoverflow.com/questions/37688054/saving-a-pandas-dataframe-to-a-django-model)

```python
from django.conf import settings
from .defs_views import get_df_compiled
from sqlalchemy import create_engine
from datetime import date, datetime, timedelta

# Set Database
user = settings.DATABASES['default']['USER']
password = settings.DATABASES['default']['PASSWORD']
database_name = settings.DATABASES['default']['NAME']

database_url = f'postgresql://{user}:{password}@localhost:5432/{database_name}'

engine = create_engine(database_url, echo=False)
```

<br>

---

## Folium

- [Django and Folium integration](https://www.thetopsites.net/article/54173552.shtml)

<br>

---

## Erros

Encerrar o que estiver na porta 8000

```bash
sudo fuser -k 8000/tcp
```

<br>

---

## Monetizando

- [**YouTube**: How To Build Affiliate Websites With Python and Django 3.0](https://www.youtube.com/watch?v=bpSOl88fhLg&list=PLCC34OHNcOtrZnQI6ZLvGPUWfQ6oh-D6H)
