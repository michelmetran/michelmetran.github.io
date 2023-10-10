---
title: "PowerBI e PowerShell"
date: 2023-10-09T00:00:00-03:00
last_modified_at: 2023-10-09T00:00:00-03:00
excerpt_separator: "<!--more-->"
categories:
  - IT
  - Data Science
tags:
  - PowerBI
  - PowerShell
---

O PowerBI é uma ferramenta de análise de dados que permite criar relatórios e _dashboards_ interativos. Para manejar o PowerBI por meio do PowerShell, é preciso instalar os cmdlets do Power BI, que são comandos que permitem interagir com os recursos do PowerBI, como _workspaces_, relatórios, conjuntos de dados e muito mais.

Com os cmdlets do PowerBI, é possível automatizar tarefas como publicar relatórios, atualizar conjuntos de dados, gerenciar permissões e invocar a API do Power BI. Para usar os cmdlets do Power BI, é necessário se autenticar no Power BI usando o comando `Login-PowerBI` e fornecer as credenciais da conta ou do aplicativo. Depois disso, é possível usar os outros cmdlets para executar as ações desejadas no PowerBI.

<br>

----

## PowerShell

Lendo o arrtigo [Cmdlets para PowerShell - Administrando o Power BI like a Pro!](http://www.rafaelmendonca.com/2019/07/power-bi-cmdlet-powershell-admin.html) passei a entender um pouco do uso do PowerShell para manejar o PowerBI.

Outro artigo que dá caminhos interessantes tanmbém para usar o PowerBi com o PowerShell é o [Working with PowerShell in Power BI](https://powerbi.microsoft.com/pt-br/blog/working-with-powershell-in-power-bi/)

```powershell
# Instalando o módulo necesário
Install-Module -Name MicrosoftPowerBIMgmt

# Conectando com o Serviço (com usuário e senha)
Connect-PowerBIServiceAccount

# Conectando com o Serviço (com service principal)
Connect-PowerBIServiceAccount -ServicePrincipal -Credential (Get-Credential) -Tenant 2dbd8499-508d-4b76-a31d-ca39cb3d8f1d

# Get Workspaces
Get-PowerBIWorkspace

# Get Workspaces
Get-PowerBIWorkspace -All
Get-PowerBIWorkspace -Scope Organization -Include All
Get-PowerBIWorkspace -Scope Organizition

# Get Workspace Specific
Get-PowerBIWorkspace -Name 'CTIC - Indicadores BI - Desenvolvimento'

$workspace = Get-PowerBIWorkspace -Name 'test workspace'

# Push New Report
New-PowerBIReport -WorkspaceId 52bcfd95-b2cf-4a1b-80da-154d24fd4daf -Path 'C:\temp\Democmdlet.pbix'

# Exporta Lista de Reports
Get-PowerBIReport -Scope Organization | Export-Csv -Path 'C:\temp\reports.csv' -Encoding UTF8

# Exporta Lista de Datasets
Get-PowerBIDatasets -Scope Organization | Export-Csv -Path 'C:\temp\datasets.csv' -Encoding UTF8

# Capacities
Get-PowerBICapacity

# Get Token
Get-PowerBIAccessToken

# Upload report (Personal)
New-PowerBIReport -Path 'ANPPs.pbix' -Name 'Report22'

# Upload report (Teams)
New-PowerBIReport -Path '.\ANPPs.pbix' -Name 'ANPPs2' -Workspace ( Get-PowerBIWorkspace -Name 'CTIC - Indicadores BI - Desenvolvimento' ) -ConflictAction CreateOrOverwrite

# Printa
Write-host "Printing the Data of Repo path variable"

# Desconecta
Disconnect-PowerBIServiceAccount
```

<br>

Acho que é de outro módulo

```powershell
# Loga
Login-PowerBI
```
