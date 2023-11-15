---
title: "Conda: <i>Portable</i>"
date: 2019-06-13T15:34:30-04:00
last_modified_at: 2022-06-28T00:00:00-03:00
excerpt_separator: "<!--more-->"
categories:
  - IT
tags:
  - python
  - anaconda
  - miniconda
---

Existe a opção de instalar o Conda em modo _portable_!! Para mais informações, consultar [Conda: Installing in silent mode](https://docs.conda.io/projects/conda/en/latest/user-guide/install/windows.html#installing-in-silent-mode).

```powershell
start /wait "" Miniconda3-latest-Windows-x86_64.exe /InstallationType=JustMe /AddToPath=0 /RegisterPython=0 /NoRegistry=1 /D=%USERPROFILE%\Documents\Conda
```

<br>

Também foi adicionado nas em `PATH`, nas variávels de ambiente:

```powershell
%USERPROFILE%\Documents\Conda
%USERPROFILE%\Documents\Conda\Scripts
%USERPROFILE%\Documents\Conda\Library\bin
%USERPROFILE%\Documents\Conda\Library\condabin
```

- [StackOverflow: Can Anaconda be packaged for a portable zero-configuration install?](https://stackoverflow.com/questions/39984611/can-anaconda-be-packaged-for-a-portable-zero-configuration-install)

Como o Conda não foi instalado da maneira padrão, é necessário acessar a pasta `C:\Users\{username}\Documents\Apps\Miniconda\condabin` para criar e manejar _enviroments_.

Descobri ainda que os _enviroments_, que usualmente ficam em `C:\Users\{username}\Documents\Apps\Miniconda\envs`, passaram a ficar em `C:\Users\{username}\.conda\env`
