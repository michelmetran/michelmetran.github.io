---
title: 'OpenSSH Server'
date: 2023-05-04T00:00:00-03:00
last_modified_at: 2023-05-04T00:00:00-03:00

excerpt_separator: '<!--more-->'

categories:
  - IT

tags:
  - ssh

---

## Server

<br>

## Conectando no Asus i7

```
ssh michel@192.168.0.112
```

```
ssh michel@192.168.0.106
ssh michelsilva@192.168.0.106
ssh MP\michelsilva@192.168.0.106
ssh -l michelsilva@MP 192.168.0.106
ssh michel@192.168.0.106
ssh michel@172.28.0.7
ssh MP\michelsilva@192.168.0.106
ssh -l michelsilva@MP 192.168.0.106
```

max@server1 – local Windows user
michelsilva@MP@192.168.0.106 – Active Directory user or Microsoft/Azure account (use the UserPrincipalName format)
woshub\max@server1 – NetBIOS name format

- [Key-based Authentication for OpenSSH on Windows](https://www.concurrency.com/blog/may-2019/key-based-authentication-for-openssh-on-windows)
- https://github.com/PowerShell/Win32-OpenSSH/wiki/Security-protection-of-various-files-in-Win32-OpenSSH
- https://github.com/microsoft/vscode-remote-release/issues/4323
- https://github.com/microsoft/vscode-remote-release/issues/5111

<br>

# Conectando no Asus i7

```
ssh michel@192.168.0.112 -p 2222

(get-acl .ssh\config).owner
icacls .ssh\config
icacls .ssh\config /setowner system
icacls .ssh\config /inheritance:r
icacls .ssh\config /grant SYSTEM:`(F`)
icacls .ssh\config /grant BUILTIN\Administradores:`(F`)
icacls .ssh\config /remove otheruser2
icacls .ssh\config /grant Everyone:F /T
```

max@server1 – local Windows user
michelsilva@MP@192.168.0.106 – Active Directory user or Microsoft/Azure account (use the UserPrincipalName format)
woshub\max@server1 – NetBIOS name format

http://makerlab.cs.hku.hk/index.php/en/mapping-network-drive-over-ssh-in-windows

```
net use X: \\sshfs\billziss@mac2018.local
net use X: \\sshfs\michel@asus-i7
net use X: \\sshfs\michel@172.28.0.7
net use X: \\sshfs\michel@172.28.0.7\Documents
net use X: /delete

net use
```
