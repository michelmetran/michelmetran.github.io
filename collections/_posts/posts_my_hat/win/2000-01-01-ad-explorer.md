---
title: 'Active Directory'
date: 2019-01-01T00:00:00-03:00
last_modified_at: 2022-06-28T00:00:00-03:00
excerpt_separator: '<!--more-->'

categories:
  - IT
  - Hacks
tags:
  - firma

---

[Responder Kali](https://www.google.com/search?q=Responder%20kali&client=firefox-b-d&sxsrf=ALiCzsZRQyvuUJr87qFjZBpm0N7bRosarQ%3A1660313556439&ei=1F_2YuKsGoSU5OUP09GMwAU&ved=0ahUKEwji5vz9vcH5AhUECrkGHdMoA1gQ4dUDCA0&uact=5&oq=Responder%20kali&gs_lcp=Cgdnd3Mtd2l6EAMyBQgAEIAEMgUIABDLATIFCAAQywEyBQgAEMsBMgUIABDLATIFCAAQywEyBQgAEMsBMgYIABAeEBYyBggAEB4QFjIGCAAQHhAWOgcIABBHELADOgcIABCwAxBDOgoIABDkAhCwAxgBOgwILhDIAxCwAxBDGAI6CAgAELEDEIMBOggIABCABBCxAzoHCAAQChDLAToICAAQHhAPEBZKBAhBGABKBAhGGAFQR1jlEGCpEmgBcAF4AIABtAGIAeEFkgEDMC41mAEAoAEByAETwAEB2gEGCAEQARgJ2gEGCAIQARgI&sclient=gws-wiz&authuser=0)

mddprov

Comando para adicionar a possibilidade do PowerShell ver coisas do AD

```powershell
Get-WindowsCapability -Online | Where-Object {$\_.Name -like "_ActiveDirectory.DS-LDS_"} | Add-WindowsCapability -Online
```

<br>

---

## Referências

- [Finding Pwned Passwords in Active Directory](https://safepass.me/2020/02/25/finding-pwned-passwords-in-active-directory/)
- [Microsoft Learn: **AD Explorer**](https://learn.microsoft.com/en-us/sysinternals/downloads/adexplorer)
- [Convert ASCII Codes to Characters](https://www.browserling.com/tools/ascii-to-text)
- [Extract Clear Text Passwords from Active Directory](https://www.youtube.com/watch?v=qnTHtTCe5ck)
- [How to Crack an Active Directory Password in 5 Minutes or Less](https://www.semperis.com/blog/easy-hacking-active-directory-password/)
