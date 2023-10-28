---
title: "Docker: Geoserver"
date: 2023-10-08T00:00:00-03:00
last_modified_at: 2023-10-08T00:00:00-03:00
excerpt_separator: "<!--more-->"
categories:
  - IT
  - Docker
  - Open Geodata
tags:
  - python
  - pycharm
  - jupyter
  - package
  - pandas
---





O [_GeoServer_](https://geoserver.org/) é um software livre que permite o desenvolvimento de soluções de webmapping, ou seja, a visualização e edição de dados geoespaciais na web. Ele segue os padrões abertos da Open Geospatial Consortium ([_OGC_](https://www.ogc.org/)), que garantem a interoperabilidade entre diferentes sistemas e fontes de dados.

Com o _GeoServer_, é possível publicar mapas e dados de vários formatos, como:

- _Shapefile_
- PostGIS
- Oracle Spatial
- GeoTiff
- NetCDF, etc.

<br>

Os dados podem ser acessados por meio de interfaces baseadas em protocolos como WMS, WFS, WCS, WPS e Tile Caching. O GeoServer também oferece suporte a estilos personalizados usando o padrão SLD, filtros OGC, transações WFS-T e outras funcionalidades.

O GeoServer é baseado em servlets Java e pode rodar em qualquer servidor _web_ que suporte essa tecnologia. Ele é projetado para ser extensível e fácil de usar, com uma ferramenta de administração via _web_ que simplifica a configuração e o gerenciamento dos dados.

<br>

---

## Docker

Utilizando Docker é possível instanciar facilmente o _Geoserver_. Muito útil ter um GeoServer para chamar de seu!, além de aprender os comandos para explorar os _Geoservers_ espalhados por ai, obtendo informação de modo mais assertivo.

A image no Geoserver está disponível no [Docker Hub](https://hub.docker.com/r/geonode/geoserver). Uma vez que estiver instalado corretamente, seguindo os passos abaixo, basta acessar o site http://localhost:8080/geoserver com as seguintes credenciais:

- username: admin
- password: geoserver

```bash
# Pull Docker Image
docker pull geonode/geoserver

# Download
wget https://build.geo-solutions.it/geonode/geoserver/latest/data-2.18.3.zip --no-check-certificate -P ~/Downloads/

# Create Directory
sudo mkdir /opt/geoserver/

# Unzip
sudo unzip ~/Downloads/data-2.18.3.zip -d /opt/geoserver/

# Deleta Pasta
rm ~/Downloads/data-2.18.3.zip

# Run Docker
docker run --name my_geoserver -v /var/run/docker.sock:/var/run/docker.sock -v /opt/geoserver/data/:/geoserver_data/data -d -p 8080:8080 geonode/geoserver

# Remove
docker rm -f my_geoserver
```
