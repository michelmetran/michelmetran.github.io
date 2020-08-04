---
layout: post
title: DataGeo
subtitle: Dados Espaciais

thumbnail-img: /assets/img/posts/datageo_icon.png
share-img: /assets/img/posts/datageo_big.png
cover-img: /assets/img/posts/datageo_big.png

gh-repo: michelmetran/geo_SP_DataGeo
gh-badge: [follow, star, watch, fork]

comments: true
language: pt-br
tags: [python, jupyter, package, datageo, gis]
---

O [**DataGeo**](http://datageo.ambiente.sp.gov.br/) é o sistema da ~~Secretaria Estadual de Meio Ambiente do Estado de São Paulo (SMA)~~ [**Secretaria de Infraestrutura e Meio Ambiente (SIMA)**](https://www.infraestruturameioambiente.sp.gov.br) que disponibiliza diversas informações relevantes. Entendo que trata-se do pilar do que é chamado de <u>Infraestrutura de Dados Espaciais Ambientais do Estado de São Paulo</u>. No evento MundoGEO Connect, edição de 2014, foi feita [uma apresentação](https://mundogeoconnect.com/2014/arquivos/palestras/9_mai-a-arlete-ohata.pdf) que explica melhor a concepção do DataGeo.

As informações são disponibilizadas, majoritariamente, em formato WMS (*Web Map Service*), que impossibilita análises espaciais, possibilitando apenas visualizações :poop:. Contudo, alguns *layers* estão acessíveis nos formatos editáveis mais usuais, sendo que os dados armazenados nesse repositório são derivados destes formatos.


## Objetivo do repositório

Este repositório tem a finalidade de disponibilizar as rotinas empregadas para fazer o *download* e tratamento dos dados, bem como disponibilizar os dados espaciais de maneira remota, sendo facilmente utilizado em outras aplicações.


- ***Download***: tentativa de busca dos dados por meio do *link* dos metadados;

- ***Tratamento dos Atributos***: deletar colunas desnecessárias, renomear colunas etc;

- ***Transformação de Projeção***: buscar padronizar a base de dados em EPSG: 4326, tento em vista ser o mais empregado em *webmaps*;

- ***Excluir Lixos***: deletar arquivos intermediários, mantendo apenas o arquivo bruto e a versão que utilizo em outros códigos.



## Consumindo dados do repositório

O *link* para um determinado arquivo *geojson* no repositório é apresentado abaixo

```bash
https://github.com/michelmetran/geo_SP_DataGeo/blob/master/data/LimiteMunicipal.geojson
```

A partir disso faz-se necessário alterar `github.com` por `raw.githubusercontent.com` e remover o `blob/`. Com isso é possível ler o arquivo *geojson* diretamente nos códigos do python usando, por exemplo, a biblioteca *geopandas*.

```python
import geopandas as gpd

url = 'https://raw.githubusercontent.com/michelmetran/geo_SP_DataGeo/master/data/LimiteMunicipal.geojson'
gdf_mun = gpd.read_file(url)
```
<div class="alert alert-info">
<b>INFORMAÇÃO</b><br/>
    <ol>
    <li>É possível acessar esse <i>post</i> em formato <a href="https://rawcdn.githack.com/michelmetran/geo_SP_DataGeo/master/docs/getdata_datageo.html" target="_blank"><i><b>html</b></i></a>, que possibilita ter uma visualização rápida do código;</li>
    <li>Diretamente por meio do <a href="https://github.com/michelmetran/geo_SP_DataGeo" target="_blank"><b>repositório do GitHub</b></a>, onde está disponível o arquivo <i><b>.ipynb</b></i>, que permite fazer edições no código;</li>
    <li>Ou ainda, de maneira interativa, usando o <a href="https://mybinder.org/v2/gh/michelmetran/geo_SP_DataGeo/master" target="_blank"><i><b>MyBinder</b></i></a>, que possibilita rodar e editar o código sem a necessidade de instalar nada.</li>
    </ol>
</div>

# *Imports* e Funções

Inicialmente faz-se necessário importar as bibliotecas que serão necessárias.

```python
import os
import re
import shutil
import zipfile
import requests
import geopandas as gpd
from datetime import date
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
```

Após isso cria-se as pastas listadas, que armazenarão as informações ao longo desse *script*.

```python
[os.makedirs(i, exist_ok=True) for i in ['data/brutos', 'docs']]
```

Usei a função abaixo para fazer *download* usando o *request*. Ainda, a função pega o nome do arquivo a partir do *Content Disposition*. Peguei a função do *post* [*Downloading Files from URLs in Python*](https://www.codementor.io/@aviaryan/downloading-files-from-urls-in-python-77q3bs0un), aonde tem outros exemplos, com outras finalidades.

```python
def get_filename_from_cd(cd):
    """
    Get filename from content-disposition
    """
    if not cd:
        return None
    fname = re.findall('filename=(.+)', cd)
    if len(fname) == 0:
        return None
    return fname[0]
```

# Dados Espaciais

Após isso a forma de obtenção dos dados:
1. Acessar a página dos metadados do plano de informação e exportar, mantendo armazenadas as informações da origem desse material;
2. Caso seja possível acessar o material cartográfica por *shapefile*, será possível tomar conhecimento disso na paǵina dos metadados;
3. Uma função específica procura o *link* do *shapefile* e faz o download, extração da pasta zipada.
4. Promove-se correções na tabela de atributos e nas projeções geográficas.

## Limite Municipal SP (IGC)

```python
# Input dos caminhos para os metadados
url = 'http://datageo.ambiente.sp.gov.br/geoportal/catalog/search/resource/details.page?uuid='
id_metadados = '{74040682-561A-40B8-BB2F-E188B58088C1}'

# Resultados
url_meta = url+id_metadados
print('Página com metadados: {}'.format(url_meta))
```

```python
# Abre a página dos metadados
page = requests.get(url_meta)
print('Resposta da página foi {}'.format(page))

# Parser HTML
soup = BeautifulSoup(page.content, 'html.parser')
soup = soup.find_all('a', href=True)

# Procura Shapefile
for i in soup:
    text = i.text.split(' ')
    #print(text)
    for j in text:
        #print(j)
        if j in 'Shapefile':
            print('> Encontrei o shapefile')
            url = i['href']
            print('Link: {}'.format(url))
```

```python
# Download do arquivo e paga o nome a partir do content-disposition
# Arquivo zip (shapefile) vai para a pasta de 'data/brutos'
r = requests.get(url, allow_redirects=True)
filename = get_filename_from_cd(r.headers.get('content-disposition'))
open(os.path.join('data', 'brutos', filename), 'wb').write(r.content)
```

```python
# Com o nome do arquivo, é realizado o download da página dos metadados
file_meta = filename.split('.')[0]
r = requests.get(url_meta, allow_redirects=True)
open(os.path.join('data', 'brutos', file_meta + '.html'), 'wb').write(r.content)
```

```python
# Unzip
file = os.path.join('data', 'brutos', filename)
temp = os.path.join(os.path.dirname(file), 'temp')
os.makedirs(temp, exist_ok=True)

with zipfile.ZipFile(file, 'r') as zip_ref:
    zip_ref.extractall(temp)
```

```python
# Lista Arquivos
os.listdir(temp)
```

```python
# Read shapefile
gdf = gpd.read_file(os.path.join(temp, 'LimiteMunicipalPolygon.shp'))
display(gdf.head(5))
gdf.plot()
```

```python
# Renomeia Colunas
gdf = gdf.rename(columns={'Cod_ibge':'ID_IBGE',
                          'Nome':'Nome_Municipio',
                          'Rotulo':'Rotulo_Municipio'})

# Deleta Colunas
gdf = gdf.drop(['Cod_Cetesb', 'UGRHI', 'Nome_ugrhi'], axis=1)

print(gdf.dtypes)
display(gdf.head(5))
```

```python
# Reprojeta
print(gdf.crs)
gdf = gdf.to_crs(epsg=4326)
print(gdf.crs)
gdf.plot()
```

```python
# Salva
gdf.to_file(os.path.join('data', 'LimiteMunicipal.geojson'), driver='GeoJSON', encoding='utf-8')
gdf.to_file(os.path.join('data', 'LimiteMunicipal' + '.gpkg'), layer='Limite', driver="GPKG")
```

```python
# Excluí pasta temporária
shutil.rmtree(temp)
```

## Sedes Municipais

```python
# Input dos caminhos para os metadados
url = 'http://datageo.ambiente.sp.gov.br/geoportal/catalog/search/resource/details.page?uuid='
id_metadados = '{64BF344A-3AD0-410A-A3AA-DFE01C4E9BBB}'

# Resultados
url_meta = url+id_metadados
print('Página com metadados: {}'.format(url_meta))
```

```python
# Abre a página dos metadados
page = requests.get(url_meta)
print('Resposta da página foi {}'.format(page))

# Parser HTML
soup = BeautifulSoup(page.content, 'html.parser')
soup = soup.find_all('a', href=True)

# Procura Shapefile
for i in soup:
    text = i.text.split(' ')
    #print(text)
    for j in text:
        #print(j)
        if j in 'Shapefile':
            print('> Encontrei o shapefile')
            url = i['href']
            print('Link: {}'.format(url))
```

```python
# Download do arquivo e paga o nome a partir do content-disposition
# Arquivo zip (shapefile) vai para a pasta de 'data/brutos'
r = requests.get(url, allow_redirects=True)
filename = get_filename_from_cd(r.headers.get('content-disposition'))
open(os.path.join('data', 'brutos', filename), 'wb').write(r.content)
```

```python
# Com o nome do arquivo, é realizado o download da página dos metadados
file_meta = filename.split('.')[0]
r = requests.get(url_meta, allow_redirects=True)
open(os.path.join('data', 'brutos', file_meta + '.html'), 'wb').write(r.content)
```

```python
# Unzip
file = os.path.join('data', 'brutos', filename)
temp = os.path.join(os.path.dirname(file), 'temp')
os.makedirs(temp, exist_ok=True)

with zipfile.ZipFile(file, 'r') as zip_ref:
    zip_ref.extractall(temp)
```

```python
# Lista Arquivos
os.listdir(temp)
```

```python
# Read shapefile
gdf = gpd.read_file(os.path.join(temp, 'SedesMunicipaisPoint.shp'))
display(gdf.head(5))
gdf.plot()
```

```python
# Renomeia Colunas
gdf = gdf.rename(columns={'Nome':'Nome_Municipio'})

# Deleta Colunas
gdf = gdf.drop(['Codigo_CET'], axis=1)

print(gdf.dtypes)
display(gdf.head(5))
```

```python
# Reprojeta
print(gdf.crs)
gdf = gdf.to_crs(epsg=4326)
print(gdf.crs)
gdf.plot()
```

```python
# Salva
gdf.to_file(os.path.join('data', 'SedesMunicipais.geojson'), driver='GeoJSON', encoding='utf-8')
gdf.to_file(os.path.join('data', 'SedesMunicipais' + '.gpkg'), layer='Sedes', driver="GPKG")
```

```python
# Excluí pasta temporária
shutil.rmtree(temp)
```
