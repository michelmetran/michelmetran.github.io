---
title: "PowerBI: Enxugando Dimensões"
date: 2023-05-04T00:00:00-03:00
last_modified_at: 2023-09-07T00:00:00-03:00
excerpt_separator: "<!--more-->"
author: Michel Metran
toc: false
classes: wide
categories:
  - IT
  - data science
tags:
  - power bi
  - Dimensões
  - Tabela Fato
---

Um modelo de dados no Power BI é uma forma de organizar e relacionar os dados que serão usados para criar relatórios e _dashboards_. Um modelo de dados pode conter várias tabelas, colunas, medidas, relações e hierarquias que definem como os dados são estruturados e como eles se conectam entre si. Um modelo de dados bem projetado pode facilitar a análise e a visualização dos dados, além de melhorar o desempenho e a escalabilidade do Power BI.

Diante disso, enfrentada o problema: como lidar com **_Dimensões_** que apresentam diversas ocorrências que não existem na **_tabela Fato_**.

Para isso a solução que adotei é:

1. Adicionar a Dimensão, contendo todos os possíveis registros. No caso em tela as dimensões são: _Situação_ e _Cargos_.

![PowerBI Atendimentos](https://i.imgur.com/FIf8Bxa.png)

<br>

2. Usando o **PowerQuery**, fazer um _join_ obtendo apenas os registros que "pareiam" com a _tabela Fato_. No caso em tela, a _tabela Fato_ é _Atendimentos_.

```m
= Table.NestedJoin(Situacao, {"IdSituacao"}, Atendimentos, {"IdSituacao"}, "Expand", JoinKind.Inner)
```

![PowerQWuery Join](https://i.imgur.com/1EjCis0.png)

<br>

Dessa forma, consigo criar uma tabela virtual no meu modelo de dados do PowerBI, contendo apenas os registros das _Situações_ que ocorrem nos _Atendimentos_. Isso evita uma série de informações "Em Branco" nas métricas do PowerBI e possibilita a reutilização das _Dimensões_ em dezenas de paineis.
