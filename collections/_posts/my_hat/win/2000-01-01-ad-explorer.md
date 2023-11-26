---
title: "Active Directory"
date: 2019-01-01T00:00:00-03:00
last_modified_at: 2023-11-08T00:00:00-03:00
excerpt_separator: "<!--more-->"
categories:
  - IT
  - Hacks
tags:
  - firma
---

O [**Active Directory (AD) Explorer**](https://learn.microsoft.com/en-us/sysinternals/downloads/adexplorer) é um visualizador e editor avançado do Active Directory (AD). Ele permite que você navegue facilmente em um banco de dados do AD, defina locais favoritos, visualize propriedades e atributos de objetos sem precisar abrir caixas de diálogo, edite permissões, visualize o esquema de um objeto e execute pesquisas sofisticadas que você pode salvar e reexecutar

O AD Explorer também inclui a capacidade de salvar instantâneos de um banco de dados do AD para visualização e comparações off-line. Quando você carrega um instantâneo salvo, pode navegar e explorá-lo como faria com um banco de dados ao vivo. Se você tiver dois instantâneos de um banco de dados do AD, poderá usar a funcionalidade de comparação do AD Explorer para ver quais objetos, atributos e permissões de segurança mudaram entre eles. O AD Explorer é uma ferramenta gratuita da Microsoft e pode ser baixado no site da [SysInternals](https://learn.microsoft.com/en-us/sysinternals/).

<br>

---

Comando para adicionar a possibilidade do _PowerShell_ ver coisas do AD

```powershell
Get-WindowsCapability -Online | Where-Object {$\_.Name -like "_ActiveDirectory.DS-LDS_"} | Add-WindowsCapability -Online
```

<br>

---

## Referências

- [Finding Pwned Passwords in Active Directory](https://safepass.me/2020/02/25/finding-pwned-passwords-in-active-directory/)
- [Convert ASCII Codes to Characters](https://www.browserling.com/tools/ascii-to-text)
- [Extract Clear Text Passwords from Active Directory](https://www.youtube.com/watch?v=qnTHtTCe5ck)
- [How to Crack an Active Directory Password in 5 Minutes or Less](https://www.semperis.com/blog/easy-hacking-active-directory-password/)
