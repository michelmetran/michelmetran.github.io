---
title: "JetBrains e o teclado"
date: 2023-05-04T00:00:00-03:00
last_modified_at: 2023-05-04T00:00:00-03:00

categories:
  - IT

tags:
  - python
  - pycharm
  - ide
---

Após algum tempo, vi que o PyCharm, o Rider e todas as IDEs da JetBrain começavam a apresentar _bugs_ estranhos relacionados ao teclado.

Quando o problema ocorria, cheguei ao ponto de formatar o Sistema Operacional visando continuar com o funcionamento adequado.

Em poucas palavras: acentos deixaram de funcionar apenas nas IDEs. No restante do SO funcionavam normalmente.

Analisando o [Cannot-type-dead-keys-in-Linux](https://youtrack.jetbrains.com/issue/IDEA-59679/) passei a testar de tudo, e melhor compreender os pontos.

<br>

---

### IBUS

Após muito ler, parece que o problema é no IBUS...

```bash
# Rodei e
sudo ibus-setup

# Pediu para adicionar no .bashrc
sudo gedit ~/.bashrc

export GTK_IM_MODULE=ibus
export QT_IM_MODULE=ibus
export XMODIFIERS=@im=ibus
```

Pediu para reiniciar

**Resultado**

Não deu.

<br>

---

### IBUS Config

```bash
im-config
```

**Resultado**
Testei vários tipos.
Nada!

<br>

---

### IM-Config

- https://manpages.ubuntu.com/manpages/jammy/man8/im-config.8.html

```bash
# Run
echo $XMODIFIERS

and it returns @im=ibus, it will work. If it returns nothing, then it won't work.
```

Edit: activating ibus for OS keyboard input fixed the problem for me, for now (added ibus-daemon --xim to startup).

```
cat /etc/default/im-config
sudo gedit /etc/default/im-config

set | grep -E 'XMODIFIERS|GTK_IM_MODULE|QT_IM_MODULE'
```

<br>

---

### Locale

```
sudo touch /etc/locale.conf
sudo gedit /etc/locale.conf
```

Bobagem!

<br>

---

### dddd

```
gsettings get org.gnome.settings-daemon.plugins.keyboard
```

```bash
# Deu merda!
sudo ibus-daemon --xim &
```

https://askubuntu.com/questions/389903/ibus-doesnt-seem-to-restart

<br>

---

### VMs

[Eduardo Moraes](https://youtrack.jetbrains.com/issue/IDEA-59679/Cannot-type-dead-keys-in-Linux#focus=Comments-27-5796877.0-0)

```bash
# Inicialmente vi as configurações
echo $GTK_IM_MODULE #ibus
echo $QT_IM_MODULE #ibus
echo $XMODIFIERS #@im=ibus


# Essas configurações ficam aqui
cat /etc/profile.d/pop-im-ibus.sh
sudo gedit /etc/profile.d/pop-im-ibus.sh

# Alterei usando
export GTK_IM_MODULE=""
export QT_IM_MODULE=""
export XMODIFIERS=""


# Quando vejos as configurações está tudo em branco, conforme defini...
set | grep -E 'XMODIFIERS|GTK_IM_MODULE|QT_IM_MODULE'
```

**Resultado**

Não deu.
Voltei configurações originais.

<br>

---

### Ajuste no _.sh_ do Pycharm

https://intellij-support.jetbrains.com/hc/en-us/community/posts/206877355-Accent-Characters-on-Editor

```bash
# Add
export XMODIFIERS=""

# Edit
sudo gedit ~/.local/share/JetBrains/Toolbox/apps/PyCharm-P/ch-0/222.4167.33/bin/pycharm.sh
```

**Resultado**

Não deu.
Voltei configurações originais.

<br>

---

### Atualizando o OpenJDK

```bash
# Vê a versão
java -version

# Adiciona Repositório
sudo add-apt-repository ppa:openjdk-r/ppa

# Atualiza e Instala!
sudo apt-get update
sudo apt-get install openjdk-18-jdk
```

<br>

---

### fcitx

```bash
# Run
sudo apt install fcitx
```

**Resultado**

Zuado.
Removi!

<br>

---

### fcitx5

```bash
# Instalar
sudo apt-get -y install fcitx5
sudo apt-get -y install fcitx5-frontend-gtk2
sudo apt-get -y install fcitx5-frontend-gtk3


# Pediu para adicionar no .bashrc
sudo gedit ~/.bashrc

export GTK_IM_MODULE=fcitx5
export QT_IM_MODULE=fcitx5
export XMODIFIERS=@im=fcitx5
```

**Resultado**

Não deu.

<br>

---

### XCompose

Criando XCompose

```
cat ~/.XCompose
sudo touch ~/.XCompose
sudo gedit ~/.XCompose
sudo rm ~/.XCompose
```
