---
title: "Virtual Box: Mount"
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

## Compartilhando entre _host_ e _guest_

Windows Host | Ubuntu Guest

<br>

---

### Forma 1: padrão

Para compartilhar pastas entre o _host_ e o _guest_ é necessário configurar as pastas a serem compartilhas:
Windows Host | Ubuntu Guest

![image.png](https://i.imgur.com/WYtxNTy.png)

Ainda, no _guest_, é necessário adicionar o usuário definido no grupo do _vsboxsf_ com o seguinte comando, conforme visto na dúvida
[askubuntu: **This location could not be displayed. You do not have the permissions necessary to view the contents of "Shared_Folder"**](https://askubuntu.com/questions/890729/this-location-could-not-be-displayed-you-do-not-have-the-permissions-necessary):

```bash
sudo adduser $USER vboxsf
```

<br>

**_Obs_**: Notei que o problema de se compartilhar arquivos que estão na nuvem da _microsoft_ é que a função _on demand_ deixa de funcionar. O VBOX passa a fazer o _download_ de todos os arquivos.

<br>

---

### Forma 2: melhor

Configura o ponto de pontantagem com um nome diferente... e sem habilitar nada! Deu certo!

```bash
# Cria pasta
mkdir ~/Documents/Codes

# Monta a pasta do VBOX na pasta recem criada
sudo mount -t vboxsf my_codes ~/Documents/Codes

# [Opcional]
sudo mount -t vboxsf -o uid=1000,gid=1000 my_codes ~/Documents/Codes

# Comando que vê o que está montado!
df

# Desmonta
sudo umount my_codes
```

```bash
# Uma vez que, manualmente, deu certo a montagem!
sudo gedit /etc/fstab

# Codes: Add Line
my_codes /home/michel/Documents/Codes vboxsf defaults,uid=1000,gid=1000,umask=0022 0 0

#
sudo gedit /etc/modules

# Add Line
vboxsf
```

- [gist: **How to mount a VirtualBox shared folder when the Guest OS boots**](https://gist.github.com/kentwait/ea49b270f4f7480541409c5ded093ec9)

<br>

---

## Compartilhando entre _host_ e _others devices_

Cenário: uma vez com a virtual machine funcionando, criei um hotspot móvel para conectar outros dispositivos externos a rede que estão inserido.

Uma vez que criei uma rede secundária, posso "montar" unidades dentro da minha _virtual box_.
No caso eu estava no pc do trabalho (_windows_), com um ubuntu em uma _virtual machine_ (guest).

No Ubuntu eu me conectei ao meu notebook (ubuntu), por wi-fi, via hotspot. E queria montar unidades.
Na _virtual machine_ é necessário ter os pacotes necessários para montar unidades em outros sistemas de arquivos (diferentes do _ext4_).

```bash
sudo apt install nfs-common
sudo apt install cifs-utils
```

<br>

Identificar o IP dos dispositivos conectados pelo hotspot móvel.

```bash
arp -a
```

<br>

Montar

```bash
# dddd
sudo mount -t cifs //10.42.0.168/Geodata/Sourcecode /home/michel/Documents/Geodata-i7 -o username=michel
sudo mount -t cifs //10.42.0.168/Geodata /home/michel/Documents/Geodata-i7 -o uid=1000,username=michel,password=*****
```

<br>

Desmontar

```bash
# Mount
sudo umount  -f -l /home/michel/Documents/Geodata-i7
```

<br>

---

## Mount

- [Virtualbox shared folder permissions - Stack Overflow](https://stackoverflow.com/questions/26740113/virtualbox-shared-folder-permissions)

```bash
sudo mount -t vboxsf Test /home/user/Test
sudo mount -t vboxsf Codes Codes

sudo mount -t vboxsf -o rw,uid=1000,gid=1000,dmode=755,fmode=644 [nome no VBOX] [caminho no host]
sudo mount -t vboxsf -o rw,uid=1000,gid=1000,dmode=755,fmode=644 Codes /media/Codes/
sudo mount -t vboxsf -o rw,uid=1000,gid=1000,dmode=755,fmode=644 Dropbox ~/Dropbox/
```

<br>

## Referência

- https://askubuntu.com/questions/525243/why-do-i-get-wrong-fs-type-bad-option-bad-superblock-error
- https://askubuntu.com/questions/506110/listing-devices-connected-in-hotspot-through-terminal
- https://gist.github.com/kentwait/ea49b270f4f7480541409c5ded093ec9
- https://askubuntu.com/questions/161759/how-to-access-a-shared-folder-in-virtualbox
