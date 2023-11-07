---
title: "Kali: <i>macchanger</i>"
date: 2019-01-01T00:00:00-03:00
last_modified_at: 2023-11-01T00:00:00-03:00
excerpt_separator: "<!--more-->"
categories:
  - IT
  - Hacks
tags:
  - firma
---

## Change Mac Address

O [*macchanger*](https://github.com/alobbs/macchanger) é uma ferramenta que permite alterar o endereço MAC de um adaptador de rede. Isso pode ser útil para fins de privacidade, segurança ou para contornar restrições de rede. Existem várias ferramentas disponíveis para alterar o endereço MAC, como o [Technitium MAC Address Changer](https://technitium.com/tmac/) e o [GNU MAC Changer]((https://github.com/alobbs/macchanger) ). Ambos são gratuitos e fáceis de usar.

```bash
# Ver Mac Address
ip addr show wlan0mon

# Help
sudo macchanger --help

# first put your wireless card off
sudo ifconfig wlan0mon down

# Random Mac Address
sudo macchanger --random wlan0mon

# Default Mac Address
sudo macchanger --permanent wlan0mon

# Specific Mac Address
sudo macchanger -mac=XXX wlan0mon

# Up
sudo ifconfig wlan0mon up
```
