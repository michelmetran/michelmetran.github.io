---
title: "Shutter Counter"
date: 2019-04-18T15:00:00-03:00
last_modified_at: 2021-09-23T16:00:00-03:00
excerpt_separator: "<!--more-->"
categories:
  - Blog
tags:
  - Post Formats
  - readability
  - standard
#categories: [Blog]
#tags: [Post Formats, notice]
#link: https://github.com
#author: Michel Metran

---

Com a finalidade de remunerar criadores de conteúdo, existem plataformas disponíveis na web que auxiiam você a obter financiamiento *online*.

<!--more-->

Inicialmente é necessário instalar o **gphoto2**.

```bash
sudo apt-get update
sudo apt-get install gphoto2
```

Uma vez instalar, é necessário listar as configurações.

```bash
gphoto2 --list-config
```

Provavelmente dê um problema visto que a câmera se conecta diretamente ao sistema operacional.

É necessário, portanto, encerrar os processos que estão usando a câmera.

```bash
killall PTPCamera
```



Além do **killall** eu também fiz o **unmount** da câmera no **Nautilus** (explorador de arquivos do Ubuntu).



![image.png](https://i.imgur.com/Pds6tvK.png)



E pegar apenas uma configuração do aplicativo: o **shuttercounter**.

```bash
gphoto2 --get-config /main/status/shuttercounter
```

O resultado é apresentado abaixo.

```bash
Label: Shutter Counter                                                   
Readonly: 0
Type: TEXT
Current: 17160
END
```



**Referências**

- [Read out Canon EOS 7D shutter count on OS X](https://www.twam.info/software/read-out-canon-eos-7d-shuttercount-on-os-x)

