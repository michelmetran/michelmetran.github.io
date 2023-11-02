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

Uma das coisas que notei enquanto usava o _Remote Desktop Connection_ do Windows é que havia um _delay_ do audio, que impossibilitava escutar coisas a partir do PC remoto.

Por vezes procurava vídeos de YouTube, por vezes procurava música. O _delay_ impossibilitava qualquer coisa!

Para contonar o problema encontrei o _post_ [How to Improve Audio Quality and Remove Delays Over Remote Desktop](https://sysadmin-central.com/2021/08/04/how-to-improve-audio-quality-and-remove-delays-over-remote-desktop/) que dá alguns passos para melhorar o audio em conexões em PCs remotos.

Segue o seguinte passo:

1. Salvei a conexão do _Remote Desktop Connection_ ou "Área de Trabalho Remota") em um arquivo _.rdp_
2. Editei o arquivo usando um editor de texto (_bloco de notas_ serve) , acrescentando a linha `audioqualitymode:i:2`
3. Pronto! Uma vez conectado usando esse arquivo, o audio fica sem _delays_!
