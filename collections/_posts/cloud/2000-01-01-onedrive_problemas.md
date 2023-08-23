---
title: 'OneDrive'
date: 2023-02-23T15:34:30-04:00
last_modified_at: 2023-02-23T15:34:30-04:00
excerpt_separator: '<!--more-->'
categories: [apps, trampo]
---

Error 80071129 OneDrive

https://eazybackup.com/knowledge-base/onedrive-error-the-tag-present-in-the-reparse-point-buffer-is-invalid/

#Tentar
https://answers.microsoft.com/pt-br/windows/forum/all/erro-0x80071129-imposs%C3%ADvel-de-excluir-pasta/4e2ba2c8-80d9-4112-a32c-5f8eb80fca0d


Ôrra! Dê boot por uma mídia de instalação e recuperação > solucionar problemas > prompt de comando

DISKPART

LIS VOL (verifique a letra da partição do Windows, por exemplo D)

EXIT

RD "D:\caminho\nome da pasta" /S /Q


CHKDSK WRITE protection

DISKPART FAILED tyo CLEAR DISK ATRBITES

https://www.itexperience.net/fix-onedrive-the-tag-present-in-the-reparse-point-buffer-is-invalid/