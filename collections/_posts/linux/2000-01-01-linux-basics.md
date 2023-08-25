---
title: "Linux: *Basics*"
date: 2023-05-04T00:00:00-03:00
last_modified_at: 2023-05-04T00:00:00-03:00
excerpt_separator: "<!--more-->"
categories:
  - IT

tags:
  - python
  - pycharm
  - jupyter
  - package
  - pandas
---

# Settings

gnome-system-monitor

<br>

---

## Manejando Arquivos

### Manejando diretórios

Para ver em qual diretório o terminal está

```bash
pwd
```

Para criar diretório

```bash
mkdir FolderName
```

Para criar múltiplos diretórios

```bash
mkdir -p Aulas/{Informática\ Aplicada,Redes,MMC,Imagens/Festas/Férias}
mkdir -p Teste/{games,videos,musicas/{hiphop,novelas},imagens/{fotos,paisagens}}
```

Para criar múltiplos diretórios em sequências

```bash
mkdir -p Teste/Sequência\ {1..6}
mkdir -p Teste/Sequência\ {a..f}
```

Para remover diretório

```bash
rm -r FolderName
rm -r Aulas
```

Vai para o Diretório do Usuário

```bash
cd ~
```

Vai para um Diretório definido

```bash
cd /home/michel/Documents/SSD
```

Sobe um Diretório

```bash
cd ..
```

Para listar conteúdos

```bash
ls              # lista arquivos
ls -lh          # lista arquivos com propriedades
ls -lha         # lista arquivos com propriedades incluindo ocultos
```

Cópia de pasta com seu conteúdo

```bash
cp -r Downloads Teste_Dow
```

Cópia de arquivo

```bash
cp arquivo.txt Documents/.
cp ~/Templates/LibreOffice\ Writer.odt Documents/.
```

Cópia do arquivo1 renomeando-o para arquivo2.

```bash
cp arquivo1 arquivo2
```

Cópia do arquivo1 e cola na pasta de destino mantendo o mesmo nome

```bash
cp /pasta/origem/arquivo1 /pasta/destino/
```

Cópia renomeando o arquivo1 para arquivo2

```bash
cp /pasta/origem/arquivo1 /pasta/destino/arquivo2
cp /etc/fstab /etc/fstab_backup
```

Mover arquivo

```bash
mv ~/Documents/LibreOffice\ Writer.odt Music/.
```

Pesquisar por nome de arquivo em uma determinada pasta

```bash
find /home -name canaltech.txt
```

Pesquisar por palavras dentro de arquivos

```bash
grep "Palavra que quer encontrar" arquivo.txt  Pesquisa simples
grep -i "Palavra que quer encontrar" arquivo.txt  Pesquisa que ignora se está em caixa alta
```

Download de Arquivos

[Wget: o que é, como instalar e exemplos de comandos Wget para Linux](https://www.hostinger.com.br/tutoriais/wget-o-que-e-como-instalar-comandos-wget)

<br>

---

### _Links_ Simbólicos

Criar Links simbólicos (atalhos)

```bash
#ln -s /path/original /path/to/link
#ln -s ~/Music Pictures
#ln -s /media/temp /home/michel
```

```bash
ln -s /media/michel/Arquivos /home/michel/Documents
ln -s /media/michel/Geodata/Sourcecode /home/michel/Documents
ln -s /media/michel/VMs /home/michel/Documents
```

[How to Create and Use Symbolic Links (aka Symlinks) on Linux](https://www.howtogeek.com/287014/how-to-create-and-use-symbolic-links-aka-symlinks-on-linux/)

<br>

---

## Configurações

### _Tweaks_

[Disable Desktop Icons ‘User Home’ & ‘Trash’ in Ubuntu 19.04](http://ubuntuhandbook.org/index.php/2019/04/disable-desktop-icons-user-home-trash-ubuntu-19-04/), que também se aplica ao 19.10

Dicas que peguei [nesse link](https://www.youtube.com/watch?v=ynA_zv2eRzE) para fazer após a instalação do Ubuntu 18.04:

Comando para atualizar o Ubuntu e Programas

```bash
sudo apt-get update
```

Instalar Codecs

```bash
sudo apt-get update
```

Caso tenha uma unidade de DVD, instalar usando:

```bash
sudo apt install libdvd-pkg
```

Instalar Shell no navegador

```bash
sudo apt install chrome-gnome-shell
```

Instalar app Tweaks for Ubuntu

```bash
sudo apt install gnome-tweak-tool
```

[How to install Tweak Tool on Ubuntu 20.04 LTS Focal Fossa Linux](https://linuxconfig.org/how-to-install-tweak-tool-on-ubuntu-20-04-lts-focal-fossa-linux)

Cria arquivos do LibreOffice na pasta templates

```bash
sudo apt install libreoffice-java-common
touch ~/'LibreOffice Writer.odt' && libreoffice --writer ~/Templates/'LibreOffice Writer.odt'
```

<br>

---

### Mouse

https://www.diolinux.com.br/2015/04/como-mudar-velocidade-do-scroll-do-mouse-ubuntu.html

```bash
sudo apt-get install imwheel
```

```bash
gedit ~/.imwheelrc
“.*”
None, Up, Up, 3
None, Down, Down, 3
```

<br>

---

### Teclas de Atalho

Alt+F2 = Executar. Equivalente ao Win+R no Windows

Ctrl+H = Oculta/Descoculta arquivos no Nautilus. Equivalente do Windows Explorer.

Descobrir a versão

```bash
cat `ls /etc/*release /etc/*version`
```

<br>

---

## Recursos

### Imagens

https://www.tecmint.com/optimize-and-compress-jpeg-or-png-batch-images-linux-commandline/

http://ask.xmodulo.com/compress-jpeg-images-command-line-linux.html

<br>

---

### _Print Screen_

Tentativa 1

```
gsettings set org.gnome.gnome-screenshot auto-save-directory 'file:///home/michel/Dropbox/Capturas de tela'
```

Tentativa 2

https://askubuntu.com/questions/114429/how-can-i-specify-the-default-save-directory-for-gnome-screenshot

https://linuxconfig.org/how-to-install-gnome-shell-extensions-on-ubuntu-18-04-bionic-beaver-linux

https://extensions.gnome.org/extension/1179/screenshot-locations/

```bash
sudo apt install gnome-shell-extensions
```

<br>

---

## _Bugs_

### Show Applications Freeze

```bash
sudo apt install dconf-editor
```

[The Applications screen freezes when I open and close the folder](https://askubuntu.com/questions/1239945/the-applications-screen-freezes-when-i-open-and-close-the-folder)
