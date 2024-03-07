---
title: "Remote Desktop Connection: <i>Audio</i>"
date: 2023-10-10T14:34:30-03:00
last_modified_at: 2023-10-10T14:34:30-03:00
share: false
comments: true
classes: wide
toc: false
categories:
  - IT
  - Hacks
tags:
  - vms
  - remote desktop
  - audio
---

## Problema

Uma das coisas que notei enquanto usava o _Remote Desktop Connection_ do Windows é que havia um _delay_ do audio, que impossibilitava escutar coisas a partir do PC remoto.

Por vezes procurava vídeos de YouTube, por vezes procurava música ou, até mesmo, comunicação via Teams. O _delay_ impossibilitava qualquer coisa!

Para contonar o problema encontrei o _post_ [How to Improve Audio Quality and Remove Delays Over Remote Desktop](https://sysadmin-central.com/2021/08/04/how-to-improve-audio-quality-and-remove-delays-over-remote-desktop/) que dá alguns passos para melhorar o audio em conexões em PCs remotos.

Vi que é necessário alteração no _Limit Audio Playback Quality_, que é ajustada nas "Polícias de Grupo" (Win+R + `gpedit.msc`).

<br>

---

## Registro

Toda Polícita de Grupo tem um correspondente no Registro do Windows! Para facilitar essa alteração, decidi criar uma chave que edita o registro do Windows!

Dai surge a questão: [How can I locate Registry key for Group policy settings?](https://serverfault.com/questions/911131/how-can-i-locate-registry-key-for-group-policy-settings). Encontrei a resposta no [Group Policy Settings Reference Guide for Windows 10; New Group Policy settings](https://www.thewindowsclub.com/group-policy-settings-reference-windows), onde há um arquivo Excel com as correspondências.

Inicialmente comecei estudando [How to change group policy via command line?](https://stackoverflow.com/questions/39834069/how-to-change-group-policy-via-command-line)

Pelo [Group Policy Administrative Templates Catalog](https://admx.help/?Category=Windows_10_2016&Policy=Microsoft.Policies.TerminalServer::TS_CLIENT_AUDIO_QUALITY), consegui encontrar a chave no registro que altera as configurações dessa política de grupo.

Uma vez com as correspondências, encontrei o registro e testei as alterações. Atestando que trata-se do registro correspondente, exportei a chave e é possível fazer _download_ abaixo.

Uma vez que **roda essa modificação de registro no PC remoto**, ele sempre disponibilizará o audio remoto em alta qualidade!

<br>

---

## Passo a Passo

1. Salvei a conexão do _Remote Desktop Connection_ ou "Área de Trabalho Remota" em um arquivo _.rdp_
2. Editei o arquivo usando um editor de texto (_bloco de notas_ serve) , acrescentando a linha `audioqualitymode:i:2`
3. Pronto! Uma vez conectado usando esse arquivo, o audio fica sem _delays_!

<br>

---
