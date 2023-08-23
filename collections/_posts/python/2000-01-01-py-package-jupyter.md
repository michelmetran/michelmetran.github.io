---
title: "Jupyter Notebook"
excerpt_separator: "<!--more-->"
tags: [python, pycharm, jupyter, package]
categories: [blog]
---

O *Jupyter Notebook* é a maneira que optei para escrever os códigos na linguagem *python*, visto que além de rodar os
códigos, é possível:

<!--more-->

1. Documentar os *scripts*, escrevendo o significado e objetivo de cada conjunto de comandos;
2. Atualizar os meus repositórios na plataforma **GitHub**;
3. Trabalhar com uma diversidade de opções de exportação do arquivo em formatos diversos, adaptados até mesmo para as
   simples leitura, como PDFs e Markdowns.

Com tais caraterísticas, notei que é possível publicar *posts* diretamente do *Jupyter Notebook*. Aqui pretendo
apresentar um pouco das funções que tenho explorado para aperfeiçoar e facilitar minhas publicações no meu site
pessoal: https://michelmetran.github.io. E, pesquisando pela internet, descobri que não sou o único a [*Exploring Jupyer
Notebook to write a Blog*](https://medium.com/gopypi/exploring-jupyer-notebook-to-write-a-blog-1e7eaa913274), tem muito
material a ser explorado...

<div class="alert alert-warning">
<b>OBSERVAÇÃO</b><br/>
    Esse <i>post</i> tem a finalidade de mostrar os comandos básicos e me deixar com uma "cola" rápida para meu uso cotidiano.<br/>
    Todas os códigos são exemplificativos e podem/devem ser alterados, indicando o nome dos arquivos e diretórios corretamente.
</div>

<div class="alert alert-info">
<b>INFORMAÇÃO</b><br/>
    <ol>
    <li>É possível acessar esse <i>post</i> em formato <a href="https://rawcdn.githack.com/michelmetran/package_juypter/master/docs/juypter.html" target="_blank"><i><b>html</b></i></a>, que possibilita ter uma visualização rápida do código;</li>
    <li>Diretamente por meio do <a href="https://github.com/michelmetran/package_juypter" target="_blank"><b>repositório</b></a>, onde está disponível este arquivo <i><b>.ipynb</b></i>, que permite fazer edições no código;</li>
    <li>Ou ainda, de maneira interativa, usando o <a href="https://mybinder.org/v2/gh/michelmetran/package_juypter/master" target="_blank"><i><b>MyBinder</b></i></a>, que possibilita rodar e editar o código sem a necessidade de instalar nada.</li>
    </ol>
</div>

```python
import os
import json
import time
import folium
import pandas as pd
from datetime import date
```

```python
[os.makedirs(i, exist_ok=True) for i in ['docs']]
```

# Get *Jupyter Notebook* filename


Para as funções que serão apresentadas ao longo desse *script*, a obtenção do nome do arquivo *.ipynb* em uma variável
seria de grande ajuda. Não há modo fácil de obter, visto que para todas as opções, é necessário o *java*, que não
funciona quando é solicitado que todas as células rodem de uma só vez (Kernel > Run All).


## Diretamente na célula


Testei diversos comandos para obter o nome do *Jupyter Notebook* em uma variável. A melhor opção que encontrei estava
nesse [*post*](https://stackoverflow.com/questions/12544056/how-do-i-get-the-current-ipython-jupyter-notebook-name) que
tem diversas outras opções.

```javascript
%%
javascript

var kernel = IPython.notebook.kernel;
var body = document.body, attribs = body.attributes;
var command = 'ipynb_filename = ' + '"' + attribs['data-notebook-name'].value + '"';
kernel.execute(command);
```

```python
# ipynb_filename
```

```javascript
%%
javascript

var kernel = IPython.notebook.kernel;
var nb = IPython.notebook;
var command = 'ipynb_pathname = ' + '"' + nb.base_url + nb.notebook_path + '"';
kernel.execute(command);
```

```python
# ipynb_pathname
```

## Com função


Usei uma função que peguei na, provavelmente [aqui](https://github.com/jupyter/notebook/issues/1000), para pegar o nome
do arquivo *.ipynb*. Atualmente preferi, nas funões que necessitam do nome do arquivo, em escreve-lo como uma
constante... evitando o uso do *java* dentro do *Juptyter Notebook*.

```python
# %load '../codes/files/get_jupyternotebook_name.py'
def get_jupyternotebook_name():
    """
    Returns the name of the current notebook as a string
    From https://mail.scipy.org/pipermail/ipython-dev/2014-June/014096.html
    :return: Returns the name of the current notebook as a string
    """
    # Import Packages
    from IPython.core.display import Javascript
    from IPython.display import display

    display(Javascript('IPython.notebook.kernel.execute("theNotebook = " + \
    "\'"+IPython.notebook.notebook_name+"\'");'))

    # Result
    return theNotebook

```

```python
name = get_jupyternotebook_name()
name
```

# Markdown Cell


## Inserindo HTML


Sabendo que tanto o *framework* Jerkll, quando o *Jupyter Notebook* utilizam
o [BootStrap 4.0](https://getbootstrap.com/docs/4.0/components/alerts/), torna-se possível utilizar alguns parâmetros
para renderizar, nas células *markdown* um conteúdo mais interessante, bastando inserir as ```<div>``` abaixo.

```html

<div class="alert alert-success" role="alert">
    This is a success alert—check it out!
</div>
```

<div class="alert alert-success" role="alert">
  This is a success alert—check it out!
</div>
<div class="alert alert-danger" role="alert">
  This is a danger alert—check it out!
</div>
<div class="alert alert-warning" role="alert">
  This is a warning alert—check it out!
</div>
<div class="alert alert-info" role="alert">
  This is a info alert—check it out!
</div>

Ainda é possível criar *box* mais elaborados, escrevendo com os códigos em HTML.

<div class="alert alert-success" role="alert">
  <strong class="alert-heading">Well done!</strong>
  <p>Aww yeah, you successfully read this important alert message. This example text is going to run a bit longer so that you can see how spacing within an alert works with this kind of content.</p>
  <hr>
  <p class="mb-0">Whenever you need to, be sure to use margin utilities to keep things nice and tidy.</p>
</div>

Além de diversas outros elementos do [Bootstrap](https://getbootstrap.com/docs/4.0/getting-started/introduction/) que
podem ser inseridas, por exemplo:

<nav aria-label="...">
  <ul class="pagination">
    <li class="page-item disabled">
      <a class="page-link" href="#" tabindex="-1">Previous</a>
    </li>
    <li class="page-item"><a class="page-link" href="#">1</a></li>
    <li class="page-item active">
      <a class="page-link" href="#">2 <span class="sr-only">(current)</span></a>
    </li>
    <li class="page-item"><a class="page-link" href="#">3</a></li>
    <li class="page-item">
      <a class="page-link" href="#">Next</a>
    </li>
  </ul>
</nav>


## Variáveis em *Markdowns*

```python
# {{a}}
a = 10
```

Para inserir uma variável em uma célula markdow para eu inserir a variável entre colchetes duplos, por exemplo {{a}}.
Logo, se eu alterar o valor de a para qualquer um terei que **a={{a}}**.

O mesmo pode ser feito com tabelas. Em tentativa de inserir tabelas diretamente do Pandas não obtive sucesso... Depois
temos dataframe modificado pelo *.to_html()*
, [função](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_html.html) que fornece várias
opções a serem exploradas.

```python
df = pd.DataFrame({"A": [1.0, 2.2, 3.6666], "B": [4.12134, 5.674, 6.13215]})
```

```python
df_html = df.to_html(index=False, decimal='.', notebook=True, justify='center')
df_html = df_html.replace('\n', '')
```

{{df_html}}


## Linhas de Tabelas


Descobri que [nesse *
post*](https://stackoverflow.com/questions/38783027/jupyter-notebook-display-two-pandas-tables-side-by-side) que é
possível trabalhar para inserir também mais de uma tabela alinhada, mas isso se dá em uma célula de *output* (e não *
markdown*).

```python
import pandas as pd
import numpy as np
from IPython.display import display, HTML

CSS = """
.output {
    flex-direction: row;
}
"""

HTML('<style>{}</style>'.format(CSS))
```

```python
display(df)
```

<br>


## Comandos do Sistema


Praticamente qualquer comando do sistema pode ser acessado usando previamente **!**, o qual passa qualquer comando
subsequente diretamente para o sistema operacional. Você pode até usar variáveis python em comandos enviados para o
sistema operacional!

```python
!ls
```

É possível trabalhar com variáveis entre o *python* e esses comandos do sistema.

```python
file_type = 'ipynb'

!ls. / *$file_type
```

<br>


# Exportando o _Juptyter Notebook_


Os arquivos *Jupyter Notebook* podem ser exportados em diversos formatos, seja através do menu de opções, ou através dos
comandos. Ao exportar, é possível definir diversas opções que limitam o que será exportado, podendo escolher
determinados tipos de células ou, até mesmo, células invidivuais.

No *
post* [Jupyter Notebook nbconvert without Magic Commands/ w/o Markdown](https://stackoverflow.com/questions/57701538/jupyter-notebook-nbconvert-without-magic-commands-w-o-markdown)
é apresentado algumas opções de exportação. A página oficial do [NbConvert](https://nbconvert.readthedocs.io/) tem todos
os parâmetros, tanto para linhas de comando quanto para *python*.

<br>


## Linha de Comando


a maneira mais simples de exportar um arquivo é por meio do comando abaixo. O uso do ponto de explamação no início do
comando é pelo fato desse comando ser "nativo" da linha de comando, e não do python.

```python
!jupyter - nbconvert
jupyter.ipynb - -to
html - -output
docs / jupyter.html
```

Uma vez compreendida a função e sabendo que é possível inserir variáveis criadas no *python* em comandos de "linha de
comando", criei a seguinte rotina.

```python
# Input
inp = 'jupyter.ipynb'

# Output
out = os.path.join('docs', inp.split('.')[0])

# Extension to export ('html', 'html_embed', 'markdown', 'latex', 'pdf', 'python')
ext = 'html_embed'

# Remove cells with tag
tag = ("['" + '"remove_cell"' + ", " + '"yaml"' + "']")
!echo $tag
```

```python
!jupyter - nbconvert $inp
- -to $ext
- -TagRemovePreprocessor.enabled = True
- -TagRemovePreprocessor.remove_cell_tags =$tag
- -ClearOutputPreprocessor.enabled = True
- -TemplateExporter.exclude_markdown = False
- -TemplateExporter.exclude_code_cell = False
- -TemplateExporter.exclude_output = True
- -TemplateExporter.exclude_raw = False
- -TemplateExporter.exclude_input_prompt = True
- -TemplateExporter.exclude_output_prompt = True
- -output $out
```

<br>


## Função


Abaixo mostro uma função que escrevi para facilitar o processo de exportação do arquivo em diferentes locais do PC para,
posteriormente, atualizar os repositórios contidos
no <a title="Link do GitHub" href="https://github.com/michelmetran" target="_blank">*GitHub*</a>. Incorporei diversas
opções para exportação no script *../codes/files/export_jupyter.py*, quando notei que seria mais fácil usar os códigos
diretamente, sem funções.

```python
# %load '../codes/files/export_jupyter.py'
def export_jupyter(filename, path, extensions=['html', 'markdown', 'latex', 'pdf', 'python'], today=True):
    """
    Export .ipynb file to others formats
    :return: File in other formats
    """
    # Import Packages
    import os
    import datetime

    # Data
    timestamp = datetime.datetime.now()
    srt_today = (str(timestamp.year) + '-' +
                 str(f"{timestamp.month:02d}") + '-' +
                 str(f"{timestamp.day:02d}"))

    import os
    filter = "['remove_cell']"
    options = ('--TagRemovePreprocessor.enabled=True '
               '--ClearOutputPreprocessor.enabled=True '
               '--TemplateExporter.exclude_markdown=False '
               '--TemplateExporter.exclude_code_cell=True '
               '--TemplateExporter.exclude_output=True '
               '--TemplateExporter.exclude_raw=False '
               '--TemplateExporter.exclude_input_prompt=True '
               '--TagRemovePreprocessor.remove_cell_tags="' + filter + '" ')

    # Extensions
    for extension in extensions:
        if today == True:
            command = ('jupyter nbconvert {} --to {} {} --output {}'.
                       format(filename,
                              extension,
                              options,
                              os.path.join(path, srt_today + '-' + filename.split('.')[0])))
            # print(command)
            os.system(command)
            print('Arquivo {} exportado corretamente para o formato {} usando prefixo da data.'.
                  format(filename, extension))

        else:
            command = ('jupyter nbconvert {} --to {} {} --output {}'.
                       format(filename,
                              extension,
                              options,
                              os.path.join(path, filename.split('.')[0])))
            # print(command)
            os.system(command)
            print('Arquivo {} exportado corretamente para o formato {} sem usar prefixo da data.'.
                  format(filename, extension))

```

```python
# export_jupyter(ipynb_filename, 'docs', ['html', 'markdown', 'pdf', 'python'], False)
```

## Exportar para Word (*.doc*)


Usando [**Pandoc**](https://pandoc.org/) descobri que é possível exportar para ***.doc***.
Em tentativos, notei alguns problemas de incompatibilidade, mas pode auxiliar em algum momento.

```python
ipynb_filename = 'jupyter.ipynb'

file_wo_ext = ipynb_filename.split('.')[0]
file_md = file_wo_ext + '.md'
file_doc = file_wo_ext + '.docx'

file_doc = os.path.join('docs', file_doc)
file_md = os.path.join('docs', file_md)
```

```python
!pandoc - o $file_doc - f
markdown - t
docx $file_md - -reference - links
```

<br>


# GitHub


Diversos projetos que tenho feito, com *scripts* do *Jupyter Notebook*, estão listados no *GitHub*. Alguns destes *
scripts* são, também, publicações no [meu site pessoal](https://michelmetran.github.io/), o qual também está hospedado
no *GitHub*.

Dessa maneira, busquei fazer com que os comandos para atualização dos repositórios já constassem dentro dos *scripts*,
de modo que modificações e ajustes fossem facilmente compartilhados. Ainda, como alguns *scripts* dão origem a *posts*
em meu site, estes também são atualizados.

<br>


## *NbStripout*


Inicialmente compreendi que é considerada como *best pratices* no *git* de projetos escritos em *Jupyter Notebook* a
aplicação de um determinado código usando o package *nbstripout*, para "limpar o cache" do arquivo. No *post* [*How to
Git Jupyter Notebooks the Right Way*](http://mateos.io/blog/jupyter-notebook-in-git) e no vídeo [*nbstripout: strip
output from Jupyter and IPython notebooks*](https://www.youtube.com/watch?v=BEMP4xacrVc) é explicado detalhadamente o
funcionamento.

```python
!nbstripout - -install - -attributes.gitattributes
```

## *Git* de linha de comando


Basta atualizar o repositório com os comandos do *git* usualmente aplicados na linha de comando. Quando se deseja rodar
comandos da linha decomando dentro de um *Jupyter Notebook*, basta adicionar o ponto de exclamação no início do comando.

**Atualmente é a minha solução preferida**, mas testei algumas outras anteriormente, conforme será demonstrado abaixo.
Fiz essa opção pois acho mais prático utilizar os comandos "originais" do *git*, para manusear os repositórios, e me dá
a flexibilidade de me familharizar com os comandos para usar em outros projetos que não envolvam python (e integrações).

```python
!git
status
!git
add.
!git
commit - m

# Atualização do repositório
!git
push
```

## Integrações do *Git*  com *Python*


Existem diversos módulos para promover a integração do git e python. Dentre elas destaca-se o
pacote [GitPython](https://gitpython.readthedocs.io/), porém existem outros. Muito foi discutido no *post* [***Python
Git Module experiences?***](https://stackoverflow.com/questions/1456269/python-git-module-experiences). Testei algumas
delas mas preferi dedicar tempo a aprender outras coisas.


## Funções e *Subprocess*


Criei uma função, utilizando o *subprocess*, para exportar o *Jupyter Notebook* em diversos formatos. Aproveitei para
incorporar o comando do ```nbstripout``` na função que faz o *commit*, visando simplificar as coisas. Com o tempo
abandonei o uso, por não gostava dos *logs do outputs*.

```python
# %load '../codes/git/update_github.py'
import subprocess


def git_add(repo, files):
    cmd = 'git add ' + files
    pipe = subprocess.Popen(cmd, shell=True, cwd=repo, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    (out, error) = pipe.communicate()
    print(out, error)
    pipe.wait()
    return


def git_commit(repo, msg):
    cmd = 'git commit -am "%s"' % msg
    pipe = subprocess.Popen(cmd, shell=True, cwd=repo, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    (out, error) = pipe.communicate()
    print(out, error)
    pipe.wait()
    return


def git_push(repo):
    cmd = 'git push '
    pipe = subprocess.Popen(cmd, shell=True, cwd=repo, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    (out, error) = pipe.communicate()
    print(out, error)
    pipe.wait()
    return


def git_full(repo, files, msg):
    # Strip Out
    import os
    os.system('nbstripout --install --attributes .gitattributes')

    # Function to comit
    git_add(repo, files)
    git_commit(repo, msg)
    git_push(repo)
    print('Done!!')
    return

```

# Erros


Em uma tentativa de exportar o *Jupyter Notebook* para PDF tive problemas. O arquivo não era exportado e apresentava a
seguinte mensagem de erro:

- *nbconvert failed: xelatex not found on PATH, if you have not installed xelatex you may need to do so. Find further
  instructions at https://nbconvert.readthedocs.io/en/latest/install.html#installing-tex.*

Para solucionar, descobri que é necessário instalar, no Linux, akguns pacotes de aplicativos com os seguintes comandos,
sendo o primeiro uma instalação mais compacta e o segundo uma instalação completa.

```sudo apt-get install texlive-xetex texlive-fonts-recommended texlive-generic-recommended```

```sudo apt-get install texlive-full```


# Referêcias


Há muita informação na internet sobre funcionalidades do *Jupyter Notebook*. Apenas para exemplificar, usei
particialmente algumas das funções e truques apresentados em [**Jupyter Notebook
Extensions**](https://towardsdatascience.com/jupyter-notebook-extensions-517fa69d2231) e [**28 Jupyter Notebook Tips,
Tricks, and Shortcuts**](https://www.dataquest.io/blog/jupyter-notebook-tips-tricks-shortcuts).
