---
layout: page
title: Folium
subtitle: Exercícios e Referências
permalink: /folium
---

<a title="Link do Folium" href="https://python-visualization.github.io/folium/index.html#" target="_blank">**_Folium_**</a> 
 
<img src='./imgs/top.png'>

- https://python-visualization.github.io/folium/quickstart.html
- https://www.freecodecamp.org/news/real-world-data-science-project-traffic-accident-analysis-e5a36775ee11/

Muita coisa interessante em https://www.youtube.com/watch?v=4RnU5qKTfYY

## Importando Bibliotecas

As bibliotecas básicas, ou _packages_, necessárias para criação do mapa são:
- O **_Pandas_**, que tem a missão de trabalhar com dados, criar _subsets_, selecionar e filtros dados e;
- O **_Folium_**, que é a biblioteca que cria, na prática, o mapa!


```python
import pandas as pd
import folium
```

## Criando um mapa

Basta um par de coordenadas -- que pode ser obtida facilmente no _link_ de qualquer endereço usando <a title="Link do Google Maps" href="https://www.google.com.br/maps" target="_blank">**_Google Maps_**</a> -- e um nível de zoom que o mapa já está criado.


```python
folium.Map(
    location=[-23.9619271,-46.3427499],      # Define coordenadas iniciais
    #min_zoom = 6,                           # Define qual o menor zoom
    #max_zoom = 14,                          # Define qual o maior zoom
    #no_wrap = True,
    #max_bounds = True,
    zoom_start=12                            # Define o zoom do início
)
```




<div style="width:100%;"><div style="position:relative;width:100%;height:0;padding-bottom:60%;"><iframe src="data:text/html;charset=utf-8;base64,PCFET0NUWVBFIGh0bWw+CjxoZWFkPiAgICAKICAgIDxtZXRhIGh0dHAtZXF1aXY9ImNvbnRlbnQtdHlwZSIgY29udGVudD0idGV4dC9odG1sOyBjaGFyc2V0PVVURi04IiAvPgogICAgCiAgICAgICAgPHNjcmlwdD4KICAgICAgICAgICAgTF9OT19UT1VDSCA9IGZhbHNlOwogICAgICAgICAgICBMX0RJU0FCTEVfM0QgPSBmYWxzZTsKICAgICAgICA8L3NjcmlwdD4KICAgIAogICAgPHNjcmlwdCBzcmM9Imh0dHBzOi8vY2RuLmpzZGVsaXZyLm5ldC9ucG0vbGVhZmxldEAxLjQuMC9kaXN0L2xlYWZsZXQuanMiPjwvc2NyaXB0PgogICAgPHNjcmlwdCBzcmM9Imh0dHBzOi8vY29kZS5qcXVlcnkuY29tL2pxdWVyeS0xLjEyLjQubWluLmpzIj48L3NjcmlwdD4KICAgIDxzY3JpcHQgc3JjPSJodHRwczovL21heGNkbi5ib290c3RyYXBjZG4uY29tL2Jvb3RzdHJhcC8zLjIuMC9qcy9ib290c3RyYXAubWluLmpzIj48L3NjcmlwdD4KICAgIDxzY3JpcHQgc3JjPSJodHRwczovL2NkbmpzLmNsb3VkZmxhcmUuY29tL2FqYXgvbGlicy9MZWFmbGV0LmF3ZXNvbWUtbWFya2Vycy8yLjAuMi9sZWFmbGV0LmF3ZXNvbWUtbWFya2Vycy5qcyI+PC9zY3JpcHQ+CiAgICA8bGluayByZWw9InN0eWxlc2hlZXQiIGhyZWY9Imh0dHBzOi8vY2RuLmpzZGVsaXZyLm5ldC9ucG0vbGVhZmxldEAxLjQuMC9kaXN0L2xlYWZsZXQuY3NzIi8+CiAgICA8bGluayByZWw9InN0eWxlc2hlZXQiIGhyZWY9Imh0dHBzOi8vbWF4Y2RuLmJvb3RzdHJhcGNkbi5jb20vYm9vdHN0cmFwLzMuMi4wL2Nzcy9ib290c3RyYXAubWluLmNzcyIvPgogICAgPGxpbmsgcmVsPSJzdHlsZXNoZWV0IiBocmVmPSJodHRwczovL21heGNkbi5ib290c3RyYXBjZG4uY29tL2Jvb3RzdHJhcC8zLjIuMC9jc3MvYm9vdHN0cmFwLXRoZW1lLm1pbi5jc3MiLz4KICAgIDxsaW5rIHJlbD0ic3R5bGVzaGVldCIgaHJlZj0iaHR0cHM6Ly9tYXhjZG4uYm9vdHN0cmFwY2RuLmNvbS9mb250LWF3ZXNvbWUvNC42LjMvY3NzL2ZvbnQtYXdlc29tZS5taW4uY3NzIi8+CiAgICA8bGluayByZWw9InN0eWxlc2hlZXQiIGhyZWY9Imh0dHBzOi8vY2RuanMuY2xvdWRmbGFyZS5jb20vYWpheC9saWJzL0xlYWZsZXQuYXdlc29tZS1tYXJrZXJzLzIuMC4yL2xlYWZsZXQuYXdlc29tZS1tYXJrZXJzLmNzcyIvPgogICAgPGxpbmsgcmVsPSJzdHlsZXNoZWV0IiBocmVmPSJodHRwczovL3Jhd2Nkbi5naXRoYWNrLmNvbS9weXRob24tdmlzdWFsaXphdGlvbi9mb2xpdW0vbWFzdGVyL2ZvbGl1bS90ZW1wbGF0ZXMvbGVhZmxldC5hd2Vzb21lLnJvdGF0ZS5jc3MiLz4KICAgIDxzdHlsZT5odG1sLCBib2R5IHt3aWR0aDogMTAwJTtoZWlnaHQ6IDEwMCU7bWFyZ2luOiAwO3BhZGRpbmc6IDA7fTwvc3R5bGU+CiAgICA8c3R5bGU+I21hcCB7cG9zaXRpb246YWJzb2x1dGU7dG9wOjA7Ym90dG9tOjA7cmlnaHQ6MDtsZWZ0OjA7fTwvc3R5bGU+CiAgICAKICAgICAgICAgICAgPG1ldGEgbmFtZT0idmlld3BvcnQiIGNvbnRlbnQ9IndpZHRoPWRldmljZS13aWR0aCwKICAgICAgICAgICAgICAgIGluaXRpYWwtc2NhbGU9MS4wLCBtYXhpbXVtLXNjYWxlPTEuMCwgdXNlci1zY2FsYWJsZT1ubyIgLz4KICAgICAgICAgICAgPHN0eWxlPgogICAgICAgICAgICAgICAgI21hcF9mYmZhMGExZGY0NTA0OTdmOGI1N2FmNjBkZDVhMWFkNSB7CiAgICAgICAgICAgICAgICAgICAgcG9zaXRpb246IHJlbGF0aXZlOwogICAgICAgICAgICAgICAgICAgIHdpZHRoOiAxMDAuMCU7CiAgICAgICAgICAgICAgICAgICAgaGVpZ2h0OiAxMDAuMCU7CiAgICAgICAgICAgICAgICAgICAgbGVmdDogMC4wJTsKICAgICAgICAgICAgICAgICAgICB0b3A6IDAuMCU7CiAgICAgICAgICAgICAgICB9CiAgICAgICAgICAgIDwvc3R5bGU+CiAgICAgICAgCjwvaGVhZD4KPGJvZHk+ICAgIAogICAgCiAgICAgICAgICAgIDxkaXYgY2xhc3M9ImZvbGl1bS1tYXAiIGlkPSJtYXBfZmJmYTBhMWRmNDUwNDk3ZjhiNTdhZjYwZGQ1YTFhZDUiID48L2Rpdj4KICAgICAgICAKPC9ib2R5Pgo8c2NyaXB0PiAgICAKICAgIAogICAgICAgICAgICB2YXIgbWFwX2ZiZmEwYTFkZjQ1MDQ5N2Y4YjU3YWY2MGRkNWExYWQ1ID0gTC5tYXAoCiAgICAgICAgICAgICAgICAibWFwX2ZiZmEwYTFkZjQ1MDQ5N2Y4YjU3YWY2MGRkNWExYWQ1IiwKICAgICAgICAgICAgICAgIHsKICAgICAgICAgICAgICAgICAgICBjZW50ZXI6IFstMjMuOTYxOTI3MSwgLTQ2LjM0Mjc0OTldLAogICAgICAgICAgICAgICAgICAgIGNyczogTC5DUlMuRVBTRzM4NTcsCiAgICAgICAgICAgICAgICAgICAgem9vbTogMTIsCiAgICAgICAgICAgICAgICAgICAgem9vbUNvbnRyb2w6IHRydWUsCiAgICAgICAgICAgICAgICAgICAgcHJlZmVyQ2FudmFzOiBmYWxzZSwKICAgICAgICAgICAgICAgIH0KICAgICAgICAgICAgKTsKCiAgICAgICAgICAgIAoKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgdGlsZV9sYXllcl9lNDU0NmY5ZjUyMTM0YzM2YWJjMjVmNzZmYjkyNGMwOSA9IEwudGlsZUxheWVyKAogICAgICAgICAgICAgICAgImh0dHBzOi8ve3N9LnRpbGUub3BlbnN0cmVldG1hcC5vcmcve3p9L3t4fS97eX0ucG5nIiwKICAgICAgICAgICAgICAgIHsiYXR0cmlidXRpb24iOiAiRGF0YSBieSBcdTAwMjZjb3B5OyBcdTAwM2NhIGhyZWY9XCJodHRwOi8vb3BlbnN0cmVldG1hcC5vcmdcIlx1MDAzZU9wZW5TdHJlZXRNYXBcdTAwM2MvYVx1MDAzZSwgdW5kZXIgXHUwMDNjYSBocmVmPVwiaHR0cDovL3d3dy5vcGVuc3RyZWV0bWFwLm9yZy9jb3B5cmlnaHRcIlx1MDAzZU9EYkxcdTAwM2MvYVx1MDAzZS4iLCAiZGV0ZWN0UmV0aW5hIjogZmFsc2UsICJtYXhOYXRpdmVab29tIjogMTgsICJtYXhab29tIjogMTgsICJtaW5ab29tIjogMCwgIm5vV3JhcCI6IGZhbHNlLCAib3BhY2l0eSI6IDEsICJzdWJkb21haW5zIjogImFiYyIsICJ0bXMiOiBmYWxzZX0KICAgICAgICAgICAgKS5hZGRUbyhtYXBfZmJmYTBhMWRmNDUwNDk3ZjhiNTdhZjYwZGQ1YTFhZDUpOwogICAgICAgIAo8L3NjcmlwdD4=" style="position:absolute;width:100%;height:100%;left:0;top:0;border:none !important;" allowfullscreen webkitallowfullscreen mozallowfullscreen></iframe></div></div>



Utilizando um conjunto de dados apresentado em https://jtemporal.com/folium/, contendo coordenadas geográficas de empresas, podemos extrair uma empresa específica e plotar no mapa, ou ainda trabalhar de outras maneiras com esses dados.


```python
# Lendo e filtrando dados
empresas = pd.read_csv('./data/empresas.xz')
empresas = empresas[empresas['state'] == 'SP']
empresas = empresas[empresas['city'] == 'SANTOS']
```


```python
empresas.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>situation</th>
      <th>neighborhood</th>
      <th>address</th>
      <th>number</th>
      <th>zip_code</th>
      <th>city</th>
      <th>state</th>
      <th>cnpj</th>
      <th>status</th>
      <th>additional_address_details</th>
      <th>main_activity</th>
      <th>latitude</th>
      <th>longitude</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1108</th>
      <td>ALMEIDA &amp; RODRIGUES MANUTENCAO EM INFORMATICA ...</td>
      <td>ATIVA</td>
      <td>CENTRO</td>
      <td>R AMADOR BUENO</td>
      <td>171</td>
      <td>11.013-151</td>
      <td>SANTOS</td>
      <td>SP</td>
      <td>13.295.386/0001-58</td>
      <td>OK</td>
      <td>SALA 69</td>
      <td>Reparação e manutenção de computadores e de eq...</td>
      <td>-23.935972</td>
      <td>-46.327216</td>
    </tr>
    <tr>
      <th>1534</th>
      <td>MARCIO CESAR FRANCISQUINE SANTOS - ME</td>
      <td>ATIVA</td>
      <td>MARAPE</td>
      <td>AV SENADOR PINHEIRO MACHADO</td>
      <td>856</td>
      <td>11.075-002</td>
      <td>SANTOS</td>
      <td>SP</td>
      <td>18.950.028/0001-55</td>
      <td>OK</td>
      <td>NaN</td>
      <td>Restaurantes e similares</td>
      <td>-23.961729</td>
      <td>-46.345475</td>
    </tr>
    <tr>
      <th>1777</th>
      <td>R P LOPES FONSECA</td>
      <td>ATIVA</td>
      <td>PONTA DA PRAIA</td>
      <td>PC CORACAO DE MARIA</td>
      <td>23</td>
      <td>11.030-280</td>
      <td>SANTOS</td>
      <td>SP</td>
      <td>58.132.036/0001-09</td>
      <td>OK</td>
      <td>NaN</td>
      <td>Comércio varejista de combustíveis para veícul...</td>
      <td>-23.986863</td>
      <td>-46.303085</td>
    </tr>
    <tr>
      <th>2516</th>
      <td>AUTO POSTO NOVO MILENIO LTDA</td>
      <td>ATIVA</td>
      <td>MACUCO</td>
      <td>R CONSELHEIRO RODRIGUES ALVES</td>
      <td>385</td>
      <td>11.015-203</td>
      <td>SANTOS</td>
      <td>SP</td>
      <td>03.542.311/0001-70</td>
      <td>OK</td>
      <td>NaN</td>
      <td>Comércio varejista de combustíveis para veícul...</td>
      <td>-23.956003</td>
      <td>-46.321556</td>
    </tr>
    <tr>
      <th>2914</th>
      <td>CHURRASCARIA E PIZZARIA MAXIM'S LTDA - ME</td>
      <td>ATIVA</td>
      <td>BOQUEIRAO</td>
      <td>AV CONSELHEIRO NEBIAS</td>
      <td>656</td>
      <td>11.045-002</td>
      <td>SANTOS</td>
      <td>SP</td>
      <td>19.396.916/0001-30</td>
      <td>OK</td>
      <td>NaN</td>
      <td>Restaurantes e similares</td>
      <td>-23.962879</td>
      <td>-46.323743</td>
    </tr>
  </tbody>
</table>
</div>



### Inserindo algumas coordenadas


```python
# Cria o mapa
webmap = folium.Map(
    location=[-23.9619271,-46.3427499],
    zoom_start=12
)

# Extrai informações de duas empresas
empresa1 = empresas.iloc[0]
empresa2 = empresas.iloc[1]

# Adiciona no mapa tais empresas
folium.Marker(
    location=[empresa1['latitude'], empresa1['longitude']],
).add_to(webmap)

folium.Marker(
    location=[empresa2['latitude'], empresa2['longitude']],
).add_to(webmap)

# Apresenta o mapa
#webmap
```




    <folium.map.Marker at 0x7fd9945c4b38>



### Inserindo multiplas coordenadas


```python
# Cria o mapa
webmap = folium.Map(
    location=[-23.9619271,-46.3427499],
    zoom_start=12
)

# Adiciona todas as empresas selecionadas
for _, empresa in empresas.iterrows():
    folium.Marker(
        location=[empresa['latitude'], empresa['longitude']],
        tooltip=empresa['neighborhood'],
    ).add_to(webmap)

# Apresenta o mapa
#webmap
```

## Tipos diferentes de Marcadores

As feições que são possiveis de apresentar são àquelas típicas do geoprocessamento:
- Pontos;
- Linhas;
- Polígonos

Abaixo são apresentados alguns tipos de marcadores.

### Pontos Simples


```python
# Cria o mapa
webmap = folium.Map(
    location=[-23.9619271,-46.3427499],
    zoom_start=12
)

# Cria cores para as tags
colors = {
    'PONTA DA PRAIA': 'pink',
    'CENTRO': 'blue',
    'GONZAGA': 'green',
    'JOSÉ MENINO': 'red',
    'EMBARE': 'beige',
    'MACUCO': 'blue',
    'VILA MATHIAS': 'lightblue',
    'POMPEIA': 'red',
    'APARECIDA': 'purple',
}

# Adiciona as diferentes empresas com cores por bairros
for _, empresa in empresas.iterrows():
    if empresa['neighborhood'] in colors.keys():
        folium.Marker(
            location=[empresa['latitude'], empresa['longitude']],
            popup=empresa['name'],
            tooltip=empresa['neighborhood'],
            icon=folium.Icon(color=colors[empresa['neighborhood']], icon='leaf')
        ).add_to(webmap)

# Apresenta o mapa
#webmap
```

### Marcador Circular


```python
# Cria o mapa
webmap = folium.Map(
    location=[-23.9619271,-46.3427499],
    zoom_start=12
)

# Adiciona as diferentes empresas com cores por bairros
for _, empresa in empresas.iterrows():
    if empresa['neighborhood'] in colors.keys():
        folium.CircleMarker(
        location=[empresa['latitude'], empresa['longitude']],        
        radius=10,
        popup='<strong>Empresa</strong>',
        tooltip='Dica',
        fill=True,
        #fill_color='#428bca'
        fill_color=colors[empresa['neighborhood']]
    ).add_to(webmap)

# Apresenta o mapa
#webmap
```

### Custom Icon


```python
#logoIcon = folium.features.CustomIcon('logo.png', icon_size=(50,50))
```

### Vegas
O _folium_ tem o vegas https://vega.github.io/vega/ como default


```python
# Cria o mapa
webmap = folium.Map(
    location=[-23.9619271,-46.3427499],
    zoom_start=12
)

# Importa bibliotecas e lê o json
import os
import json
vis = os.path.join('data', 'vis.json')


# Adiciona as diferentes empresas com gráficos no popup
for _, empresa in empresas.iterrows():
    if empresa['neighborhood'] in colors.keys():
        folium.Marker(
            location=[empresa['latitude'], empresa['longitude']],            
            popup=folium.Popup(max_width=450).add_child(folium.Vega(json.load(open(vis)), width=450, height=250))
).add_to(webmap)
        
# Apresenta o mapa
#webmap
```

### Geojson

É possivel também inserir desenhos em formato **_GeoJson_**, o que abre grande spossibilidades.
Contudo, para rabiscos aleatórios, é possivel criar o arquivo usando http://geojson.io.


```python
# Cria o mapa
webmap = folium.Map(
    location=[-23.9619271,-46.3427499],
    zoom_start=12
)

# Importa bibliotecas e lê o json
import os
import json
shp = os.path.join('data', 'trajetos.json')

# Adiciona as diferentes empresas com gráficos no popup
folium.GeoJson(shp, name='Trajetos').add_to(webmap)
        
# Apresenta o mapa
#webmap
```

# Basemap

O mapa pode ter diferentes _basemaps_, que são, na essência, o mapa de fundo renderizado em _titles_. O _folium_ utiliza, por _default_, o basemap do _OpenStreetMap_, contudo existe a possibilidade d eadicionar outros serviços, conforme se vê abaixo.


```python
folium.Map(    
    location=[-23.9619271,-46.3427499],
    #tiles='Mapbox Bright',
    #tiles='Mapbox Control Room',
    #tiles='Stamen Toner',
    tiles='Stamen Terrain',
    #tiles='OpenStreetMap',
    zoom_start=12
)
```

Um outro jeito de inserir _basemaps_ é utilizado o <a title="Link do MapBox" href="https://www.mapbox.com" target="_blank">MapBox</a>, onde é possível customizar um _basemap_ personalizado, bem como utilizar outros _basemaps_ pré-existentes, incluindo imagens de satélite de alta resolução, etc.

Para melhor utilização, com a possiblidade de disponibilizar códigos, é necessário estudar a melhor maneira de ocultar a _API key_. Um início:
- http://www.blacktechdiva.com/hide-api-keys/
- https://www.quora.com/How-do-you-hide-your-API-customer-key-token-when-youre-pushing-code-to-Github


```python
#folium.Map(location=[-23.9619271,-46.3427499],
#           tiles='Mapbox',
#           API_key='your.API.key',
#           zoom_start=12
#          )
```

Por fim, é possivel ainda inserir _basemaps_ personalizados, disponibilizados em algum servidor. E existem diversos servidores:
- https://www.spatialbias.com/2018/02/qgis-3.0-xyz-tile-layers/
- https://xyz.michelstuyts.be/
- https://www.trailnotes.org/FetchMap/TileServeSource.html


```python
# Cria o mapa com servidores dos tiles
folium.Map(location=[-23.9619271,-46.3427499],
           zoom_start=12,
           tiles='http://{s}.tile.osm.org/{z}/{x}/{y}.png',
           attr='s'
          )
```


```python
# %load '~/Documents/GitRepo/code_reference/maps/create_tiles_folium.py'
def create_tiles_folium(tile_service=1, location=[-23.9619271, -46.3427499], zoom_start=10):
    """
    Function to create map using tiles... a list of them
    :param tile_service:
    :param location:
    :param zoom_start:
    :return:
    """
    # Import
    import pandas as pd
    import folium

    # Read table with all tiles servers
    tiles_services = pd.read_csv('~/Documents/GitRepo/code_reference/data/tiles.csv', index_col=0)
    # print(tiles_services)

    # Create reference to attribution
    ref = ('<a href="' +
           tiles_services.loc[tile_service, 'attribution'] +
           '" target="blank">' +
           tiles_services.loc[tile_service, 'name'] +
           '</a>')

    return folium.Map(location=location,
                      zoom_start=zoom_start,
                      tiles=tiles_services.loc[tile_service, 'link'],
                      attr=ref)
```


```python
create_tiles_folium()
```

### Outros elementos do WebMap


```python
# Adiciona legenda
folium.LayerControl().add_to(webmap)
webmap

# Adiciona a possibilidade de pontos, on-the-fly
webmap.add_child(folium.ClickForMarker(popup='Waypoint'))

# Adiciona a possibilidade de, a cada clique, descobrir as coordenadas
webmap.add_child(folium.LatLngPopup())
```

## Salva o mapa em HTML

A grande vantagem é salvar o mapa como um arquivo _.html_, bastante possivel para dar um _embed_ em qualquer página. Para salvar, criei uma função que pode contribuir, que avalia se determinadas pastas estão criadas e, em caso negativo, cria as mesmas. Em uma destas pastas que ficará salvo o arquivo _.html_ criado


```python
# %load '~/Documents/GitRepo/code_reference/files/create_folders.py'
def create_folders(folders):
    """
    :param folders: Name os folders that you want create; E.g.: ['folder1', 'folder2']
    :return: Create directories if not exist
    """

    import os
    for folder in folders:
        try:
            if not os.path.exists(folder):
                os.makedirs(folder)
                print('Directory "', folder, '" created!', sep='')
            else:
                print('Directory "', folder, '" already exists...', sep='')
        except OSError:
            print('Error: Creating directory "', folder, '" fail.', sep='')
```


```python
paths=['data', 'maps', 'imgs', 'docs']
create_folders(paths)
```


```python
webmap.save('./maps/map_santos.html')
```

### Embed do arquivo HTML no Jupyter


```python
# É possivel inserir em uma célula de código, possibilitando uma iteratividade

import IPython
iframe = '<iframe width="900" height="800" frameborder="0" scrolling="no" src="//plot.ly/~ekirzhner/6.embed"></iframe>'
IPython.display.HTML(iframe)
```

... ou como um texto em _.html_, que não dá iteratividade.

<div>
    <a href="https://plot.ly/~ekirzhner/6/" target="_blank" title="Plot 6" style="display: block; text-align: center;"><img src="https://plot.ly/~ekirzhner/6.png" alt="Plot 6" style="max-width: 100%;width: 600px;"  width="600" onerror="this.onerror=null;this.src='https://plot.ly/404.png';" /></a>


```python
%%HTML

# Em uma célula de código é possivel inserir o webmap
<iframe src="https://michelmetran.github.io/pages/folium/map/map_santos.html" width="800" height="300" frameborder="0"></iframe>
```

Mas não consigo inserir o mapa em uma célula de comentário, ou _markdown_.

CartoDB
<iframe width="100%" height="520" frameborder="0" src="https://michelmetran.carto.com/viz/7076681e-cf4b-11e4-ad33-0e4fddd5de28/embed_map" allowfullscreen webkitallowfullscreen mozallowfullscreen oallowfullscreen msallowfullscreen></iframe>

Iframe genérico
<iframe src="https://michelmetran.github.io/pages/folium/map_santos.html" width="800" height="300" frameborder="0"></iframe>

# Exercício completo


```python
states = os.path.join('data', 'us-states.json')
unemployement_data = os.path.join('data', 'us_unemployment.csv')
state_data = pd.read_csv(unemployement_data)

m = folium.Map(location=[48, -102], zoom_start=3)
```


```python
m.choropleth(
    geo_data=states,
    name='choropleth',
    data=state_data,
    columns=['State', 'Unemployment'],
    key_on='feature.id',
    fill_color='YlGn',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='Unemployment Rate %'
)

folium.LayerControl().add_to(m)    # Adiciona legenda

m.save('map2.html')
```


```python
#m
```

## Exportando o _Juptyter Notebook_ para outros formatos


```python
# %load '~/Documents/GitRepo/code_reference/files/get_jupyternotebook_name.py'
def get_jupyternotebook_name():
    """
    Returns the name of the current notebook as a string
    From https://mail.scipy.org/pipermail/ipython-dev/2014-June/014096.html
    :return: Returns the name of the current notebook as a string
    """

    from IPython.core.display import Javascript
    from IPython.display import display

    display(Javascript('IPython.notebook.kernel.execute("theNotebook = " + \
    "\'"+IPython.notebook.notebook_name+"\'");'))

    # Here are dragons
    return theNotebook
```


```python
# %load '~/Documents/GitRepo/code_reference/files/export_jupyter.py'
def export_jupyter(extensions=['html', 'markdown', 'latex', 'pdf']):
    """

    :return:
    """
    # Import packages
    import os
#    import subprocess
#    cmd = 'python script.py'

#    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
#    out, err = p.communicate()
#    result = out.split('\n')
#    for lin in result:
#        if not lin.startswith('#'):
#            print(lin)

    # Extensions
    for extension in extensions:
        os.system('jupyter nbconvert --to {} {} --output {}'.
                  format(extension, get_jupyternotebook_name(),
                         get_jupyternotebook_name().split('.')[0]))
        print(extension)

export_jupyter()
```


```python

```
