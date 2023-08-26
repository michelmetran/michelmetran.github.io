---
title: "Django"
date: 2023-05-04T00:00:00-03:00
last_modified_at: 2023-05-04T00:00:00-03:00
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

<br>

# Install

django-admin --help

Para instalar

```bash
pip3 install django
pip3 install django --upgrade
```

<br>

---

# _Create_

## _Create Project_

Primeira coisa a fazer é criar um projeto com o _framework_ do Django. Isso é feito com o seguinte comando, no terminal:

```bash
django-admin startproject {project name}
cd {project name}
```

<br>

## _Create Aplication_

Uma vez criado o projeto, é necessário adicionar uma aplicação ao projeto, com o comando abaixo.
O nome convencionado **_core_** pode ser alterado. Vi em tutoriais e aprendi assim. Achei adequado, visto que é, de fato, o **_core_** da aplicação.

```bash
python manage.py startapp core
```

<br>

Após a criação da aplicação, é necessário lista-la nas configurações do Django, no arquivo settings.py

![Settings](https://i.imgur.com/GbxMFvN.png)

<br>

---

# Runserver

Posteriormente é botar pra rodar com

```bash
python manage.py runserver
```

<br>

Um jeito interessante para se trabalhar com o PyCharm é definir o _runserver_ no PyCharm.

![Settings](https://i.imgur.com/46h6ubM.png)

<br>

---

# Admin.py

Uma vez criado o modelo de dados, é preciso registra-lo no arquivo admin.py, podendo ser configurado ainda a lista das colunas que irão aparecer na aba do adminstrados, bem como as opções para filtrar os dados.

```python
from django.contrib import admin
from core.models import serie_historica

# Register your models here.
class CoreAdmin(admin.ModelAdmin):
    list_display = ('data', 'descricao', 'pu_compra')
    list_filter = ('descricao',)

admin.site.register(serie_historica, CoreAdmin)
```

<br>

---

# Apps.py

No painel de administração, é possível ajustar o nome da aplicação usando o verbose name

```python
from django.apps import AppConfig

class CoreConfig(AppConfig):
    name = 'core'
    verbose_name = 'Bando de Dados'
```

<br>

Para isso é necessário inserir o comando abaixo no arquivo **\_**init**.py\_**

```python
default_app_config = 'core.apps.CoreConfig'
```

<br>

### Referências

- https://docs.djangoproject.com/en/3.1/ref/applications/

<br>

---

# URLs

<br>

## _Redirect_

Usualmente as URLs do site são definidas no arquivo `{project name}/urls.py`.
Dessa forma, é possível fazer roteamento e redirecionamento/redirect das urls, quando definido um caminha em branco ('').

```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('agenda/', views.lista_eventos),
    path('', views.index),
]
```

<br>

Para que isso dê certo, no arquivo **view** é preciso criar a função que faz o redirecionamento para outra view pré-existente.

```python
from django.shortcuts import render, redirect

def index(request):
    return redirect('/agenda/')
```

<br>

Outra alternativa é fazer o redirect já no arquivos urls, sem precisar criar função no views para isso.

```python
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('agenda/', views.lista_eventos),
    path('', RedirectView.as_view(url='/agenda/')),
]
```

---

<br>

## URLs da _Application_

Uma saída bastante elegante é definir as urls em um arquivo _urls.py_ a ser criado dentro do diretório da aplicação. Para que isso funcione, no arquivo ulrs do projeto é necessário incluir todas as urls que serão listadas na aplicação. Ainda, é necessário fazer um ajuste adicional para carregar os arquivos estáticos, logo o arquivo urls deve fazer assim

```python
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # ... the rest of your URL configuration goes here...
    path('', include('core.urls')),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
```

<br>

E o arquivo urls na pasta da aplicação deve ficar, mais ou menos, assim:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.go_home, name='home'),
]
```

<br>

---

# Views

Apenas para renderizar o arquivo que criamos, insira a seguinte função no arquivo **_view.py_**.

```python
def go_home(request):
    return render(request, 'index.html')
```

<br>

---

# Customizações

<br>

## Settings Fuso Brasil

```python
# Internationalization
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_L10N = True
USE_TZ = False
```

<br>

---

# Custom Commands

- https://docs.djangoproject.com/en/3.0/howto/custom-management-commands/
- Iniciamnente é necessário criar a estrutura de pastas **management/commands** dentro do _app_.
- https://www.youtube.com/watch?v=V0RfgNIwCqI

```bash
python manage.py {command name}
python manage.py update
```

<br>

---

# Autenticação

- Autentica
- Login
- Logout

**DECORADORES** é usado em cima da views para ver se o usuário está logado em uma determinada view que requer isso!

```python
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')
```

<br>

---

# _Sitemap_

Rodei o tutorial no projeto do PL 251

[Medium: How to create a Django Sitemap](https://medium.com/analytics-vidhya/django-sitemap-8f4ca0538fa)

... de quebra, aprendi o slug! Top!
https://stackoverflow.com/questions/837828/how-do-i-create-a-slug-in-django

<br>

**Referências**

[Django 3.2: Sitemaps](https://docs.djangoproject.com/en/3.2/ref/contrib/sitemaps/)

<br>

---

# Referências

- [Curso TreinaWeb](https://lp.treinaweb.com.br/python/aula1)
