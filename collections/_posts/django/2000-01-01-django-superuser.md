---
title: "Django: *superuser*"
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

---

# _Create Superuser_

Uma ver criado o superusuário, com o comando abaixo, é possível acessar o painel de administração dos usuários e modelos no [127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

```bash
python manage.py createsuperuser --email admin@example.com --username admin
python manage.py createsuperuser --email michelmetran@gmail.com --username michelmetran
```

```python
# Criando Usuários
# echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@myproject.com', 'password')" | python manage.py shell
# https://stackoverflow.com/questions/6244382/how-to-automate-createsuperuser-on-django
```
