---
title: "Remote Desktop Connection: Password"
date: 2023-05-12T14:00:00-03:00
last_modified_at: 2023-05-12T14:00:00-03:00
tags: [vms, remote desktop, WOL]
---

Sempre que acesso uma máquina remota, no Windows, por meio do _Remote Desktop Connection_ eu precisava digitar a senha. Curiosamente o Windows não armazenada a senha, mesmo que na primeira tentativa eu habilita-se o _Remember-me_

**OBS**: Isso ocorre quando estou me conectando em PCs que estão dentro de domínios, ou seja, o login de usuário está na estrutura `{domain}/{username}`.

|                Antes                 |                Depois                |
| :----------------------------------: | :----------------------------------: |
| ![](https://i.imgur.com/mNAUk3Y.png) | ![](https://i.imgur.com/u8DgXKP.png) |

<br>

Estive buscando soluções para evitar digitar a senha a todo instante e descobri que apesar da senha estar armazenada no _Windows Defender Credential Guard_ (também conhecido como _Credencial Manager_, por algum motivo do Windows, não funciona!). **Contudo, há uma maneira de solucionar!**

<br>

---

## Solução

Inicialmente, em um terminal, dê o comando para listar as credencias

```
cmdkey /list:TERMSRV/*
```

<br>

E note que o registro armazenado é do tipo _Domain Password_...

![](https://i.imgur.com/Cjroaxy.png)

<br>

Será necessário excluir esse registro e recria-lo como sendo do tipo _Generic Password_. Para excluir o registro basta dar o comando abaixo:

```
cmdkey /delete:TERMSRV/{hostname}
```

<br>

E recriar o registro no _Credencial Manager_

```powershell
# Recriar
cmdkey /generic:TERMSRV/{hostname} /user:{domain}/{username} /pass:{senha}

# Conferir
cmdkey /list:TERMSRV/*
```

<br>

Agora é possível notar que a senha está armazenada do tipo _Generic_ e o ao tentar se conectar, **o _Remote Desktop Connection_ não mais solicitará senha! Resolvido!**

![](https://i.imgur.com/Pg9mIGJ.png)

<br>

---

## Referências

- [Microsoft: **Como usar a Área de Trabalho Remota**](https://support.microsoft.com/pt-br/windows/como-usar-a-%C3%A1rea-de-trabalho-remota-5fe128d5-8fb1-7a23-3b8a-41e636865e8c)
- [Learn: **Windows 11 22H2 - Can't use saved credential**](https://learn.microsoft.com/en-us/answers/questions/1021785/windows-11-22h2-cant-use-saved-credential#answer-1177710)
- [StackOverflow: **"Windows Defender Credential Guard does not allow using saved credentials" for RDP connections?**](https://superuser.com/questions/1756354/windows-defender-credential-guard-does-not-allow-using-saved-credentials-for-r)
