---
title: "WireShark"
date: 2019-01-01T00:00:00-03:00
last_modified_at: 2022-06-28T00:00:00-03:00
excerpt_separator: "<!--more-->"
categories:
  - IT
  - Hacks
tags:
  - firma
---

O [Wireshark](https://www.wireshark.org) é um programa que analisa o tráfego de rede, e o organiza por protocolos. As funcionalidades do Wireshark são parecidas com o tcpdump mas com uma interface gráfica, com mais informação e com a possibilidade da utilização de filtros.

<br>

---

## Instalar

Para instalar basta dar os comandos abaixo conforme explicado [aqui](https://linuxhint.com/install_wireshark_ubuntu/).

```bash
sudo apt-get update
sudo apt-get install wireshark
```

<br>

---

## Erros

Ao final da instalação, é possível definir que usuários possam capturar pacotes. Por equívoco, não habilitei isso.

![](https://i.imgur.com/sVoW8As.png)

<br>

E foi necessário rodar os seguintes comandos para corrigir. [Setting up wireshark for non root user](https://askubuntu.com/questions/246363/setting-up-wireshark-for-non-root-user).

```bash
sudo dpkg-reconfigure wireshark-common
sudo adduser {username} wireshark
sudo adduser michel wireshark
```

<br>

---

## Protocolos

- eapol: autentication protocol
- ssh
- tftp

<br>

---

## Referências

- [Network traffic analysis for IR: TFTP with Wireshark](https://resources.infosecinstitute.com/topic/network-traffic-analysis-for-ir-tftp-with-wireshark/)
- [Spy on Traffic from a Smartphone with Wireshark](https://null-byte.wonderhowto.com/how-to/spy-traffic-from-smartphone-with-wireshark-0198549/)

<br>

**Portais**

- [Wonder How To](https://www.wonderhowto.com/)
