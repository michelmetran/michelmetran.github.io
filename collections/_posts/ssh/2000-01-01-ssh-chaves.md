---
title: 'OpenSSH: Chaves'
date: 2023-05-04T00:00:00-03:00
last_modified_at: 2023-05-04T00:00:00-03:00

excerpt_separator: '<!--more-->'

categories:
  - IT

tags:
  - ssh
---

## Criando Chaves

```powershell
#
ssh-keygen -t ed25519
ssh-keygen -t rsa

# dddd
ssh-keygen -t rsa -C "michelmetran@gmail.com"
ssh-keygen -t rsa -C "michelsilva@mpsp.mp.br"
ssh-keygen -t ed25519 -C "michelmetran@gmail.com"
```

<br>

Adiciono o git como variável de ambiente

```
%USERPROFILE%\Documents\PortableGit\cmd
```

<br>

Aviso o `git` que é pra usar o `OpenSSH` do Windows e informo ao git sua localização. Essa configuração foi observada aqui [Windows 10 SSH client: password-less access](https://superuser.com/questions/1433917/windows-10-ssh-client-password-less-access)

```powershell
git config --global core.sshCommand C:/Windows/System32/OpenSSH/ssh.exe
```
