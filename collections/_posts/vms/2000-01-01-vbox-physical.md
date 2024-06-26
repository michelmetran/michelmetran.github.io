---
title: "Virtual Box: Máquina Física para Virtual"
date: 2023-05-04T00:00:00-03:00
last_modified_at: 2023-05-04T00:00:00-03:00

excerpt_separator: "<!--more-->"
categories:
  - IT
tags:
  - python
  - pycharm
  - jupyter
  - package
  - pandas
#layout: post
#title: Jupyter Notebook
#subtitle: Exercícios e Referências
#tags: [python, pycharm, jupyter, package]
#image: /img/posts/jupyter_icon.png
#bigimg: /img/posts/jupyter_big.png
#gh-repo: michelmetran/package_jupyter
#gh-badge: [follow, star, watch, fork]
#comments: true
---

Visando fazer testes com o Sistema Operacional instalado no PC, sem risco de corrompe-lo, é possível clonar o sistema instalado na máquina física, em um arquivo _.vhd_, para ser configurado como máquina virtual. Fiz isso seguindo passos apresentados nesse vídeo: [YouTube: Physical to Virtual (P2V) Windows 10 with VirtualBox](https://www.youtube.com/watch?v=6wVJUimaq2U).

Notei que tutoriais mais antigos apresentavem uma série de passos adicionais para criar partições ocultas do Windows, possibilitando o _boot_.
[How to: Windows 10 Physical to VirtualBox](https://community.spiceworks.com/how_to/148559-windows-10-physical-to-virtualbox). Aparentemente isso não se faz mais necessário.

<br>

---

## Disk2vhd

Utilizando o aplicativo SysInternal [Disk2vhd](https://docs.microsoft.com/pt-br/sysinternals/downloads/disk2vhd) é possível converter uma máquina física, ou seja, um Sistema operacional instalado em um PC, em um arquivo _.vhd_

![](https://i.imgur.com/ThhnTUx.png)

<br>

O processo pode ser demorado e necessita que você tenho acesso de administrador no Windows _host_ para copiar o Sistema Operacional.

![](https://i.imgur.com/wYFBMNE.png)

<br>

---

## Passos

Após feito isso, usando o VirtualBox eu criei nova máquina, com configurações simples, e indiquei um disco existente, ou seja, o arquivo _.vhd_ recem criado.

Abri minha máquina virtual, deletei alguns programas visando "dar uma limpada". Removi bastante coisa!

<br>

---

## Compactação

Após isso, com a máquina mais leve, converti a máquina para o formato _.vdi_, usando os comandos abaixo.

```powershell
# No Windows, vai até a pasta de instalação
cd C:\Program Files\Oracle\VirtualBox

# Outros
VBoxManage.exe clonemedium disk "E:\hostname.vhd" "E:\hostname-dynamic.vdi" --variant Standard --format vdi

# Infos
VBoxManage.exe showmediuminfo "E:\hostname-dynamic.vdi"

# Compact
VBoxManage.exe modifyhd --compact "E:\hostname-dynamic.vdi"
```

<br>

Após isso o arquivo _.vdi_ estápronto pra uso!
