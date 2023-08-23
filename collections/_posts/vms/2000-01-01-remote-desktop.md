---
title: 'Remote Desktop'
excerpt_separator: '<!--more-->'
tags: [python, pycharm, jupyter, package, pandas]
---

### _Ubuntu_ para _Windows_

Inicialmente é necessário habilitar a opção de _Área de Trabalho Remota_ no Windows 10. Importante ressaltar que essa opção está disponível apenas nas versões do Windows 10 Pro. A versão Windows Home não possibilita habilitar essa opção, sendo necessário fazer o _upgrade_ do Windows.

Usei o aplicativo [Remmina](https://remmina.org/) para se conectar. Observei que o Remmina não aceitou o _hostname_.

<br>

### _Windows_ para _Ubuntu_

Inicialmente é necessário que o Linux tenha o **xrdp** instalado.

```bash
sudo apt-get install xrdp
```

<br>

Uma vez instalado, basta conectar-se ao Ubuntu, através do Windows, usando o comando `mstsc`, utilizando o **Executar**.

<br>

### XfreeRDP

Instalar

```bash
sudo apt-get install freerdp2-x11
```

<br>

Usar

```bash
xfreerdp /multimon /u:<username> /v:<remote windows machine name>
xfreerdp /multimon /u:michel /v:192.168.0.106 -wallpaper
xfreerdp /multimon /u:michel /v:asus-i5-mp
xfreerdp /multimon /gu:workgroup\michel /v:asus-i5-mp
xfreerdp /u:pecege /v:192.168.0.107

# Compartilhar Tela
xfreerdp /multimon /u:michel /v:asus-i5 -wallpaper
xfreerdp /multimon /u:michel /v:asus-i5 -wallpaper /audio-mode:1
xfreerdp /multimon /u:michel /v:asus-i5 /audio-mode:1
xfreerdp /u:michel /v:asus-i5 /audio-mode:1
```

<br>

Tecla para alternar entre Remote e Host

```
CTRL + ALT + Enter
```

### KVM

```bash
xrandr --newmode "1920x1080"  173.00  1920 2048 2248 2576  1080 1083 1088 1120 -hsync +vsync
xrandr --addmode VGA-1 1920x1080
xrandr --output VGA-1 --mode 1920x1080
```

https://qastack.com.br/superuser/758463/getting-1920x1080-resolution-or-169-aspect-ratio-on-ubuntu-or-linux-mint

<br>

**Referências**

- [Linux : Remote desktop multiple monitor support](https://medium.com/analytics-vidhya/linux-remote-desktop-multiple-monitor-support-840974e9eb73)
- [Conexão de área de trabalho remota do Windows no Linux com clientes RDP](https://kamarada.github.io/pt/2020/04/11/conexao-de-area-de-trabalho-remota-do-windows-no-linux-com-clientes-rdp/#.XzaSuxlv_AI)
- [**YouTube**: Como Mudar do Windows Home para o Pro, sem Precisar FORMATAR o PC!](https://www.youtube.com/watch?v=uAW83G0Vxis)
- [Como conectar à um servidor Linux via Remote Desktop (Windows)](https://medium.com/@fabianosarmento/como-conectar-%C3%A0-um-servidor-linux-via-remote-desktop-windows-aa5ce95405e8)
- [Como se conectar a partir do Windows no Ubuntu usando o Remote Desktop](https://www.vivaolinux.com.br/dica/Como-se-conectar-a-partir-do-Windows-no-Ubuntu-usando-o-Remote-Desktop)

https://learn.microsoft.com/en-us/windows/win32/termserv/terminal-services-shortcut-keys

<br>

---
