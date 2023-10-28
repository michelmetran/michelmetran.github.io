---
title: "Git"
date: 2023-05-04T00:00:00-03:00
last_modified_at: 2023-05-04T00:00:00-03:00
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

## Instalando

Inicialmente é interessante avaliar se o git já não está instalado!

```bash
git --version
```

<br>

Se receber um resultado semelhante ao seguinte, o Git já está instalado.

```bash
# Output
git version 2.25.1
```

<br>

Senão receber tal mensagem, é necessário instalar

<br>

### Instalando no Linux

```bash
sudo apt update
sudo apt install git
```

<br>

## Configurações Iniciais

Uma vez instalado é necessário configura-lo, definindo o usuário e e-mail.

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

Este comando apresenta o conteúdo do arquivo `~/.gitconfig` e é possível editado diretamente por meio do `sudo gedit ~/.gitconfig`

<br>

### Github

```powershell
ssh-keygen -t rsa -b 4096 -C "michelmetran@gmail.com"
ssh-keygen -t ed25519 -C "michelmetran@gmail.com"

# Copia Bash
cat ~/.ssh/id_rsa.pub
cat ~/.ssh/id_ed25519.pub

# Copia Powershell
Get-Content ~\.ssh\id_rsa.pub | clip
Get-Content ~\.ssh\id_ed25519.pub | clip
```

<br>

**Referências**

- [Installing and using Git and GitHub on Ubuntu Linux: A beginner's guide](https://www.howtoforge.com/tutorial/install-git-and-github-on-ubuntu/)
- [Gerar uma nova chave SSH e adicioná-la ao ssh-agent](https://help.github.com/pt/github/authenticating-to-github/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)

---

<br>

### Criar um novo Repositório no PC local

Para criar um repositório, a ser enviado posteriormente para o **<a title="Link do GitHub" href="https://github.com/" target="_blank">GitHub</a>** (ou qualquer outro serviço para hospedar códigos) é necessário iniciar o _git_, ou seja, o versionamento, em um dado diretório. Para isso basta cria-lo, acessa-lo e iniciá-lo.

```bash
cd /home/michel/Codes/

mkdir --parents {Nome do Diretório}
cd {Nome do Diretório}
git init
```

<br>

### Clonar (_ou copiar_) um Repositório existente

#### ... do GitHub para o PC local

Basta acessar a basta aonde estão listados os diretórios e dar o comando **_clone_**.

Isso deve ser feito no por meio do comando genérico _git clone /caminho/para/o/repositório_ ou, quando em um servidor, o comando será _git clone usuário@servidor:/caminho/para/o/repositório_.

```bash
cd /home/michel/Geodata/SourceCode
git clone git@github.com:jekyll/jekyll
git clone git@github.com:michelmetran/michelmetran.github.io.git
```

<br>

#### ... do PC local para o PC local

```bash
cd /home/michel/Geodata
git clone /home/michel/Geodata/SourceCode/jekyll
```

<br>

### Atualizar repositório remoto

Inicialmente vá até o diretório local que tem os arquivos a serem enviados para o **<a title="Link do GitHub" href="https://github.com/" target="_blank">GitHub</a>**. No meu caso _/home/michel/Geodata/SourceCode/{Nome do Repositório}_.

```bash
cd /home/michel/Geodata/SourceCode/michelmetran.github.io
```

E adiciona todos os arquivos a serem _"comitados"_ e, por meio do comando **_push_**, é realizado o **_upload_** dos arquivos para o **<a title="Link do GitHub" href="https://github.com/" target="_blank">GitHub</a>**.

```bash
git add --all
git commit -m "Initial commit"
git push origin master
```

Para adicionar arquivos, recomenda-se incluir apenas os arquivos modificados. Para isso o comando **_git add -all_** deve ser alterado conforme tabela abaixo:

| Comando                      | Inclui Novos | Inclui Modificados | Inclui Removidos | Descrição                                                                                                   |
| :--------------------------- | :----------- | :----------------- | :--------------- | :---------------------------------------------------------------------------------------------------------- |
| _git add --all_ _git add -A_ | Sim          | Sim                | Sim              | Adiciona **arquivos e diretórios (_novos, modificados ou removidos_)**, que começam ou não com .            |
| _git add \*_                 | Sim          | Sim                | Sim              | Adiciona **arquivos e diretórios (_novos, modificados ou removidos_)**, ignorando aqueles que começam com . |
| _git add ._                  | Sim          | Sim                | Sim              | Adiciona **apenas arquivos (_novos, modificados ou removidos_)**, ignorando aqueles que começam com .       |
| _git add -u_                 | Não          | Sim                | Sim              | Adiciona **apenas arquivos (_modificados e removidos_)**, ignorando os **_novos_**                          |

Ainda há a possibilidade de adicionar apenas um arquivo a ser _comitado_ por meio do comando abaixo.

```bash
git add {filename}
```

<br>

### Atualizar o repositório local

É possível fazer o **_download_** dos arquivos do **<a title="Link do GitHub" href="https://github.com/" target="_blank">GitHub</a>**, atualizando o repositório local. Isso é útil quando são realizadas modificações nos arquivos por outros meios (diretamente pelo **<a title="Link do GitHub" href="https://github.com/" target="_blank">GitHub</a>**, por meio do **<a title="Link do StackEdit" href="https://stackedit.io/" target="_blank">StackEdit</a>** ou qualquer outro editor _online_, por exemplo).

```bash
git pull origin master
```

<br>

### Outros

```bash
# Status do repositório
git status

# Log do repositório
git log
git log --stat

# Versão do git
git --version
```

```bash
# Ver o repositório remoto
git remote
git remote -v

# Editar a mensagem do último commit (antes do push)
git commit --amend

# Ver modificações feitas no arquivo
git diff {nome do arquivo}

# Retirar um arquivo adicionado para commitar (após utilizar git add)
git reset HEAD {nome do arquivo}

# Marcar "compromissos específicos"
git tag 1.1.0 <insert-commitID-here>
```

Como remover a origem do repositório remoto?

```bash
git remote rm origin
```

O que é executado com o comando git remote add origin? Conectar meu repositório a um servidor remoto!

<br>

### Branching

```bash
# Para listar branchs e ver qual está ativa
git branch
```

```bash
# Para criar uma branch
git branch {nome da branch}

# Para deletar uma branch
git branch -D {nome da branch}
```

```bash
# Para criar uma branch e alternar para ativa-la
git checkout -b {nome da branch}
```

```bash
# Para alternar para uma branch
git checkout {nome da branch}
```

```bash
# Para unificar as branchs
git merge {nome da branch a unificar na branch ativa}
```

<br>

### Referências

- [LinuxHint: **Install Git in Ubuntu 20.04**](https://linuxhint.com/git-source-code-management-system/)

<br>

### Remote

git remote set-url origin [updated link url https://........git]
git remote set-url origin [git@github.com](mailto:git@github.com):michelmetran/github_actions.git

Git Portable
Git Credential Manager

Git Atribute
https://dev.to/deadlybyte/please-add-gitattributes-to-your-git-repository-1jld

# Atualizar

git update-git-for-windows




https://chrisjhart.com/Windows-10-ssh-copy-id/
