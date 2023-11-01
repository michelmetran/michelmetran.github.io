---
title: "Kali: <i>monitor mode</i>"
date: 2019-01-01T00:00:00-03:00
last_modified_at: 2022-06-28T00:00:00-03:00
excerpt_separator: "<!--more-->"
categories:
  - IT
  - Hacks

tags:
  - firma
---

O _monitor mode_ é uma funcionalidade que permite que um adaptador Wi-Fi capture e analise pacotes de rede sem fio em tempo real. Isso é útil para fins de segurança, como testes de penetração e análise de tráfego de rede. Para colocar um adaptador Wi-Fi no modo monitor, você pode usar o _airmon-ng_, que é uma ferramenta disponível no Kali Linux.

<br>

---

## Hardware

Existem diversos modelos de adaptadores wi-fi no mercado. Existem também alguns que são recomendados para o uso no Kali Linux. Os dois que tenho, para fins de teste, são listados abaixo.

### OIW 2422USG

O adaptador [OIW 2422USG](https://www.powernetwork.com.br/produto/adaptador-usb-wireless-oiw-2422usg) tem com _chipset_ **Ralink RT2070**.

Vendo o [vídeo](https://www.youtube.com/watch?v=K1ETBeRQBs4), é indicado obter o _Vendor ID_ e _Product ID_. Isso é ensinado no Windows, porém no Ubuntu vi [outra informação](https://tuxthink.blogspot.com/2011/09/finding-vendor-id-and-product-id-of-usb.html?m=1) que explica que com o comando abaixo:

```bash
# Command
usb-devices

# Output
T:  Bus=03 Lev=01 Prnt=01 Port=00 Cnt=01 Dev#= 14 Spd=480 MxCh= 0
D:  Ver= 2.00 Cls=00(>ifc ) Sub=00 Prot=00 MxPS=64 #Cfgs=  1
P:  Vendor=148f ProdID=2070 Rev=01.01
S:  Manufacturer=Ralink
S:  Product=802.11 g WLAN
S:  SerialNumber=1.0
C:  #Ifs= 1 Cfg#= 1 Atr=80 MxPwr=450mA
I:  If#=0x0 Alt= 0 #EPs= 7 Cls=ff(vend.) Sub=ff Prot=ff Driver=rt2800usb
```

<br>

---

### D-Link DWA-182

O adaptador [D-Link DWA-182](https://www.dlink.com.br/produto/adaptador-wireless-usb-ac1300-dwa-182/) usa _chipset_ Realtek RTL8812AU.

Instalei os _drivers_ com auxílio do repositório [morrownr/8812au-20210629](https://github.com/morrownr/8812au-20210629), disponível no GitHub, que dá o passo a passo para instalação dos _drivers_.

```shell
# Vê configurações
cat /etc/modprobe.d/8812au.conf

# Edita configurações
sudo nano /etc/modprobe.d/8812au.conf
```

<br>

---

## Mudando para *Monitor Mode*

Usando o *airmon-ng*

```bash
# Ver interfaces
iwconfig
ip addr

# Desabilitarkali
sudo ifconfig wlan0 down

# Kill all process
sudo airmon-ng check kill

# Habilitando o Monitor Mode
sudo airmon-ng start wlan0

# Check (mode:Monitor)
iwconfig
```

<br>

Usando o *iwconfig*

```bash
# Habilitando o Monitor Mode
sudo iwconfig wlan0 mode monitor

# Habilita
sudo ifconfig wlan0 up
```
