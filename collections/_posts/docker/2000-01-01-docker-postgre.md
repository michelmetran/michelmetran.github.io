---
title: "Docker: PostGres"
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

- https://hub.docker.com/_/postgres

```bash
# Install
docker pull postgres

# Run
docker run \
--name db-postgres \
-e "POSTGRES_PASSWORD=Senha123" \
-e "POSTGRES_USER=michel" \
-p 5432:5432 \
-d \
postgres
```

```bash
# Others Parameters
# https://imasters.com.br/banco-de-dados/postgresql-docker-executando-uma-instancia-e-o-pgadmin-4-partir-de-containers
docker run \
--name db-postgres-groffe \
-e "POSTGRES_PASSWORD=Senha123" \
-p 5432:5432 \
--network=postgres-network \
-v /home/renatogroffe/Desenvolvimento/PostgreSQL:/var/lib/postgresql/data \
-d \
postgres
```
