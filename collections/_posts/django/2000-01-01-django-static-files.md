---
title: "Django: *staticfiles*"
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

Para fazer com que o Django utiliza arquivos estáticos --- usualmente acessários para renderizar os arquivos HTML (tais como _css_, _javascript_, _fonts_, _imagens_ etc) --- é necessário ajustar alguns parâmetros no arquivo _settings_, conforme abaixo:

```python
# Static files (CSS, JavaScript, Images)
# The URL which will serve static files
STATIC_URL = '/static/'

# Where to look to search
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'dados/static_app'),
    os.path.join(BASE_DIR, 'sabesp/static_app'),
]

# Where locate files, and comment the AppDirectoriesFinder
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

# Name of dir that will be create
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
```

<br>

Ainda, na sessão **_Middleware_**, é necessário acrescentar o comando `'whitenoise.middleware.WhiteNoiseMiddleware'`, conforme é apresentado abaixo.

```python
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', # Add Whitenoise Middleware
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
```

<br>

Comando para reunir todos os arquivos na pasta definida em STATIC_ROOT

```bash
python manage.py collectstatic
```

<br>

É possivel procurar a fonte de um arquivo, ou seja, qual o local que ele está buscando o arquivo:

```bash
python manage.py findstatic css/base.css admin/js/core.jspython manage.py
```

---

<br>

## WhiteNoise

- http://whitenoise.evans.io/en/stable

<br>

---

## Problemas

### _Could be not found_

Nos projetos que eu utiliava o _template_ AdminLTE, ao realizar o comando `collectstatic` eu recebia o seguinte erro:

```
whitenoise.storage.MissingFileError: The file 'plugins/jquery-ui/"images/ui-icons_555555_256x240.png"' could not be found with <whitenoise.storage.CompressedManifestStaticFilesStorage object at 0x7f04d25224d0>.

The CSS file 'plugins/jquery-ui/jquery-ui.css' references a file which could not be found:
  plugins/jquery-ui/"images/ui-icons_555555_256x240.png"

Please check the URL references in this CSS file, particularly any
relative paths which might be pointing to the wrong location.

```

<br>

Para contornar econtrei discussão em [stackoverflow: **_Whitenoise giving errors on jquery-ui.css when doing collectstatic_**](https://stackoverflow.com/questions/47238946/whitenoise-giving-errors-on-jquery-ui-css-when-doing-collectstatic) que sugeria deletar **_all first comment block in all jquery css file_** e deu certo.

Por exemplo, o arquivo que era assim:

```css
/*! jQuery UI - v1.13.0 - 2021-10-07
* http://jqueryui.com
* Includes: core.css, accordion.css, autocomplete.css, menu.css, button.css, controlgroup.css, checkboxradio.css, datepicker.css, dialog.css, draggable.css, resizable.css, progressbar.css, selectable.css, selectmenu.css, slider.css, sortable.css, spinner.css, tabs.css, tooltip.css, theme.css
* To view and modify this theme
* Copyright jQuery Foundation and other contributors; Licensed MIT */

/* Layout helpers
----------------------------------*/
.ui-helper-hidden {
  display: none;
}
```

<br>

Ficou assim:

```css
.ui-helper-hidden {
  display: none;
}
```

<br>

**Sem sucesso!**

<br>

---

Tentei também substiuir...

Substitui `"images/ui-icons_555555_256x240.png"` por `%22images%2Fui-icons_555555_256x240.png%22`

<br>

**Sem sucesso!**<br>
Solução tosca: deletar as entradas!

<br>

---

### _The JS file 'plugins/pdfmake/pdfmake.js' references a file which could not be found:_

Recebia o erro que determinado arquivo fazia menção a outro... que não constava nos arquivos estáticos.

```bash
The JS file 'plugins/pdfmake/pdfmake.js' references a file which could not be found:
  plugins/pdfmake/FileSaver.min.js.map
```

Fui procurar a menção. Tratava-se de um comentário: excluí!

<br>

---

## Referências

- [YouTube: **Try Django 1.9 - 25 of 38 - Setup Static Files - CSS & Javascript & Images in Django**](https://www.youtube.com/watch?v=YH-ipgxlJzs)
- [YouTube: **Understanding Django Static Files**](https://www.youtube.com/watch?v=w9F9k-JHvcQ)
- [Medium: **Understanding static files in Django + Heroku**](https://medium.com/@vonkunesnewton/understanding-static-files-in-django-heroku-1b8d2f003977)
- [Heroku Dev Center: **Django and Static Assets**](https://devcenter.heroku.com/articles/django-assets)
- [Django: **Static Files**](https://docs.djangoproject.com/en/3.0/howto/static-files/)
- [StackOverflow: **Found another file with the destination path - where is that other file?**](https://stackoverflow.com/questions/35571256/found-another-file-with-the-destination-path-where-is-that-other-file)
