---
title: "Django: *REST*"
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

Com o objetivo de estudar maneiras de usar os dados do modelo em um formato _json_, similar ao output de uma API, fui estudar como serializar dados do Django.

A meta é usar o **Django Rest Framework** no final, mas para isso quero estudar alternativas mais simples.

A primeira alternativa é

<br>

---

## Json de um _dataframe_

url.py

```python
# Consultar: URL/api_df
path('api_df', views_admin.go_api_dataframe, name='go_api_pandas'),
```

<br>

views.py

```python
def go_api_dataframe(request):
    # Using Pandas
    details = {
        'Name': ['Ankit', 'Aishwarya', 'Shaurya', 'Shivangi'],
        'Age': [23, 21, 22, 21],
        'University': ['BHU', 'JNU', 'DU', 'BHU'],
    }
    df = pd.DataFrame(details)
    result = df.to_json(orient='records')
    parsed = json.loads(result)
    return JsonResponse(parsed, safe=False)

```

<br>

---

## Json de um _model_

- [Outputting a Django queryset as JSON](https://www.yellowduck.be/posts/outputting-django-queryset-json)

url.py

```python
# Consultar: URL/api_model
path('api_model', views_admin.go_api_model, name='go_api_modelo'),
```

<br>

views.py

```python
def go_api_model(request):
    # Using Model
    return JsonResponse(
        list(Students.objects.all().values()),
        safe=False,
        content_type='application/json'
    )
```

<br>

---

## Django Rest Framework

- https://www.django-rest-framework.org

<br>

```bash
pip3 install djangorestframework
```

```python
INSTALLED_APPS = [
    ...
    'rest_framework',
]
```

<br>

---

### Referências

- [Django Rest Framework](http://www.django-rest-framework.org/)
- [**YouTube**: Django + Chart.js // Learn to intergrate Chart.js with Django](https://www.youtube.com/watch?v=B4Vmm3yZPgc)



<br>

---

### dddd

```python
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework.authentication.SessionAuthentication",
    ),
}
```

```bash
# Testes
curl -X GET --user {username}:{password} http://localhost:8000/api_rest2

# dddd
curl -X GET --user michelmetran@gmail.com:111 http://localhost:8000/api_rest2 >> output-file.json

# Servidor Local, com Autenticação
curl -X GET --user michelmetran@gmail.com:111 http://localhost:8000/api/rest/?format=json >> output-file.json

# Servidor Heroku, com Autenticação
curl -X GET --user michelmetran@gmail.com:111 https://openescola.herokuapp.com/api/rest/?format=json >> output-file.json

# Servidor Heroku, sem Autenticação
curl -X GET https://openescola.herokuapp.com/api/rest/?format=json >> output-file.json
```
