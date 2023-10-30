---
title: "OpenSSH: Chaves"
date: 2023-05-04T00:00:00-03:00
last_modified_at: 2023-05-04T00:00:00-03:00
excerpt_separator: "<!--more-->"
categories:
  - IT
tags:
  - ssh
---

## Criando Chaves

```powershell
# Cria com tipos definidos
ssh-keygen -t ed25519
ssh-keygen -t rsa

# Cria com Comentários
ssh-keygen -t rsa -C "michelmetran@gmail.com"
ssh-keygen -t ed25519 -C "michelmetran@gmail.com"
```

<br>

Adiciono o git como variável de ambiente

```
%USERPROFILE%\Documents\PortableGit\cmd
```
