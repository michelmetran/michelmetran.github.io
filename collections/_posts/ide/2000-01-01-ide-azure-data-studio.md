---
title: "Azure Data Studio"
date: 2023-05-04T00:00:00-03:00
last_modified_at: 2023-11-13T00:00:00-03:00
categories:
  - IT
tags:
  - ide
  - sql
  - Azure Data Studio
---

O **_Azure Data Studio_** é uma ferramenta de gerenciamento e desenvolvimento de dados de código aberto, moderna e multiplataforma, projetada para simplificar o panorama de dados. Ele é construído para profissionais de dados que usam o SQL Server e bancos de dados Azure localmente ou em ambientes multicloud.

O Azure Data Studio oferece uma experiência de ferramentas unificada para profissionais de dados, com um editor de consulta integrado, notebooks Jupyter nativos e um terminal. Ele também oferece suporte robusto a idiomas para SQL, PowerShell, Python, KQL, Apache Spark TM e PySpark para gerenciar e consultar o SQL Server, PostgreSQL e Azure Data Explorer.

O Azure Data Studio é uma ferramenta de análise de dados moderna, híbrida, multiplataforma e de _software_ livre, projetada para simplificar o panorama de dados. Você pode baixar o Azure Data Studio gratuitamente no [site da _Microsoft_](https://learn.microsoft.com/pt-br/azure-data-studio/).

<br>

---

## _Bugs_

### Multiplas Instâncias

Passei a enfrentar o seguinte problema quando eu tentava abrir multiplas instâncias: ao abrir, aparecia uma tela preta e os componentes do aplicativo não carregavam.

Li o _post_ [How to Fix Azure Data Studio Blank / Black Screen](https://metadataconsulting.blogspot.com/2019/03/How-to-Fix-Azure-Data-Studio-Blank-Black-Screen.html) e _issue_ [#22022: Open folder doesn't work on new window](https://github.com/microsoft/azuredatastudio/issues/22022), que sugeria que fosse aberta a nova instância por meio do terminal, com o comando:

```shell
azuredatastudio .
```

<br>

Por algum tempo usei o recurso. Passado algum tempo adotei solução melhor. Lendo a _issue_ [#22225: Add "Open With Azure Data Studio" to Explorer](https://github.com/microsoft/azuredatastudio/issues/22225), optei por criar uma entrada no registro do Windows que me permitisse abrir o Azure Data Studio a partir do menu de contexto (botão direito).

Criei um arquivo `.reg` com o seguinte conteúdo:

```
Windows Registry Editor Version 5.00

;Adiciona AzureDataStudio no menu de Contexto do Windows 11
;https://www.quora.com/How-do-you-add-an-option-to-the-right-click-context-menu-in-Windows-Explorer
;https://github.com/microsoft/azuredatastudio/issues/22022
;https://github.com/microsoft/azuredatastudio/issues/22225
;Michel Metran
;Novembro de 2023


[HKEY_CLASSES_ROOT\Directory\background\shell\AzureDataStudio]
"Icon"="\"C:\\Program Files\\Azure Data Studio\\azuredatastudio.exe\""
@="Open with Azure Data Studio"

[HKEY_CLASSES_ROOT\Directory\background\shell\AzureDataStudio\command]
@="\"C:\\Program Files\\Azure Data Studio\\azuredatastudio.exe\" \".\""
```

<br>

Uma vez criado o arquivo, basta executar. Deixei o arquivo disponível para [_download_](/assets/attachments/azure_data_studio/Add%20Azure%20Right%20Click.reg).

<br>

---

## Extensões

### ER Diagram

Em 18.10.2023 encontrei a extensão [Schema Visualization](https://github.com/R0tenur/visualization), que possibilita ver diagramas ER.

Interessante notar que há muita gente solicitando o [Support mermaid diagrams in markdown file preview](https://developercommunity.visualstudio.com/t/support-mermaid-diagrams-in-markdown-file-preview/817244).

<br>

---

### Coleção

Encontrei postagem que indica uma coleção de extenões para o Azure Data Studio [These are the extensions I have installed on Azure Data Studio](https://bornsql.ca/blog/these-are-the-extensions-i-have-installed-on-azure-data-studio/)
