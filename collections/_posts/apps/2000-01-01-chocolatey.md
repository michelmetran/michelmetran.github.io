---
title: "Chocolatey"
date: 2019-06-13T15:34:30-04:00
last_modified_at: 2022-06-28T11:00:00-03:00
excerpt_separator: "<!--more-->"
categories:
  - IT
tags:
  - aplicativos
---

Nunca gostei de instalar aplicativos no Windows. É uma tarefa chata, após cada formatação (nos PCs pessoais, de amigos e família), era necessário acessar cada _site_ do aplicativo, fazer o _download_, e instalar.

Para facilitar essa etapa, eu costumava ter uma pasta de executáveis (arquivos _.exe_) para instalar os aplicativos. Os arquivos executáveis usualmente grandes, ocupavam bastante espaço em um HD e, frequentemente, estavam desatualizados!

Quando passei a usar o Ubuntu, vi o quão fácil é instalar um aplicativo por meio de uma linha de comando. Achava mágico, com um simples comando `sudo apt install code`, ter o editor VsCode instalado no meu PC, por exemplo.

<!--more-->

Essa facilidade me fez buscar usar e aprender aplicativos que sejam de fácil instalação e manutenção. Com isso, passei a usar/buscar projetos _freeware_, que não dependessem de pirataria, _cracks_, _patchs_, _keygens_ os quais, além de dependerem de ajustes manuais, também contribuem (e muito!) para aumentar a vulnerabilidade dos PC.

Ainda assim, a facilidade proporcionada pelo gerenciador de pacotes `apt` limitava-se ao meu Debian/Ubuntu. Contudo, muitos PCs que uso tem sistema operacional Windows e eu ficava transtornado com a dificuldade de manter aplicativos instalados e atualizados em comparação ao Ubuntu. Nesse contexto que conheci o [Chocolatey.org](https://chocolatey.org/), um gerenciador de pacotes para Windows!

Com ele é possível instalar várias aplicações por meio de linhas de comando e mante-las atualizadas! Aprendi alguns passos básicos ao ler o artigo [How to install chocolatey/choco on Windows 10](https://jcutrer.com/windows/install-chocolatey-choco-windows10).

<br>

---

## Instalando o Choco

```powershell
# Instala Choco
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
```

<br>

---

## Comandos Básicos

```powershell
# Help
choco -?

# Procurar pacote
choco search hugo

# Atualizar Choco
choco upgrade chocolatey

# Atualiza tudo
choco upgrade all -y

# Lista pacotes instalados pelo choco
choco list --local-only

# Desistala
choco uninstall microsoft-teams.install -x
```

<br>

---

## Instalando Aplicativos

Abaixo listei os aplicativos que eu uso, porém existem muito outros [_packages_](https://community.chocolatey.org/packages) disponíveis.

### Internet

```shell
choco install firefox -y
choco install googlechrome -y
choco install jre8 -y
```

<br>

### Office

```shell
choco install 7zip.install -y
choco install adobereader -y
choco install googledrive -y
choco install libreoffice-fresh -y
choco install miktex.install -y
choco install notepadplusplus.install -y
choco install office365business -y
choco install pandoc -y
choco install sshfs -y
choco install winrar -y
```

<br>

### Comunicação

```shell
choco install discord -y
choco install microsoft-teams -y
choco install slack -y
choco install teamviewer -y
choco install telegram -y
choco install zoom -y
```

<br>

### Geo

```shell
choco install qgis -y
choco install qgis-ltr -y
choco install googleearthpro -y
```

<br>

### Codes

```shell
choco install azure-data-studio -y
choco install daxstudio -y
choco install docker-desktop -y
choco install dotnetfx -y
choco install dotnet-7.0-sdk -y
choco install filezilla -y
choco install git.install -y
choco install javaruntime -y
choco install jetbrainstoolbox -y
choco install miniconda3 -y
choco install miniconda3 --params="'/AddToPath:1'" -y
choco install microsoft-windows-terminal -y
choco install netfx-4.8-devpack -y
choco install powerbi -y
choco install soapui -y
choco install r.studio -y
choco install r.project -y
choco install r.project --force --params "/AddToPath"
choco install ruby -y
choco install tableau-public -y
choco install vcredist140 -y
choco install vscode -y
choco install visualstudio2022community -y
```

<br>

### Mídia

```shell
choco install audacity -y
choco install audacity-lame -y
choco install ghostscript -y
choco install inkscape -y
choco install obs-studio -y
choco install screentogif -y
choco install sharex -y
choco install spotify -y
choco install vlc -y
```

<br>

### Manutenção

```shell
choco install ccleaner -y
choco install partitionwizard -y
choco install treesizefree -y
choco install zerotier-one -y
```

<br>

### Files

```shell
choco install virtualbox --params "/NoDesktopShortcut /CurrentUser /ExtensionPack"
```

<br>

### Others

```shell
# GitHub: https://github.com/arkane-systems/mousejiggler
# Choco: https://community.chocolatey.org/packages/mouse-jiggler
choco install mouse-jiggler -y
```

<br>

### Conda

```shell
'/InstallationType:AllUsers'
choco install miniconda3 --params="'/AddToPath:1' '/RegisterPython:1' '/D:%USERPROFILE%\Documents\Conda'"

start /wait "" Miniconda3-latest-Windows-x86_64.exe /InstallationType=JustMe /AddToPath=0 /RegisterPython=0 /NoRegistry=1 /D=%USERPROFILE%\Documents\Conda
```
