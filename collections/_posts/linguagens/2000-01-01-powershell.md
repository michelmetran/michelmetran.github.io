---
title: "PowerShell"
date: 2023-10-09T00:00:00-03:00
last_modified_at: 2023-10-09T00:00:00-03:00
excerpt_separator: "<!--more-->"
#classes: wide
categories:
  - IT
tags:
  - powershell
  - linguagens
---

PowerShell é uma ferramenta de automação e configuração multiplataforma (Windows, Linux e macOS) que funciona bem com as suas ferramentas existentes e é otimizada para lidar com dados estruturados (por exemplo, JSON, CSV, XML, etc.), APIs REST e modelos de objetos. Ele inclui um _shell_ de linha de comando, um ambiente de script associado e um conjunto de *cmdlets*.

PowerShell é um _shell_ moderno que inclui as melhores características de outros _shells_ populares. Ao contrário da maioria dos _shells_ que só aceitam e retornam texto, o PowerShell aceita e retorna objetos .NET. O _shell_ inclui os seguintes recursos:

- Histórico de linha de comando robusto
- Edição de linha de comando intuitiva
- Suporte a tabulação para completar nomes de comandos e parâmetros
- Suporte a pipelines para encadear comandos e lidar com grandes volumes de dados
- Formatação flexível e saída para várias fontes e formatos (por exemplo, console, GUI, arquivos, impressoras, etc.)
- Um grande conjunto de ferramentas integradas (cmdlets) que executam tarefas comuns do sistema
- Um amplo conjunto de provedores que permitem acessar dados armazenados em diferentes formatos e locais
- Uma linguagem de script poderosa que permite aos usuários criar suas próprias ferramentas personalizadas
- Uma extensa comunidade que fornece recursos, documentação, tutoriais, exemplos e módulos

<br>

Para instalar o PowerShell no Windows, existem várias formas possíveis. Cada método de instalação é projetado para suportar diferentes cenários e fluxos de trabalho. Escolha o método que melhor se adapte às suas necessidades3. Alguns dos métodos disponíveis são:

- **_Winget_**: forma recomendada de instalar o PowerShell em clientes Windows
- **_Pacote MSI_**: melhor escolha para servidores Windows e cenários de implantação empresarial
- **_Pacote ZIP_**: forma mais fácil de "carregar lateralmente" ou instalar várias versões
- **_Ferramenta global .NET_**: uma boa escolha para desenvolvedores .NET que instalam e usam outras ferramentas globais
- **_Pacote da Microsoft Store_**: uma forma fácil de instalar para usuários casuais do PowerShell, mas tem limitações

<br>

---

## Alguns Comandos

```powershell
# Reinicia PC
shutdown -r -t 01
```
