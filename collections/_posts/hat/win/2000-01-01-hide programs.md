---
title: "Escondendo programas"
excerpt_separator: "<!--more-->"
tags: [python, pycharm, jupyter, package]
---

- Passo 1: Instalar em dispositivo externo
- Passo 2: Remove a entrada na sessão "Adicionar e Remover Programas"

Navigate to this location:

```
HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall
```

<br>

Find the software you wish to hide.
In the right pane, find the value name DisplayName. Right-click it and click Rename. Name it anything you like.

<br>

---

## Referências

- [How to Hide an Entry in the Add/Remove Programs](https://www.wikihow.com/Hide-an-Entry-in-the-Add/Remove-Programs#:~:text=Type%20in%20regedit%20and%20hit%20%E2%86%B5%20Enter%20.,-2&text=2-,Navigate%20to%20this%20location%3A%20HKEY_LOCAL_MACHINE%5CSOFTWARE%5CMicrosoft%5CWindows,software%20you%20wish%20to%20hide.&text=Right%2Dclick%20in%20the%20open,select%20New%E2%86%92DWORD%20Value)
