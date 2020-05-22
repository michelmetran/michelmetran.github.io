---
layout: post
title: VirtualBox
subtitle: Exercícios e Referências
tags: [VirtualBox, host, shared folders]
image: /img/posts/gspread_icon.png
bigimg: /img/posts/gspread_big.png
comments: true
---

Por algum tempo não conseguia compartilhar, de maneira que me atendesse, as pastas e unidades do Windows 10 (na ocasião, meu *host*), com o Ubuntu 19.10 (na ocasião, era o meu *host*).

O problema tratava-se da impossibilidade de alterar os arquivos pelo host. Até conseguia criar arquivos e pastas, mas sem edita-los posteriormente.

{: .box-warning}
**Aviso:** Esse _post_ tem a finalidade de mostrar os comandos básicos e me deixar com uma "cola" rápida para meu uso cotidiano. Todas os códigos são exemplificativos e podem/devem ser alterados, indicando o nome dos arquivos e diretórios corretamente.

<br>



# *Shared Folders*

Logo, segui <a title="Link do GSpread" href="https://serverfault.com/questions/394197/mount-shared-folder-vbox-as-another-user" target="_blank">**_estes procedimentos_**</a>, que utilizam o mount para contornar a limitação do VirtualBox.

```
sudo mount -t vboxsf SHARE_NAME -o rw,dmode=777,gid=GROUP_ID,uid=USER_ID /path/on/guest
```



Para meu caso concreto, os códigos que montam as minhas unidades de interesse são:

```
sudo mount -t vboxsf Arquivos -o rw,dmode=777,gid=1000,uid=1000 /home/michel/Arquivos
sudo mount -t vboxsf Geodata -o rw,dmode=777,gid=1000,uid=1000 /home/michel/Geodata
```



Ainda é possível desmonta-las usando:

```
sudo umount /home/michel/Arquivos
sudo umount /home/michel/Geodata
```

