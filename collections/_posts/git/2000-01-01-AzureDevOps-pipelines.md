---
title: "Azure DevOps: CD/CI"
date: 2023-10-04T00:00:00-03:00
last_modified_at: 2023-10-04T00:00:00-03:00
excerpt_separator: "<!--more-->"
categories:
  - IT
  - Hacks
tags:
  - AzureDevOps
  - DevOps
  - git
  - yaml
---

```yaml
  # # Existem dezenas de variáveis pré definidas
  # # https://learn.microsoft.com/pt-br/azure/devops/pipelines/build/variables
  # - script: |
  #     echo Add other tasks to build, test, and deploy your project.
  #     echo See https://aka.ms/yaml
  #     echo ${{variables.NamePbixFile}}
  #     echo ----------------------------
  #     echo Build.Id: $(Build.Id)
  #     echo Build.ArtifactStagingDirectory: $(Build.ArtifactStagingDirectory)
  #     echo Build.ArtifactsDirectory: $(Build.ArtifactsDirectory)
  #     echo Build.DefaultWorkingDirectory: $(Build.DefaultWorkingDirectory)
  #     echo Build.SourcesDirectory: $(Build.SourcesDirectory)
  #     echo Build.SourceBranch: $(Build.SourceBranch)
  #     echo Build.DefinitionName: $(Build.DefinitionName)
  #     echo ----------------------------
  #     echo System.ArtifactsDirectory: $(System.ArtifactsDirectory)
  #     echo ----------------------------
  #     echo artifactsPath: $(artifactsPath)
  #   displayName: 'Entendendo Variáveis'

  # # Pasta dos Artifacts
  # - script: |
  #     echo ArtifactStagingDirectory: $(Build.ArtifactStagingDirectory)

  #   displayName: 'Pasta dos Artifacts'
# Outros
# - script: echo Hello, world!
#   displayName: 'Run a one-line script'

# - script: |
#     echo Add other tasks to build, test, and deploy your project.
#     echo See https://aka.ms/yaml
#   displayName: 'Run a multi-line script'
```
