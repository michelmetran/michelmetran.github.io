---
title: 'Red Hat'
date: 2023-04-05T15:00:00-03:00
last_modified_at: 2023-04-05T15:00:00-03:00
excerpt_separator: '<!--more-->'
tags: [python, pycharm, jupyter, package, pandas]
---

Nessa postagem https://access.redhat.com/discussions/5585571
descobri, na fala de *Nate Lager*, que existe um programa de desenvolvedor, para testes...

Ao acessar, vi que já tenho e, na realidade, está quase expirando (expira em 27.04.2023).

Vi o vídeo que mostra como renovar. Quer dizer, não há renovação, há reinscrição!!
https://www.youtube.com/watch?v=uV5Aj4VK2A4

<br>

---

## Linux

- Versão mais utilizada: Red Hat 8
- Versão Atual: 9.1
- Java com TomCat, estável...

<br>

---

## RHEL

https://developers.redhat.com/rhel8/install-rhel8-vbox#virtualbox_guest_additions

<br>

---

## MP

1. Podman instalado!
2. Instalei tb o _insights_

<br>

---

## _Insights_

O Red Hat® _Insights_ analisa plataformas e aplicações continuamente para prever riscos, recomendar ações e rastrear custos, permitindo o gerenciamento de ambientes de nuvem híbrida de maneira mais eficiente.

> https://www.redhat.com/pt-br/technologies/management/insights

<br>

Para registrar segui os passos indicados em nessa [postagem](https://console.redhat.com/insights/registration#SIDs=&tags=).

```bash
# Loga como root
sudo su -

# Registra
insights-client --register
```

<br>

---

## SSH

Precisava de acesso ao _ssh_ do RHEL fora na instância, ou seja, acesso público.

Segui uns tutoriais na postagem [RHEL 8 / CentOS 8 enable ssh service](https://linuxconfig.org/redhat-8-enable-ssh-service) que também direcionava para o vídeo [How to install SSH server on CentOS 8 / RHEL 8 Linux](https://www.youtube.com/watch?v=DHBU4P0GOIQ).

Grosso modo, criei um par de chaves públicas EDSA e adicione

<br>

---

## Referências

- [Customer Portal](https://access.redhat.com/)
- [Red Hat](https://www.redhat.com/en)
- [Documentação](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/9)
- [Developers](https://developers.redhat.com/)

<br>

---

## Comandos

Comandas para atualiza aplicações.

```
sudo dnf update
sudo dnf upgrade
```

<br>

----

## Customize

Adicionar botões de minimizar, maxomizar e close nas janelas [How to Enable Minimize and Maximize Buttons on CentOS/RHEL 8](https://bonguides.com/how-to-enable-minimize-and-maximize-buttons-on-centos-rhel-8/)

```
gsettings set org.gnome.desktop.wm.preferences button-layout ":minimize,maximize,close"
```
