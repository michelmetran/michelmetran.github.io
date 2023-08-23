---
title: 'Virtual Box: Command Line'
excerpt_separator: '<!--more-->'
tags: [python, pycharm, jupyter, package, pandas]
---

## Convert Fixed into Dynamic

Criei minhas VMs usando o disco com tamanho fixo, visto que o acesso ao HD virtual fica mais ágil. Contudo, decidi converter em espaço dinâmico, visto que eu teria que transportar essas VMs. Li no artigo [How to Convert Between Fixed and Dynamic Disks in VirtualBox](https://www.howtogeek.com/312456/how-to-convert-between-fixed-and-dynamic-disks-in-virtualbox/) instruções para fazer, conforme segue

```powershell
# No Windows, vai até a pasta de instalação
cd C:\Program Files\Oracle\VirtualBox

# Compacta o Disco da VM do Win
VBoxManage.exe clonemedium disk "C:\Users\michelsilva\VMs\Ubuntu\Ubuntu.vdi" "C:\Users\michelsilva\VMs\Ubuntu\Ubuntu-dynamic2.vdi" -variant Standard

# Compacta o Disco da VM do Ubuntu
VBoxManage.exe clonemedium disk "C:\Users\michelsilva\VMs\Win\Win.vdi" "C:\Users\michelsilva\VMs\Win\Win-dynamic.vdi" -variant Standard
```

<br>

Agora é necessário compactar. Inicialmente faz-se isso:

```powershell
# Compact
VBoxManage.exe modifyhd --compact "C:\Users\michelsilva\VMs\Ubuntu\Ubuntu-dynamic2.vdi"
VBoxManage.exe modifyhd --compact "C:\Users\michelsilva\VMs\Win\Win-dynamic.vdi"
```

<br>

Mas ainda assim o ideal é compactar o Sistema Operacional do host. No Widows, trata-se do desframentador. No Linux é foda!, vários eros.

```bash
systemctl stop systemd-journald.socket
systemctl stop systemd-journald.service
sudo swapoff -a
mount -n -o remount,ro -t ext2 /dev/sda5 /
zerofree /dev/sda5 -v
```

<br>

É possível alterar o tamanho do disco tb.

```powershell
.\VBoxManage.exe modifyhd "E:\VMs\Ubu\Ubuntu\Ubuntu.vdi" --resize 40960
```

<br>

---

## CloneVDI

Após os comandos, notei que a compactação não foi bem sucesdida.
Com o aplicativo [CloneVDI tool](https://forums.virtualbox.org/viewtopic.php?t=22422) o processo de compactação foi facilitado.

<br>

---

## Keyserver behide proxy

ddddd

```bash
sudo apt-key adv --keyserver keyserver.ubuntu.com --keyserver-options http-proxy=http://127.0.0.1:3128 --recv-keys E298A3A825C0D65DFD57CBB651716619E084DAB9
```

<br>

- https://unix.stackexchange.com/questions/361213/unable-to-add-gpg-key-with-apt-key-behind-a-proxy

<br>

---

## Atalhos

Em uma tentativa de usar o venv na VM Ubuntu, deu erro: [virtualenv returns error 'Operation not Permitted'](https://stackoverflow.com/questions/28651173/virtualenv-returns-error-operation-not-permitted). Estudando, encontrou soluões

> Error: [Errno 1] Operation not permitted: 'lib' -> '/home/michel/Codes/open_traquitanas/build_classic/venv/lib64'

```bash
python -m venv ./venv
```

```powershell
# No Windows, vai até a pasta de instalação
cd C:\Program Files\Oracle\VirtualBox

# Vê configurações
VBoxManage.exe getextradata "Linux Ubuntu" enumerate

# Habilta symlinks
VBoxManage.exe setextradata "Linux Ubuntu" VBoxInternal2/SharedFoldersEnableSymlinksCreate/"my_codes" 1
```

<br>

Não deu certo.

<br>

---

# Problemas e Resoluções

## USB

Espetado no PC e o Virtual Box não encontrava o usb. Dava a mensagem de erro `<no devices available>` . [Descobri](https://superuser.com/questions/956622/no-usb-devices-available-in-virtualbox) que adicionando o usuário no grupo, aparece! É necessário reiniciar ou deslogar/logar!

Nesse artigo tem mais informações: [How to set up USB for Virtualbox? - Ask Ubuntu](https://askubuntu.com/questions/25596/how-to-set-up-usb-for-virtualbox?noredirect=1&lq=1)

```bash
sudo adduser $USER vboxusers
sudo usermod -aG vboxusers {username}
sudo usermod -aG vboxusers michel
sudo usermod -G vboxsf -a michel
```

<br>

---

## Core Isolation

Na versão 7.0.6 e Win 11 passei a receber o erro:

```
Failed to load R0 module C:\Program Files\Oracle\VirtualBox/VMMR0.r0: SUP_IOCTL_LDR_OPEN failed (VERR_LDR_GENERAL_FAILURE).
Failed to load VMMR0.r0 (VERR_LDR_GENERAL_FAILURE).
Código de Resultado:
E_FAIL (0X80004005)
Componente:
ConsoleWrap
Interface:
IConsole {6ac83d89-6ee7-4e33-8ae6-b257b2e81be8}
```

<br>

Li em [publicações](https://www.youtube.com/watch?v=kIXPsAM1iLI) que seria necessário desabilittar o Hyper-V. **Não funcionou pra mim!**, visto que sequer estava habilitado!

```
bcdedit /set hypervisorlaunchtype off
```

<br>

Na [_thread_](https://forums.virtualbox.org/viewtopic.php?t=104574) descobri o erro. É necessário desabilitar o protocolo de segurança do Windows _Memory integrity_:

> _go to Start > Settings > Update & security > Windows Security > Open Windows Security, select Device security, then Core isolation details. Under Core Isolation, check if Memory integrity is turned on or off._

<br>

Testei e deu certo!! Contudo, não gostaria de adotar essa solução pois, com essa função desabilitada, outro aplicativo que eu uso (_Check Point Endpoint Security_) deixa de funcionar.

Para solucionar a recomendação é substituir a versão do VirtualBox. A versão 6.1.32 parece que não ocorre esse _bug_! É possível baixar as versões antigas [aqui](https://www.virtualbox.org/wiki/Download_Old_Builds).

Para modar a versão eu limpava a pasta `C:\Users\{username}\.VirtualBox`.

<br>

Tentei fazer isso e recebi a seguinte mensagem de erro:

```
Error in D:\VMs\RHEL\RHEL.vbox (line 64) -- Invalid value 'WAS' in AudioAdapter/@driver attribute.
F:\tinderbox\win-6.1\src\VBox\Main\src-server\MachineImpl.cpp[499] (long __cdecl Machine::initFromSettings(class VirtualBox *,const class com::Utf8Str &,const class com::Guid *)).
```
