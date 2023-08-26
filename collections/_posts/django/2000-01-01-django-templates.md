---
title: "Django: *templates*"
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

Criar pasta _templates_ na raiz do projeto.
Registra a pasta _templates_ no arquivo _settings.py_, usando o comando

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',

        # Add Templates in Django
        'DIRS': [(os.path.join(BASE_DIR, 'templates'))],

        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

<br>

Inicialmente, usando o pyCharm, crie um arquivo chamado index.html, apenas para testes.

Criei três arquivos de modelo do HTML:

- \_footer.html
- \_header.html
- \_page.html

Eles serão acessórios de outros que chamar.

<br>

### Referências

- [Django: **builtins**](https://docs.djangoproject.com/en/3.0/ref/templates/builtins/)
- https://adminlte.io/blog/django-website-templates
