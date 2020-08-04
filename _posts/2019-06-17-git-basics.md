---
layout: post
title: Git Basics
subtitle: Comandos Básicos para atualizar repositórios do GitHub

thumbnail-img: /assets/img/posts/github_icon.png
share-img: /assets/img/posts/github_big.png
cover-img: /assets/img/posts/github_big.png

comments: true
language: pt-br
tags: [linux, git, github, gitpages]
---

O **<a title="Link do GitHub" href="https://github.com/" target="_blank">GitHub</a>** é uma plataforma de hospedagem de código-fonte com controle de versão usando o **<a title="Link do Git" href="https://git-scm.com/" target="_blank">Git</a>**. Ele permite que programadores, utilitários ou qualquer usuário cadastrado na plataforma contribuam em projetos privados e/ou _Open Source_ de qualquer lugar do mundo.

A alteração/contribuição em um dado projeto se dá por meio do comando **_commit_**, ou seja, o ato de fazer um _upload_ dos códigos para um repositório.

{: .box-warning}
**Aviso:** Esse _post_ tem a finalidade de apresentar __apenas__ os comandos básicos e me deixar com uma "cola" rápida para meu uso cotidiano. Logo, todos os códigos são exemplificativos e podem/devem ser alterados, indicando o nome dos arquivos e diretórios corretamente.



[TOC]



## Definindo Configurações Iniciais

```bash
git config --global user.name "michelmetran"
git config --global user.email "michelmetran@gmail.com"
```



## Criar um novo Repositório no PC local
Para criar um repositório, a ser enviado posteriormente para o **<a title="Link do GitHub" href="https://github.com/" target="_blank">GitHub</a>** (ou qualquer outro serviço para hospedar códigos) é necessário iniciar o *git*, ou seja, o versionamento, em um dado diretório. Para isso basta cria-lo, acessa-lo e iniciá-lo.
~~~bash
cd /home/michel/Geodata/SourceCode/

mkdir --parents {Nome do Diretório}
cd {Nome do Diretório}
git init
~~~


## Clonar (_ou copiar_) um Repositório existente

### ... do GitHub para o PC local
Basta acessar a basta aonde estão listados os diretórios e dar o comando ***clone***.

Isso deve ser feito no por meio do comando genérico *git clone /caminho/para/o/repositório* ou, quando em um servidor, o comando será *git clone usuário@servidor:/caminho/para/o/repositório*.
~~~bash
cd /home/michel/Geodata/SourceCode
git clone git@github.com:jekyll/jekyll					# Ex. 1

git clone git@github.com:michelmetran/michelmetran.github.io.git
git clone git@github.com:michelmetran/ArcGIS-Transformation.git
git clone git@github.com:michelmetran/ArcGIS-TrackSource.git
git clone git@github.com:michelmetran/ArcGIS-IGC.git
git clone git@github.com:michelmetran/ArcGIS-Convert.git
git clone git@github.com:michelmetran/ArcGIS-SiCAR.git
~~~
<br>

### ... do PC local para o PC local

~~~bash
cd /home/michel/Geodata
git clone /home/michel/Geodata/SourceCode/jekyll
~~~
<br>

## Atualizar repositório remoto

Inicialmente vá até o diretório local que tem os arquivos a serem enviados para o **<a title="Link do GitHub" href="https://github.com/" target="_blank">GitHub</a>**. No meu caso _/home/michel/Geodata/SourceCode/{Nome do Repositório}_.
~~~bash
cd /home/michel/Geodata/SourceCode/michelmetran.github.io
~~~

E adiciona todos os arquivos a serem _"comitados"_ e, por meio do comando **_push_**, é realizado o **_upload_** dos arquivos para o **<a title="Link do GitHub" href="https://github.com/" target="_blank">GitHub</a>**.
~~~bash
git add --all
git commit -m "Initial commit"
git push origin master
~~~

Para adicionar arquivos, recomenda-se incluir apenas os arquivos modificados. Para isso o comando **_git add -all_** deve ser alterado conforme tabela abaixo:

| Comando | Inclui Novos | Inclui Modificados | Inclui Removidos | Descrição
| :------ |:--- | :--- | :--- | :---
| _git add --all_ _git add -A_ | Sim | Sim | Sim | Adiciona **arquivos e diretórios (_novos, modificados ou removidos_)**, que começam ou não com .
| _git add *_ | Sim | Sim | Sim | Adiciona **arquivos e diretórios (_novos, modificados ou removidos_)**, ignorando aqueles que começam com .
| _git add ._ | Sim | Sim | Sim | Adiciona **apenas arquivos (_novos, modificados ou removidos_)**, ignorando aqueles que começam com .
| _git add -u_ | Não | Sim | Sim | Adiciona **apenas arquivos (_modificados e removidos_)**, ignorando os **_novos_**

Ainda há a possibilidade de adicionar apenas um arquivo a ser _comitado_ por meio do comando abaixo.
~~~bash
git add {filename}
~~~




## Atualizar o repositório local
É possível fazer o **_download_** dos arquivos do **<a title="Link do GitHub" href="https://github.com/" target="_blank">GitHub</a>**, atualizando o repositório local. Isso é útil quando são realizadas modificações nos arquivos por outros meios (diretamente pelo **<a title="Link do GitHub" href="https://github.com/" target="_blank">GitHub</a>**, por meio do **<a title="Link do StackEdit" href="https://stackedit.io/" target="_blank">StackEdit</a>** ou qualquer outro editor _online_, por exemplo).
~~~bash
git pull origin master
~~~



## Outros

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



## Branching

```bash
# Para listar branchs e ver qual está ativa
git branch
```

## 

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











{: .box-error}
**Informações:** Existem muitos outros comandos existentes a serem aprendidos que ainda não utilizei. Toda a discussão sobre _branchs_..., aplicação do comando **_add_** apenas aos arquivos alterados, evitando o **_git add --all_**. Aqui sintetizei apenas o conhecimento adquirido até o momento que venho utilizando em meus repositórios.