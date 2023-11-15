---
title: "Django: <i>Heroku</i>"
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

Para fazer o _deploy_ de uma aplicação Django no Heroku, são necessários alguns passos. É preciso adicionar o seguinte código no arquivo **_settings.py_**

```python
import django_heroku

# Deploy on Heroku
django_heroku.settings(locals())
```

<br>

Por fim, fazer o git

```bash
git init
git add . -A
git commit -m 'first commit'
git push heroku master
```

<br>

No Heroku

```bash
heroku login
heroku create {project_name}
heroku git:remote -a {project_name}
heroku git:remote -a opentesouro
```

<br>

Para migrar base de dados

```bash
heroku run python manage.py migrate
```

<br>

---

### Referências

- [Heroku: django-app-configuration](https://devcenter.heroku.com/articles/django-app-configuration)
- [Heroku: Working with Django](https://devcenter.heroku.com/categories/working-with-django)
- [Medium: Deploy de uma aplicação Django no Heroku](https://medium.com/@renatojlelis/deploy-de-uma-aplica%C3%A7%C3%A3o-django-no-heroku-267ae0842410)
