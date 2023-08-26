---
title: "Django: *media*"
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

Para adicionar imagens ou médias, é necessário criar uma pasta `media` na raiz do projeto.

Após isso é necessário no arquivo `settings.py` a definição da localização dessas pastas

```python
# Media
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

<br>

No arquivo `url.py` é necessário adicionar a referência à url

```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
              ] + \
              static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + \
              static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

<br>

---

## Referências

- https://docs.djangoproject.com/en/4.1/topics/files/
