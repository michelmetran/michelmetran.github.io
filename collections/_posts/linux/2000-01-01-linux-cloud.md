---
title: "Linux: Cloud"
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

### DropBox

Baixa o pacote

```bash
# Atualiza
sudo apt update

# Pega
wget -O ~/Downloads/dropbox.deb "https://www.dropbox.com/download?dl=packages/ubuntu/dropbox_2020.03.04_amd64.deb"

# Instala
sudo apt install ~/Downloads/dropbox.deb
sudo apt install python3-gpg
```

<br>

**Referência**

https://linuxhint.com/install_dropbox_debian_10/

<br>

---

### Google Drive

Google Drive Ocaml Fuse

```bash
# Adiciona Repositório
sudo add-apt-repository ppa:alessandro-strada/ppa

# Atualiza e Instala
sudo apt update && sudo apt install google-drive-ocamlfuse

# Pega Autorização
google-drive-ocamlfuse

# Cria Diretório
mkdir ~/Cloud/"GDrive"
mkdir ~/Cloud/"GDrive Alumni"
mkdir ~/Cloud/"GDrive USP"

# Montar
google-drive-ocamlfuse -label Personal ~/Cloud/"GDrive"/
google-drive-ocamlfuse -label USP ~/Cloud/"GDrive USP"/
google-drive-ocamlfuse -label Alumni ~/Cloud/"GDrive Alumni"/

# Desmontar
fusermount -u ~/Cloud/"GDrive USP"/

# Configurações
sudo gedit ~/.gdfuse/default/config
desktop_entry_as_html=true  # Os arquivos nativos do Google Drive abrirão
```

<br>

**Referência**

- https://www.linuxbabe.com/cloud-storage/install-google-drive-ocamlfuse-ubuntu-linux-mint
- https://github.com/astrada/google-drive-ocamlfuse/blob/beta/doc/Automounting.md
- https://www.linuxuprising.com/2019/06/how-to-speed-up-google-drive-ocamlfuse.html
- https://ubuntu-mate.community/t/automatically-mount-google-drive-with-google-drive-ocamlfuse-at-startup/13143/7

Automont

```bash
# Editar
sudo gedit /etc/systemd/system/google-drive-ocamlfuse-personal.service

[Unit]
Description=FUSE filesystem over Google Drive
After=network.target

[Service]
User=michel
Group=michel
ExecStart=google-drive-ocamlfuse -label Personal ~/Cloud/"GDrive"/
ExecStop=fusermount -u ~/Cloud/"GDrive"/
Restart=always
Type=forking

[Install]
WantedBy=multi-user.target
```

```bash
sudo systemctl start google-drive-ocamlfuse-personal.service
sudo systemctl stop google-drive-ocamlfuse-personal.service
sudo systemctl enable google-drive-ocamlfuse-personal.service
```

<br>

---

### OneDrive

- https://github.com/jstaf/onedriver
- https://github.com/abraunegg/onedrive/blob/master/docs/INSTALL.md
- https://www.edivaldobrito.com.br/como-instalar-o-cliente-onedrive-onedriver-no-linux/

```bash
echo 'deb http://download.opensuse.org/repositories/home:/jstaf/xUbuntu_20.04/ /' | sudo tee /etc/apt/sources.list.d/home:jstaf.list

curl -fsSL https://download.opensuse.org/repositories/home:jstaf/xUbuntu_20.04/Release.key | gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/home_jstaf.gpg > /dev/null

sudo apt update && sudo apt install onedriver
```
