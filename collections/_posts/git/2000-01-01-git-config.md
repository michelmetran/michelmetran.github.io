---
title: "Git: <i>config</i>"
date: 2023-05-04T00:00:00-03:00
last_modified_at: 2023-10-30T00:00:00-03:00
excerpt_separator: "<!--more-->"
categories:
  - IT
tags:
  - git
  - github
---

[Git](https://git-scm.com/) é um sistema de controle de versão distribuído gratuito e de código aberto projetado para lidar com tudo, desde projetos pequenos a muito grandes com velocidade e eficiência.

<!--more-->

O [GitHub](https://github.com/) é uma plataforma de hospedagem de código-fonte com controle de versão usando o [Git](https://git-scm.com/). Ele permite que programadores, utilitários ou qualquer usuário cadastrado na plataforma contribuam em projetos privados e/ou _Open Source_ de qualquer lugar do mundo.

A alteração/contribuição em um dado projeto se dá por meio do comando **_commit_**, ou seja, o ato de fazer um _upload_ dos códigos para um repositório.

**Aviso:** Esse _post_ tem a finalidade de apresentar **apenas** os comandos básicos e me deixar com uma "cola" rápida para meu uso cotidiano. Logo, todos os códigos são exemplificativos e podem/devem ser alterados, indicando o nome dos arquivos e diretórios corretamente.
{: .notice--primary}

**Informações:** Existem muitos outros comandos existentes a serem aprendidos que ainda não utilizei. Toda a discussão sobre _branchs_..., aplicação do comando **_add_** apenas aos arquivos alterados, evitando o **_git add --all_**. Aqui sintetizei apenas o conhecimento adquirido até o momento que venho utilizando em meus repositórios.
{: .notice--info}

<br>

---

## Instalando

Inicialmente é interessante avaliar se o git já não está instalado!

```bash
# Versão do Git
git --version
```

<br>

Se receber um resultado semelhante ao seguinte, o Git já está instalado.

```bash
# Output
git version 2.42.0
```

<br>

Senão receber tal mensagem, é necessário instalar

<br>

**Instalando no Linux**

```bash
sudo apt update
sudo apt install git
```

<br>

**No Windows**, usando o _choco_

```bash
choco install git
```

<br>

---

## Configurações Iniciais

Uma vez instalado é necessário configurá-lo, definindo o usuário e e-mail.

```bash
git config --global user.name "Michel Metran"
git config --global user.email "michelmetran@gmail.com"
```

<br>

É possível checar as informações com o comando

```bash
git config --list
```

<br>

Este comando apresenta o conteúdo do arquivo `~/.gitconfig` e é possível editado diretamente por meio do `sudo nano ~/.gitconfig`.

<br>

---

### Criando Par de Chaves

Visto que estamos com o OpenSSH instalado, é possível criar um par de chaves para autenticação, evitando o uso de senhas.

Inicialmente criamos as chaves.

```powershell
# Cria Par de Chaves
ssh-keygen -t rsa -b 4096 -C "michelmetran@gmail.com"
ssh-keygen -t ed25519 -C "michelmetran@gmail.com"

# Copia o conteúdo (Linux)
cat ~/.ssh/id_rsa.pub
cat ~/.ssh/id_ed25519.pub

# Copia o conteúdo (Powershell)
Get-Content ~\.ssh\id_rsa.pub | clip
Get-Content ~\.ssh\id_ed25519.pub | clip
```

<br>

---

## Git e OpenSHH

**Apenas no Windows** é necessário também "avisar" o _git_ que é pra usar o _OpenSSH_ do Windows. Para isso é necessário informar ao _git_ sua localização. Essa configuração foi observada aqui [Windows 10 SSH client: password-less access](https://superuser.com/questions/1433917/windows-10-ssh-client-password-less-access)

```powershell
git config --global core.sshCommand C:/Windows/System32/OpenSSH/ssh.exe
```

<br>

**Referências**

- [Installing and using Git and GitHub on Ubuntu Linux: A beginner's guide](https://www.howtoforge.com/tutorial/install-git-and-github-on-ubuntu/)
- [Gerar uma nova chave SSH e adicioná-la ao ssh-agent](https://help.github.com/pt/github/authenticating-to-github/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)
