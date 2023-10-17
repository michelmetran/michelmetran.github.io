---
title: "PowerBI: CD/CI"
date: 2023-09-04T00:00:00-03:00
last_modified_at: 2023-10-17T00:00:00-03:00
excerpt_separator: "<!--more-->"
categories:
  - IT
  - Data Science
tags:
  - Power BI
  - AzureDevOps
  - DevOps
---

## Fundamentos

O CD/CI (entrega contínua e integração contínua) é uma abordagem de desenvolvimento de _software_ em que todos os desenvolvedores trabalham juntos em um repositório compartilhado de código e, conforme as alterações são feitas, há um processo de _build_ automatizado para detectar problemas de código.

Agora imaginemos um cenário onde há um repositório _git_, na estrutura do AzureDevOps, no qual existem arquivos _markdown_, arquivos _.sql_, arquivos _.pbix_ entre outros tantos e desejamos, a cada _push_, publicar a nova versão do arquivo _.pbix_ em uma _workspace_.

Isso é possível utilizando os conceitos de CD/CI!! Por meio da configuração de _Pipelines_, no ambiente do AzureDevOps, é possível fazer o _"deploy"_ automático de painéis em _workspaces_, com auxílio da extensão [Power BI Actions](https://marketplace.visualstudio.com/items?itemName=maikvandergaag.maikvandergaag-power-bi-actions) do [Maik van der Gaag](https://marketplace.visualstudio.com/publishers/maikvandergaag).

Abaixo seguem explicações para dar início a essa configuração!

<br>

---

## Configurações

### No Ambiente do Portal Azure

É necessário registrar um novo aplicativo no Portal Azure, dentro do _Microsoft Entra ID_ (anteriormente chamado de _Active Diretory_). Para isso basta ir em _Microsoft Entra ID_ e, dentro da estrutura da sua organização, ir em _App Registrations_.

**Crie uma _Application_** e dê o nome de sua preferêrencia. É necessário anotar, para usar depois, o _Application (Client) ID_ e o _Directory (Tenant) ID_.

![](https://i.imgur.com/Pq7Ykh8.png)

<br>

É também necessário **criar credenciais** para essa _Application_! Para isso basta ir em _Certificates & secrets_ e criar uma. Anote o _secret_ criado!

![](https://i.imgur.com/L1Hwac6.png)

<br>

Por fim, é **necessário criar um grupo**, do tipo _Security_, na estrutura do _Tenant_ da organização, no qual deve ser adicionado, como membro, a _Application_ recem criada. Esse grupo será usado nas configurações do Power BI. Dei o nome de _Power BI CD-CI_ para o grupo.

![](https://i.imgur.com/JAhK773.png)

<br>

---

### No Ambiente do PowerBI

No [PowerBI Admin Portal](https://app.powerbi.com/admin-portal/tenantSettings) é necessário habilitar o _Security Group_ recém criado para que ele possa fazer _deploys_ de paineis nas _workspaces_.

![](https://i.imgur.com/SS2lSBt.png)

<br>

---

### No Ambiente do AzureDevOps

Para isso é necessário instalar a extensão [Power BI Actions](https://marketplace.visualstudio.com/items?itemName=maikvandergaag.maikvandergaag-power-bi-actions) no AzureDevOps.

E, por fim, promover configução do _pipeline_. Em um primeiro momento fiz a configuração de maneira similar ao que o [vídeo do indiano](https://youtu.be/qskIb2Hilv4?si=CWtswRzGUV8MvrL9&t=362) sugere, ou seja,

1. Usando o _Azure Pipeline_, crio um _artifact_.
2. Usando o _Realease_, configuro a publicação do _artifact_ na _workspace_

![](https://i.imgur.com/xitZmlC.png)

<br>

Outra abordagem que usei foi definir todas as etapas no arquivo `azure-pipelines.yml`, com o seguinte conteúdo

```yaml
trigger:
  - main

# Definição do Agent
pool:
  vmImage: windows-2019

# Definição de Variáveis
variables:
  system.debug: "true" # Ideal para debugar o pipeline

  # Static Variable
  NamePbixFile: "ANPP.pbix"

steps:
  # Copia o arquivo .pbix para a pasta de artifacts
  - task: CopyFiles@2
    displayName: 'Copy Files to: "$(Build.ArtifactStagingDirectory)"'
    inputs:
      SourceFolder: $(Build.SourcesDirectory)
      Contents: "bi/${{variables.NamePbixFile}}"
      TargetFolder: $(Build.ArtifactStagingDirectory)
      flattenFolders: true
      OverWrite: true

  # Copia o conteúdo da pasta de artifacts para o AzurePipelines
  - task: PublishBuildArtifacts@1
    displayName: "Publish Artifact to: $(Build.ArtifactStagingDirectory)"
    inputs:
      PathtoPublish: $(Build.ArtifactStagingDirectory)
      ArtifactName: my_bi_artifact
      publishLocation: FilePath
      TargetPath: "$(Build.ArtifactStagingDirectory)"

  # Release: publica na workspace
  - task: maikvandergaag.maikvandergaag-power-bi-actions.PowerBIActions.PowerBIActions@5
    displayName: "Power BI Action: Publish"
    inputs:
      PowerBIServiceEndpoint: "power-bi-service-principal"
      WorkspaceName: Testes
      PowerBIPath: "$(Build.ArtifactStagingDirectory)/${{variables.NamePbixFile}}"
```

<br>

---

## Referências

Foram diversas as referências que usei para conseguir fazer o _deploy_ dos painéis automaticamente. Talvez o vídeo que importante foi o [PowerBI - CI/CD using Azure DevOps](https://youtu.be/qskIb2Hilv4?si=EmJS2bTw387IzZFh), de um indiano que foi explicando as etapas que segui.

O vídeo [Power BI Dataset CI/CD Pipeline (Azure Dev Ops, XMLA Endpoint, Tabular Editor & Service Connection)](https://www.youtube.com/watch?v=8NHVFuvHwoI) avança nas configurações, por trazer também a possibilidade de fazer _deploy_ do modelo tabular!
