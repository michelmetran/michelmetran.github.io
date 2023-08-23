---
title: 'Remote Desktop: Windows'
date: 2023-02-02T14:34:30-03:00
last_modified_at: 2023-02-02T14:34:30-03:00
tags: [vms, remote desktop, WOL]
---

Uma vez utilizando *desktops* remotos (que tenham sistema operacional Windows), me deparei com um problema: por esquecimento, solicitava o desligamento da máquina e perdia acesso.

Existem duas maneiras de contornar esse problema:

1. Habilitar o [_Wake on Lan_](./../hardware/2000-01-01-wake.md) no PC, de forma que seja possível ligar o PC quando estiver desligado.
2. Impedir o acesso aos comandos de Desligar, Reiniciar, Dormir e Hibernar.

<br>

Essa segunda opção é configurada no **Editor de Política de Grupo Local**, acessado por meio do comando `gpedit.msc` (Win+R), por meio dos seguintes procedimentos:

1. Acesse _Configuração de Usuário/Menu Iniciar e Barra de Tarefa_
2. Habilite a opção _Remover e Impedir o acesso aos comandos de Desligar, Reiniciar, Dormir e Hibernar_

<br>

Tais informações foram obtidas no artigo [superuser: **How to remove shutdown option in start menu of Windows 10**](https://superuser.com/questions/983797/how-to-remove-shutdown-option-in-start-menu-of-windows-10) que traz mais detalhes.

<br>

---

**IMPORTANTE**

Habilitar a opção acima não impede os usuários de desligarem o PC. Os comandos que devem ser lembrados, quando necessário reiniciar o PC, são:

- `shutdown /s` para desligar o computador
- `shutdown /r` para reiniciar o computador
