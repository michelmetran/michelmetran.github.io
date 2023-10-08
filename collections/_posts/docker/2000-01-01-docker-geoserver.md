---
title: "Docker: Geoserver"
date: 2023-10-08T00:00:00-03:00
last_modified_at: 2023-10-08T00:00:00-03:00
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



## Geoserver

Com Docker é possível instanciar facilmente o Geoserver. É uma ferramenta bastante útil para ter um GeoServer para chamar de seu!, além de aprender os comandos para explorar os Geoservers espalhados por ai, obtendo informação de mod mais assertivo.

A image no Geoserver está disponível no [Docker Hub](https://hub.docker.com/r/geonode/geoserver). Uma vez que estiver instalado corretamente, seguindo os passos abaixo, basta acessar o site http://localhost:8080/geoserver com as seguintes credenciais:

- username: admin
- password: geoserver

<br>

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
