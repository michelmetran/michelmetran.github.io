---
title: "Git: <i>basics</i>"
date: 2023-05-04T00:00:00-03:00
last_modified_at: 2023-10-30T00:00:00-03:00
excerpt_separator: "<!--more-->"
categories:
  - IT
tags:
  - git
  - github
---

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
