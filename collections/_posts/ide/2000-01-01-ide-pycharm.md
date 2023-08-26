---
title: "IDE: PyCharm"
date: 2023-05-04T00:00:00-03:00
last_modified_at: 2023-05-04T00:00:00-03:00
categories:
  - IT
tags:
  - linux
  - git
  - github
  - gitpages
  - python
  - pycharm
  - anaconda
  - miniconda
---

O [**PyCharm**](https://www.jetbrains.com/pycharm/) é um ambiente de desenvolvimento integrado (ou IDE, do inglês '_Integrated Development Environment_') usado em programação de computadores, especificamente para a linguagem [**Python**](https://www.python.org/).

<br>

---

### Instalando o _PyCharm Community_ no Ubuntu

Executei os procedimentos detalhados em aqui [How to Install PyCharm on Ubuntu 18.04](https://linuxize.com/post/how-to-install-pycharm-on-ubuntu-18-04/).

Simplificando ao máximo, basta aplicar o comando abaixo no terminal.

```bash
sudo snap install pycharm-community --classic
```

<br>

---

### Instalando o _PyCharm Professional_ no Ubuntu

```bash
sudo snap install pycharm-professional --classic
```

<br>

---

### JetBrains ToolBox

```bash
# Faz Download
wget -O ~/Downloads/jetbrains.tar.gz "https://download.jetbrains.com/toolbox/jetbrains-toolbox-1.22.10774.tar.gz"

# Descompacta
cd ~/Downloads
tar -zxvf jetbrains.tar.gz

# Instala
cd jetbrains-toolbox*
./jetbrains-toolbox
```

- [YouTube: Download and install jetbrains toolbox in ubuntu 22.04/ 20.04LTS | install intellij, webstrom](https://www.youtube.com/watch?v=gZ_XtkcPSHY)

<br>

---

### IDE IntelliJ IDEA

instala via snap

```bash
# Para Instalar
sudo snap install intellij-idea-community --classic

# Para Atualizar
sudo snap refresh intellij-idea-community
```

<br>

---

## Referência

- [Como instalar a incrível IDE Java IntelliJ IDEA no Linux](https://www.edivaldobrito.com.br/ide-intellij-idea-no-ubuntu-debian/)
