---
title: 'JetBrains e o inotify'
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

---

Usando o IDE PyCharm no Ubuntu, passei a receber uma mensagem do _inotify_ e busquei corrigir o problema. Encontrei a seguinte solução: [How to fix these warnings "External file changes sync may be slow" and "The current inotify(7) watch limit is too low" in IntelliJ Project in Ubuntu](https://stackoverflow.com/questions/67927480/how-to-fix-these-warnings-external-file-changes-sync-may-be-slow-and-the-curr).

```bash
# Cria arquivo
sudo touch /etc/sysctl.d/60-jetbrains.conf

# Edita arquivo
sudo gedit /etc/sysctl.d/60-jetbrains.conf
```

<br>

Adiciona o seguinte conteúdo.

```bash
# Set inotify watch limit high enough for IntelliJ IDEA (PhpStorm, PyCharm, RubyMine, WebStorm).
# Create this file as /etc/sysctl.d/60-jetbrains.conf (Debian, Ubuntu), and
# run `sudo service procps start` or reboot.
# Source: https://confluence.jetbrains.com/display/IDEADEV/Inotify+Watches+Limit
#
# More information resources:
# -$ man inotify # manpage
# -$ man sysctl.conf # manpage
# -$ cat /proc/sys/fs/inotify/max_user_watches # print current value in use

fs.inotify.max_user_watches = 524288
```

<br>

E depois restarta o _system_.

```bash
# Restart
sudo sysctl -p --system
```

<br>

---

### Problem: Inotify (velho!)

Para ajustar a mensagem constantemente recebido, referente ao tempo adotado pelo **inotify**, contrei uma [referência](https://youtrack.jetbrains.com/articles/IDEA-A-2/Inotify-Watches-Limit) que explica como resolver. VIsando automaticar a questão, basta rodar o código abaixo na linha de comando e reiniciar o PyyCharm. _Done!_

```bash
echo "# Inotify on PyCharm" | sudo tee -a /etc/sysctl.d/idea.conf && \
echo "# https://youtrack.jetbrains.com/articles/IDEA-A-2/Inotify-Watches-Limit" | sudo tee -a /etc/sysctl.d/idea.conf && \
echo "" | sudo tee -a /etc/sysctl.d/idea.conf && \
echo "fs.inotify.max_user_watches = 524288" | sudo tee -a /etc/sysctl.d/idea.conf && \
sudo sysctl -p --system
```

<br>

Problema similar ocorre no VsCode

- https://code.visualstudio.com/docs/setup/linux#_visual-studio-code-is-unable-to-watch-for-file-changes-in-this-large-workspace-error-enospc
