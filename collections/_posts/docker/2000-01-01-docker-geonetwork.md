---
title: "Docker: <i>Geonetwok</i>"
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

O [_GeoNetwork_](https://geonetwork-opensource.org/) é um sistema de gerenciamento de informações geoespaciais aberto e baseado em padrões, que permite o acesso a dados e mapas georreferenciados de diferentes fontes, através de metadados descritivos.

O objetivo do _GeoNetwork_ é facilitar o compartilhamento de informação entre organizações e usuários, utilizando os recursos da Internet. O _GeoNetwork_ faz parte da Open Source Geospatial Foundation ([_OSGeo_](https://www.osgeo.org/)) e pode ser usado para catalogar e compartilhar metadados geográficos, controlar o acesso de usuários, realizar comunicação com outros sistemas e importar metadados de outros software

<br>

---

## Docker

No [DockerHub](https://hub.docker.com/_/geonetwork) há uma imagem oficial do _GeoNetwork_.

http://localhost:8080/geonetwork

- Default user: admin
- Default password: admin

```bash
# Pull Docker Image
docker pull geonetwork

# ddd
mkdir /var/lib/geonetwork
mkdir /var/lib/geonetwork/data
mkdir /var/lib/geonetwork/db
mkdir /var/lib/geonetwork/db/gn

# Run Docker
docker run --name my_geonetwork -d -p 8080:8080 geonetwork

docker run --name my_geonetwork -d -p 8080:8080 -e ES_HOST=elasticsearch geonetwork

# É necessário usar o elasticsearch como  index.... um Docker Compose funcionaria (http://elasticsearch:9200)
#docker run --name my_geonetwork -d -p 8080:8080 -e DATA_DIR=/var/lib/geonetwork/data -e GEONETWORK_DB_NAME=/var/lib/geonetwork/db/gn geonetwork

# Remove
docker rm -f my_geonetwork
```
