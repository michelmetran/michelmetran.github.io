---
layout: post
title: Git Basics
subtitle: Comandos Básicos para atualizar repositórios do GitHub
tags: [linux, git, github, gitpages]
image: /img/posts/icon_github.png
bigimg: /img/posts/big_git.png
comments: true
---

O **<a title="Link do GitHub" href="https://github.com/" target="_blank">GitHub</a>** é uma plataforma de hospedagem de código-fonte com controle de versão usando o **<a title="Link do Git" href="https://git-scm.com/" target="_blank">Git</a>**. Ele permite que programadores, utilitários ou qualquer usuário cadastrado na plataforma contribuam em projetos privados e/ou _Open Source_ de qualquer lugar do mundo.

A alteração/contribuição em um dado projeto se dá por meio do comando **_commit_**, ou seja, o ato de fazer um _upload_ dos códigos para um repositírio.

{: .box-warning}
**Aviso:** Esse _post_ tem a finalidade de apresentar __apenas__ os comandos básicos e me deixar com uma "cola" rápida para meu uso cotidiano. Logo, todos os códigos são exemplificativos e podem/devem ser alterados, indicando o nome dos arquivos e diretórios corretamente.

<br>

### Criar um novo Repositório no PC local
Para criar um repositório, a ser enviado posteriormente para o  **<a title="Link do GitHub" href="https://github.com/" target="_blank">GitHub</a>** (ou qualquer outro serviço para hospedar códigos) é necessário iniciar o _git_, ou seja, o versionamento, em um dado diretório. Para isso basta cria-lo, acessa-lo e iniciá-lo.
~~~
mkdir --parents /home/michel/Documents/GitRepo/{Nome do Diretório}
cd /home/michel/Documents/GitRepo/{Nome do Diretório}
git init
~~~
<br>

### Clonar (_ou copiar_) um Repositório existente
#### ... do GitHub para o PC local
Basta acessar a basta aonde estão listados os diretórios e dar o comando **_clone_**.

Isso deve ser feito no por meio do comando genérico _git clone /caminho/para/o/repositório_ ou, quando em um servidor, o comando será _git clone usuário@servidor:/caminho/para/o/repositório_.
~~~
cd /home/michel/Documents/GitRepo
git clone git@github.com:jekyll/jekyll					# Ex. 1
git clone git@github.com:michelmetran/michelmetran.github.io.git	# Ex. 2
~~~
<br>

#### ... do PC local para o PC local
~~~
cd /home/michel/Documents
git clone /home/michel/Documents/GitRepo/jekyll
~~~
<br>

### Atualizar (_comitar_) alterações em um Repositório
Inicialmente vá até o diretório local que tem os arquivos a serem enviados para o **<a title="Link do GitHub" href="https://github.com/" target="_blank">GitHub</a>**. No meu caso _/home/michel/Documents/GitRepo/{Nome do Repositório}_.
~~~
cd /home/michel/Documents/GitRepo/michelmetran.github.io
~~~

E adiciona todos os arquivos a serem _"comitados"_ e, por meio do comando **_push_**, é realizado o **_upload_** dos arquivos para o **<a title="Link do GitHub" href="https://github.com/" target="_blank">GitHub</a>**.
~~~
git add --all
git commit -m "Initial commit"
git push -u origin master
~~~

Para adicionar arquivos, recomenda-se incluir apenas os arquivos modificados. Para isso o comando **_git add -all_** deve ser alterado conforme tabela abaixo:

| Comando | Inclui Novos | Inclui Modificados | Inclui Removidos | Descrição
| :------ |:--- | :--- | :--- | :---
| _git add --all_ _git add -A_ | Sim | Sim | Sim | Adiciona **arquivos e diretórios (_novos, modificados ou removidos_)**, que começam ou não com .
| _git add *_ | Sim | Sim | Sim | Adiciona **arquivos e diretórios (_novos, modificados ou removidos_)**, ignorando aqueles que começam com .
| _git add ._ | Sim | Sim | Sim | Adiciona **apenas arquivos (_novos, modificados ou removidos_)**, ignorando aqueles que começam com .
| _git add -u_ | Não | Sim | Sim | Adiciona **apenas arquivos (_modificados e removidos_)**, ignorando os **_novos_**

Ainda há a possibilidade de adicionar apenas um arquivo a ser _comitado_ por meio do comando abaixo.
~~~
git add {filename}
~~~

<br>

### Atualizar o Repositório local
É possível fazer o **_download_** dos arquivos do **<a title="Link do GitHub" href="https://github.com/" target="_blank">GitHub</a>**, atualizando o repositório local. Isso é útil quando são realizadas modificações nos arquivos por outros meios (diretamente pelo **<a title="Link do GitHub" href="https://github.com/" target="_blank">GitHub</a>**, por meio do **<a title="Link do StackEdit" href="https://stackedit.io/" target="_blank">StackEdit</a>** ou qualquer outro editor _online_, por exemplo).
~~~
git pull origin master
~~~

<br>

### _Status_ do Repositório
No diretório local insira o seguinte comando.
~~~
git status
~~~

<br>

{: .box-error}
**Informações:** Existem muitos outros comandos existentes a serem aprendidos que ainda não utilizei. Toda a discussão sobre _branchs_..., aplicação do comando **_add_** apenas aos arquivos alterados, evitando o **_git add --all_**. Aqui sintetizei apenas o conhecimento adquirido até o momento que venho utilizando em meus repositórios.

<br>
