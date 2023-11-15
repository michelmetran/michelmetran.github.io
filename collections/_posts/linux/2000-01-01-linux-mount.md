---
title: "Linux: <i>mount</i>"
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
---

<br>

## Meus HDs

**HD1**: /dev/sda - 500GB, SSD

- dev/sda1: efi
- dev/sda2: 200GB - SO
- dev/sda3: resto GB - VMs

**HD1**: /dev/sdb - 750GB, SATA

- dev/sdb1: 300GB - Arquivos
- dev/sdb2: resto GB - Geodata

<br>

---

## Montar Partições

Fui seguindo esse tutorial bastante completo e entendi muita coisa do Fstab: [How to Write an fstab File on Linux](https://www.howtogeek.com/444814/how-to-write-an-fstab-file-on-linux/). Abaixo seguem alguns dos comandos. Tantos outros estão somente no link.

https://wiki.archlinux.org/index.php/NTFS-3G

Conferir espaço em Partições

```bash
df -h
```

Descobrir os códigos UUID das partições

```bash
sudo blkid
```

Cria as partições

```bash
sudo mkdir /media/$USER/Arquivos
sudo mkdir /media/$USER/Geodata
sudo mkdir /media/$USER/VMs
```

Monta a partição

```bash
sudo mount /dev/sdb1 /media/$USER/Arquivos
sudo mount /dev/sdb2 /media/$USER/Geodata
sudo mount /dev/sda3 /media/$USER/VMs
```

<br>

Adicionar partições no fstab

```bash
sudo gedit /etc/fstab
```

```bash
# Outras partições do SSD
UUID=e9d6a225-c3f2-4c85-b6a4-e81581bf0a6a	/media/michel/SSD	ext4	rw,auto,user,sync,exec	1	2
UUID=985b0aff-9fef-4df1-b6fa-dd6e1a07843a	/media/michel/VMs	ext4	rw,auto,user,sync,exec	1	2

# Outras partições do HD de 750 do Caddy (rw,auto,user,uid=1000)
#UUID=488A2E2F2C011AEC	/media/michel/Arquivos	ntfs	rw,auto,user,async	1	2
#UUID=000866C43F87D142	/media/michel/Geodata	ntfs	rw,auto,user,async	1	2
UUID=488A2E2F2C011AEC	/media/michel/Arquivos	ntfs-3g	auto,user,exec,uid=1000,gid=1000	1	2
UUID=000866C43F87D142	/media/michel/Geodata	ntfs-3g	auto,user,exec,uid=1000,gid=1000	1	2
```

Ler um arquivo

```bash
cat /etc/fstab
```

Desmonta a partição

```bash
sudo umount /dev/sda1
sudo umount /dev/sdb1
sudo umount /dev/sdb2
```

Dá permissões

```bash
sudo chown [user]:[group] /media/VMs
sudo chown -R michel:michel /media/michel/VMs
sudo chown -R michel:michel /media/michel/Arquivos
sudo chown -R michel:michel /media/michel/Geodata
```

<br>

---

### NTFS Read Only

- [StackOVerflow: Why does my NTFS partition mount as read only?](https://askubuntu.com/questions/70281/why-does-my-ntfs-partition-mount-as-read-only)

```bash
sudo apt-get remove ntfsprogs
sudo apt-get install ntfs-3g
```

<br>

---

### SWAP

- https://linuxhint.com/change_swap_size_ubuntu/
- https://www.cloudbooklet.com/how-to-add-swap-space-in-ubuntu-20-04-google-cloud/

```bash
# ddd
sudo swapon -s

#
dd if=/dev/zero of=/swapfile bs=1M count=16384

#
sudo mkswap /swapfile

sudo swapon /swapfile

# ddd
sudo swapon -s

# Desabilitando
sudo swapoff -a
```

<br>

---

### Montar Partição por Hotspot

```bash
# Install
sudo apt install net-tools

# This command is used to display the ARP table for a particular IP address. It also shows all the entries of the ARP cache or table
arp -a


# Mount
sudo mount -t cifs //10.42.0.168/Codes /home/michel/Codes -o uid=1000,username=michel,password=******
```
