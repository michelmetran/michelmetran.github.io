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

**Notas:** Traçando paralelos, a aplicação criada atuará de forma similar à um usuário da organização que, por meio das credenciais, poderá publicar arquivos _.pbix_ nas _workspaces_ da organização!
{: .notice--info}

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

Também é necessário adicionar a _Application_ (ou _Service Principal_) com a permissão de, no mínimo, membro.

![](https://i.imgur.com/y2lgEOY.png)

<br>

---

### No Ambiente do AzureDevOps

Para isso é necessário instalar a extensão [Power BI Actions](https://marketplace.visualstudio.com/items?itemName=maikvandergaag.maikvandergaag-power-bi-actions) no AzureDevOps.

E, por fim, promover configução do _pipeline_. Em um primeiro momento fiz a configuração de maneira similar ao que o [vídeo do indiano](https://youtu.be/qskIb2Hilv4?si=CWtswRzGUV8MvrL9&t=362) sugere, ou seja,

1. Usando o _Azure Pipeline_, crio um _artifact_.
2. Usando o _Realease_, configuro a publicação do _artifact_ na _workspace_

![](https://i.imgur.com/xitZmlC.png)

<br>

Outra abordagem que usei posteriormente, e **é mais _clean_ (e portanto, melhor!)** , foi definir todas as etapas no arquivo `azure-pipelines.yml`, localizado na raiz do repositório git, no AzureDevOps, com o seguinte conteúdo

```yaml
# Pipeline criado para automatizar a publicação de
# arquivos .pbix em workspaces do Power BI
#
# Michel Metran
# Data: 05.10.2023
# Atualizado em: 17.10.2023
# -------------------------

trigger:
  - main

# Agent
pool:
  vmImage: windows-2019

# Variáveis
variables:
  # AJUSTAR
  NamePbixFile: "ANPPs.pbix"
  WorkspaceName: "Testes"
  PowerBIService: "power-bi-service-principal"

  # Debugar Pipeline
  system.debug: "true"

steps:
  # Copia o arquivo .pbix para Staging Directory
  - task: CopyFiles@2
    displayName: 'Copy Files to: "$(Build.ArtifactStagingDirectory)"'
    inputs:
      SourceFolder: $(Build.SourcesDirectory)
      Contents: "**/${{variables.NamePbixFile}}"
      TargetFolder: $(Build.ArtifactStagingDirectory)
      flattenFolders: true
      OverWrite: true

  # Publica arquivo do Staging Directory no Artifact
  # https://learn.microsoft.com/pt-br/azure/devops/pipelines/tasks/reference/publish-build-artifacts-v1
  - task: PublishBuildArtifacts@1
    displayName: "Publish Artifact to: $(Build.ArtifactStagingDirectory)"
    inputs:
      PathtoPublish: $(Build.ArtifactStagingDirectory)
      ArtifactName: my_artifact
      publishLocation: Container
      MaxArtifactSize: 0
      Parallel: false
      StoreAsTar: false

  # Publica Artifact na workspace
  - task: maikvandergaag.maikvandergaag-power-bi-actions.PowerBIActions.PowerBIActions@5
    displayName: "Power BI: Publish in Workspace"
    inputs:
      PowerBIServiceEndpoint: "$(PowerBIService)"
      WorkspaceName: "$(WorkspaceName)"
      PowerBIPath: "$(System.ArtifactsDirectory)/${{variables.NamePbixFile}}"
```

<br>

Ah!, e também é necessário definir o _Service Connection_, inserindo o _Application (Client) ID_, o _Directory (Tenant) ID_ e o _Secret_ da _Application_.

![](https://i.imgur.com/1p9CQk5.png)

<br>

---

## _Deploy_

Após todas essas configurações, ao fazer qualquer modificação nos arquivos do repositório _git_ e fizer um _push_ para "subir" as modificações, o _pipeline_ será disparado e o arquivo _.pbix_ definido será publicada na _workspace_ também definida no arquivo `azure-pipelines.yml`.

<br>

---

## Referências

Foram diversas as referências que usei para conseguir fazer o _deploy_ dos painéis automaticamente. Talvez o vídeo que importante foi o [PowerBI - CI/CD using Azure DevOps](https://youtu.be/qskIb2Hilv4?si=EmJS2bTw387IzZFh), de um indiano que foi explicando as etapas que segui.

O vídeo [Power BI Dataset CI/CD Pipeline (Azure Dev Ops, XMLA Endpoint, Tabular Editor & Service Connection)](https://www.youtube.com/watch?v=8NHVFuvHwoI) avança nas configurações, por trazer também a possibilidade de fazer _deploy_ do modelo tabular!

Ainda, durante a configuração do _pipeline_, tive dificuldades para fazer funcionar corretamente e, diante disso, escrevi a _issue_ [#508 Doesn't recognize my workspace](https://github.com/maikvandergaag/msft-extensions/issues/508) que pode trazer mais informações.
