---
title: 'Conda: <i>Enviroments</i>'
date: 2019-06-13T15:34:30-04:00
last_modified_at: 2022-06-28T00:00:00-03:00
excerpt_separator: '<!--more-->'
categories:
  - IT

tags:
  - python
  - anaconda
  - miniconda
---

Comandos para criar e clonar _enviroments_. A grande vantagem de criar um _enviroments_ com todos os _packages_ juntos é que já ocorre a resolução de conflitos das dependências.

### Pablo Carreira

É o _enviroment_ que mais uso, que tem todas as ferramentas. O nome é uma homenagem a um amigo que publicou um livro sobre uso do _python_ no geoprocessamento. Na tentativa de acompanhar os tutorais, ainda usando o Windows, me deparei com diversos problemas de incompatibilidade entre pacotes, momento em que migrei para o Linux e uso do conda para eliminar esses problemas.

```bash
conda create --name pablocarreira-lastest python=3.10 jupyter jupyterlab jupyter_contrib_nbextensions jupyterlab-git nb_conda nb_conda_kernels nbstripout nbconvert conda-build anaconda-client ipyparallel ipywidgets autopep8 pandoc pandas geopandas descartes geopy shapely gdal fiona tabulate tabula-py openpyxl xlrd requests xmltodict psycopg2 opencv pylint folium seaborn gspread df2gspread keyring oauth2client tqdm beautifulsoup4 selenium scrapy Pillow pytesseract papermill flask dask sqlite plotly python-dotenv
```

<br>

### Trade

```bash
conda create --name trade -c conda-forge -c cpaulik -c bioconda -c esri python=3.8 jupyter jupyterlab  jupyter_contrib_nbextensions nb_conda nbstripout nbconvert=5.6.1 ipyparallel ipywidgets autopep8 pandoc pandas requests plotly nodejs tornado=5.1.1
```

<br>

### R

```bash
conda create --name R -c conda-forge -c r r-recommended r-irkernel jupyter jupyterlab  jupyter_contrib_nbextensions nb_conda nbstripout nbconvert=5.6.1 ipyparallel ipywidgets
```

<br>

### OneDrive

```bash
conda create --name onedrive-py35 -c conda-forge -c cpaulik -c bioconda -c ddboline  python=3.5 jupyter jupyterlab jupyter_contrib_nbextensions nb_conda nbstripout ipyparallel ipywidgets autopep8 pandoc pandas geopandas descartes geopy shapely gdal django gitpython tabulate requests xmltodict psycopg2  xlrd  opencv folium seaborn sh gspread df2gspread oauth2client tqdm wget python-wget beautifulsoup4 selenium scrapy Pillow pytesseract tabula-py papermill flask sqlite pipreqs onedrivesdk
```

<br>

### _WebApps_

_Enviroment_ usado para o projeto Django.

```bash
conda create --name webapp-py38 -c conda-forge python=3.8 django django-heroku gunicorn requests sqlite mysqlclient pandas geopandas folium seaborn
```

<br>

### Colab

_Enviroment_ usado para o projeto Django.

```bash
conda create --name colab-py37 -c conda-forge python=3.7 requests pandas geopandas
```

<br>

### Finanças

_Enviroment_ usado para o projeto Django do **Tesouro Direto**

```bash
conda create --name td-py38 -c conda-forge -c cpaulik python=3.8 django requests psycopg2 pandas bs4 plotly django-heroku gunicorn xlrd djangorestframework
```

<br>

### _Firebase_

_Enviroment_ usado para **pyrebase**

```bash
conda create --name firebase-py38 -c conda-forge -c auto python=3.8 jupyter jupyter_contrib_nbextensions nb_conda nbstripout ipyparallel ipywidgets pandas requests
```

```bash
conda install -c modoolar firebase-admin
```

<br>

### Wfuzz

_Enviroment_ usado para **wfuzz**

```bash
conda create --name wfuzz-py38 -c conda-forge -c auto python=3.8 jupyter jupyter_contrib_nbextensions nb_conda nbstripout ipyparallel ipywidgets pandas requests wfuzz
```
