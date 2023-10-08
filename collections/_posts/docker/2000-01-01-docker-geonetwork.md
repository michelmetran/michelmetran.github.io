---
title: "Docker: Geonetwok"
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

https://hub.docker.com/_/geonetwork

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

# É necessário usar o elasticsearch como  index.... um Docker COmpose funcionaria (http://elasticsearch:9200)
#docker run --name my_geonetwork -d -p 8080:8080 -e DATA_DIR=/var/lib/geonetwork/data -e GEONETWORK_DB_NAME=/var/lib/geonetwork/db/gn geonetwork

# Remove
docker rm -f my_geonetwork

```
