---
title: "Requirements"
excerpt_separator: "<!--more-->"
tags: [python, pycharm, jupyter, package]
---

O arquivo _requirements.txt_, usualmente localizado na pasta-raiz do projeto, tem a finalidade de listar quais são os _packages_ que foram utilizados naquele determinado projeto.

<!--more-->

Muitas vezes, no curso de um _script_, é possível instalar uma dependência utilizando o `pip install {nome do pacote}`, porém o arquivo _requirements.txt_ se faz fundamental quando os projetos serão acessados por aplicações, tais como **_Django_**, **_Flask_**, **_Heroku_** e **_MyBinder_**, por exemplo, sendo esse o motivo principal para criar esse arquivo.

<br>

### _Pip Freeze_

O comando `pip freeze` é o mais difundido na internet para se criar o arquivo _requirements.txt_, ou seja, o arquivo com o qual é possível indicar quais os _packages_ necessários para rodar um determinado _script_. O problema é que **ele não lista apenas** os _packages_ utilizados em um determinado _script_, listando **TODOS** os _packages_ de instalados no _python_ (ou ambiente _python_).

Particularmente eu utilizo _enviroments_ do Conda, com dezenas de pacotes instalados em cada _enviroments_, e os arquivos _requirements.txt_ ficavam muito extensos, apresentando alguns problemas.

```python
#pip freeze > requirements.txt
```

<br>

### _Pipreqs_

O pacote [**pipreqs**](https://pypi.org/project/pipreqs/), pelas descrições, pareceu atender a demanda de lista **APENAS** os pacotes de um determinado projeto. Porém ele não funciona diretamente no _Juptyter Notebook_, motivo que foi preciso inserir um ponto de exclamação no início do comando, para que o _jupyter_ interpretasse que se trata de um comando a ser feito em _bash_.

```python
!pipreqs '.' --force --debug --print
```

<br>

### _Environment.yml_

Descobri ainda que o comando ` conda env export > environment.yml` pode auxiliar na criação destes parâmetros, não sendo exatamente o que se busca, ou seja, o arquivo _requirements.txt_ necessário para aplicações.

```python
#!conda env export > environment.yml
```

<br>

### PIP

É possível, dentro de um ambiente _conda_, instalar um _package_ por meio do _pip_, usando o comando.

```python
pip3 install {package name}
pip3 install folium --upgrade
```
