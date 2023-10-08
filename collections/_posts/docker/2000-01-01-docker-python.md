---
title: "Docker: Python"
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

A imagem fica bem maior que instalando um Ubuntu e um *python* dentro do Ubuntu.

```bash
docker pull python
docker images

mkdir python-img && cd python-img
nano app.py
nano Dockerfile

# Cria Imagem
docker image build -t app-python:1.0 .

# Roda a imagem
docker run -ti --name runapp1 app-python:1.0
```
