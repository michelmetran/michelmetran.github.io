---
title: "PowerBI: Pipelines"
date: 2023-05-04T00:00:00-03:00
last_modified_at: 2023-09-07T00:00:00-03:00
excerpt_separator: "<!--more-->"
categories:
  - IT
  - data science
tags:
  - power bi
  - devops
---





Passo 1: Instalar "Power BI Actions" no AzureDevOps, na organização
https://marketplace.visualstudio.com/items?itemName=maikvandergaag.maikvandergaag-power-bi-actions

Passo 2:
https://youtu.be/qskIb2Hilv4?si=EmJS2bTw387IzZFh&t=91
Clicar em "App Registration" com nome (sugestão) "power-bi"
Após a criação, preciso dos seguintes dados:
- Application (client) ID
- Directory (tenant) ID

Passo 3:
https://youtu.be/qskIb2Hilv4?si=CN5U1BUS-EjW4ePH&t=146
Criar "Security Group" para a aplicação com nome (sugestão) "power-bi-sg"
Na seleção de membros, escolha a aplicação recem criada!

Passo 4:
https://youtu.be/qskIb2Hilv4?si=ZbQvffJAM8w1uEvQ&t=660
Clicar em "Certificat and Secret" para criar um "New Client Secret" (será necessário para definir o pipeline)
Após a criação, preciso dos seguintes dados:
- Client Secret

Passo 5:
https://youtu.be/qskIb2Hilv4?si=ZbQvffJAM8w1uEvQ&t=195
No PowerBI Admin Portal é necessário habilitar o "Security Group" recém criado para que ele possa fazer deploys.

Passo 7:
https://youtu.be/qskIb2Hilv4?si=CWtswRzGUV8MvrL9&t=362
Configurar o pipeline
