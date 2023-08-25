---
title: 'Samba'
date: 2023-05-04T00:00:00-03:00
last_modified_at: 2023-05-04T00:00:00-03:00
excerpt_separator: '<!--more-->'
categories:
  - IT

tags:
  - python
  - pycharm
  - jupyter
  - package
  - pandas

---

O Samba é um conjunto de ferramentas para lidar com o protocolo SMB (também conhecido como “CIFS”) no Linux. Esse protocolo é usado pelo Windows para compartilhamento de rede e impressoras compartilhadas.

Samba também pode atuar como um controlador de domínio Windows. Esta é uma excelente ferramenta para garantir a perfeita integração de servidores Linux com as máquinas desktop de escritório ainda executando Windows.

- https://www.samba.org
- https://wiki.samba.org

<br>

Inicialmente faz-se necessário instalar o Samba

```bash
sudo apt-get update
sudo apt-get install samba
sudo apt-get install samba nautilus-share
```

<br>

Adicionar um _password_...

```bash
sudo smbpasswd -a $USER
sudo gpasswd -a $USER sambashare
sudo usermod -a -G sambashare $USER
```

<br>

Consultar os _status_ do serviço...

```bash
sudo service smbd status
sudo service smbd start
sudo service smbd stop
sudo service smbd restart
```

<br>

---

### Configurações

```bash
sudo gedit /etc/samba/smb.conf
```

<br>

---

### Acessos

#### Linux (server) > Windows (client)

Uma vez comprtilhada uma pasta no Ubuntu (ou PopOS), via Nautilus é possível acessar a pasta no Windows, por meio do IP:

```
\\10.0.2.15
```

<br>

É também possível acessar pelo _hostname_. Para isso e possível usar o comando `hostnamectl` para ver o _hostname_ do Linux e editar usando `sudo gedit /etc/host`.

```
\\pop-os
```

<br>

#### Windows (server) > Linux (client)

Para acessar os arquivos do Windows, bastar usar o Nautilus (equivalente do Windows Explorer) e digitar

```
smb://asus-i7
smb://asus-i5/Arquivos
smb://P116630/Downloads
```

<br>

É possível usar os comandos abaixo para acessar os arquivos pelo Terminal, usando o [smbclient](https://access.redhat.com/documentation/pt-br/red_hat_enterprise_linux/8/html/deploying_different_types_of_servers/proc_using-smbclient-in-scripting-mode_assembly_using-the-smbclient-utility-to-access-an-smb-share)

```
smbclient //P116630/Downloads -U michel -W workgroup
smbclient //192.168.1.104/Michel -U michel -W workgroup
```

---

<br>

### Referências

- https://askubuntu.com/questions/923306/connecting-to-a-windows-network-with-ubuntu-16-04-lts
