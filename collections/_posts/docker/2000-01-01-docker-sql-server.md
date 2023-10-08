---
title: "Docker: SQL Server"
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


DB Management Studio


user: sa
password: <YourStrong@Passw0rd>

> https://www.youtube.com/watch?v=0E0sU_z74HM


```bash
docker run \
-e "ACCEPT_EULA=Y" \
-e "MSSQL_SA_PASSWORD=<YourStrong@Passw0rd>" \
-p 1433:1433 \
--name sql1 \
--hostname sql1 \
-d \
mcr.microsoft.com/mssql/server:2022-latest
```
