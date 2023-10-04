---
title: "PowerBI: Criando Dimensões a partir da Fato"
date: 2023-05-04T00:00:00-03:00
last_modified_at: 2023-10-04T00:00:00-03:00
excerpt_separator: "<!--more-->"
author: Michel Metran
toc: false
classes: wide
categories:
  - IT
  - Data Science
tags:
  - power bi
  - dimensões
  - tabela fato
---

Um modelo de dados no Power BI é uma forma de organizar e relacionar os dados que serão usados para criar relatórios e _dashboards_. Um modelo de dados pode conter várias tabelas, colunas, medidas, relações e hierarquias que definem como os dados são estruturados e como eles se conectam entre si. Um modelo de dados bem projetado pode facilitar a análise e a visualização dos dados, além de melhorar o desempenho e a escalabilidade do Power BI.

Diante disso, enfrentava o seguinte problema: eu tinha uma **_Tabela Fato_** contendo centenas de registros. Esses registros poderiam ser de dois sistemas diferentes e havia uma coluna que indicava qual era o Sistema:

- Sistema A
- Sistema B

<br>

Imaginemos outros exemplo: uma tabela fato com o registro de vendas. As vendas podem ter sido feitas por dois canais de atendimento:

- _Online_
- Presencial

<br>

Para isso a solução que adotei é:

1. Usando o **PowerQuery**, usar a função `Table.Distinct` para obter os registros únicos de uma _Tabela Fato_, criando uma _Dimensão_

```m
= Table.Distinct(Table.SelectColumns(Atendimentos, "SistemaControle"))
```

![PowerQuery Table Distinct](https://i.imgur.com/04JrJ4J.png)

<br>

Dessa forma, consigo criar uma tabela virtual no meu modelo de dados do PowerBI, contendo apenas os registros dos _Sistemas de Controle_ que ocorrem nos _Atendimentos_.
