---
layout: post
title: Git Basics
subtitle: Comandos Básicos para atualizar repositórios do GitHub
tags: [linux, git, github, gitpages]
bigimg: /img/posts/git.png
comments: true
---

O <a title="Link do GitHub" href="https://github.com/" target="_blank">GitHub</a> é uma plataforma de hospedagem de código-fonte com controle de versão usando o <a title="Link do Git" href="https://git-scm.com/" target="_blank">Git</a>. Ele permite que programadores, utilitários ou qualquer usuário cadastrado na plataforma contribuam em projetos privados e/ou Open Source de qualquer lugar do mundo.

Esse _post_ tem a finalidade de mostrar os comandos básicos e me deixar com uma "cola" rápida para meu uso cotidiano.

{: .box-warning}
**Aviso:** Todas os códigos são exemplificativos e podem/devem ser alterados, indicando o nome das pastas e arquivos corretamente.

<br>
<br>
### Comitar alterações em um repositório no _GitHub_
Vai para a pasta no seu PC que tem os arquivos a serem enviados para o GitHub. No meu caso _/home/michel/Documents/GitPages/michelmetran.github.io_.
~~~
cd /home/michel/Documents/GitPages/michelmetran.github.io
~~~

Adiciona todos os arquivos que estão no drive a serem comutados e, por meio do comando **_push_**, é feito o _upload_ dos arquivos para o <a title="Link do GitHub" href="https://github.com/" target="_blank">GitHub</a>.
~~~
git add --all
git commit -m "Initial commit"
git push -u origin master
~~~

Há a possibilidade de baixar fazer o _download_ dos arquivos do <a title="Link do GitHub" href="https://github.com/" target="_blank">GitHub</a>. Isso é útil quando são realizadas modificações nos arquivos por outros meios (diretamente pelo GitHub ou por meio do <a title="Link do StackEdit" href="https://stackedit.io/" target="_blank">StackEdit</a>, por exemplo).
~~~
git pull origin master
~~~
<br>
<br>
### _Download_ um repositório no _GitHub_
Para fazer um _download_, **pela primeira vez**, do conjunto de arquivos de um repositório no <a title="Link do GitHub" href="https://github.com/" target="_blank">GitHub</a> basta ir na pasta que receberá o repositório e dar o comando **_clone_**

~~~
cd /home/michel/Documents/GitPages/michelmetran.github.io
git clone git@github.com:michelmetran/michelmetran.github.io.git
~~~
<br>
<br>
### _Upload_ um repositório no _GitHub_

(Errado / Editar) 
