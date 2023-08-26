---
title: "PowerShell"
date: 2019-06-13T15:34:30-04:00
last_modified_at: 2022-06-29T00:00:00-03:00
excerpt_separator: "<!--more-->"
categories:
  - IT
tags:
  - command line
  - apps
  - powershell
---

O [PowerShell](https://learn.microsoft.com/pt-br/powershell/scripting/overview?view=powershell-7.2) é uma solução de automação de tarefas multiplataforma que consiste em um shell de linha de comando, em uma linguagem de script e uma estrutura de gerenciamento de configuração. O PowerShell pode ser executado no Windows, Linux e macOS.

<br>

---

## Atualiza

Sempre que abria o PowerShell, recebia um alerta sobre atualização. Utilizando o comando abaixo, no PowerShell 6, é possível atualizar (rodar como admin) para o PS7, conforme explicado, em detalhes, no artigo [How to Install and Update PowerShell 6](https://www.thomasmaurer.ch/2019/03/how-to-install-and-update-powershell-6/).

```powershell
# Atualiza
iex "& { $(irm https://aka.ms/install-powershell.ps1) } -UseMSI"
```

<br>

---

## Problemas e Soluções

Em out.22 o PowerShell deixou de funcionar no PC e descobri, com [How To Fix PowerShell Has Stopped Working or Not Opening In Windows 10](https://www.youtube.com/watch?v=QfCKCasBef4) que se fazia necessário.

1. Command Line (_Run as Admin_) `sfc /scannow`
