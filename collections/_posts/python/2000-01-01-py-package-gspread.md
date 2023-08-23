---
title: "GSpread"
excerpt_separator: "<!--more-->"
tags: [python, pycharm, jupyter, package, gspread]
---

O <a title="Link do GSpread" href="https://gspread.readthedocs.io/en/latest/api.html" target="_blank">**_GSpread_**</a> é um pacote que possibilita a edição e obtenção de dados das planilhas do _Google SpreadSheet_, utilizando _Python_. Ou seja, é possível manipular os dados utiliznado toda uma variedade de _packages_ do _Python_ e inseri-los em _Google Spreadsheets_.

<!--more-->

Outro pacote relevante para trabalhar junto é o <a title="Link do df2gspread" href="https://df2gspread.readthedocs.io/en/latest/index.html" target="_blank">**_df2gspread_**</a>, que lê a tabela no formado do **_Pandas_**.

<br>

{: .box-warning}
**Aviso:** Esse _post_ tem a finalidade de mostrar os comandos básicos e me deixar com uma "cola" rápida para meu uso cotidiano. Todas os códigos são exemplificativos e podem/devem ser alterados, indicando o nome dos arquivos e diretórios corretamente.

{: .box-note}
**Nota:** É possível acessar esse _post_ em formato <a title="Link do Folium" href="https://github.com/michelmetran/package_gspread/raw/master/docs/gspread.pdf" target="_blank">**_pdf_**</a>, diretamente por meio do <a title="Link do Repositório" href="https://github.com/michelmetran/package_gspread" target="_blank">**repositório do GitHub**</a> ou ainda, de maneira interativa, usando o [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/michelmetran/package_gspread/master).

<br>

# Importando Bibliotecas

As bibliotecas básicas, ou _packages_, necessárias para criação do mapa são:

- O **_GSpread_**, que é a biblioteca que lê e edita as tabelas do Google;
- O **df2gspread** é uma biblioteca que, junto com o **_GSpread_**, lê e escreve as tabelas no formato do **_Pandas_**.

```python
import gspread
from oauth2client.service_account import ServiceAccountCredentials

from df2gspread import df2gspread as d2g
from df2gspread import gspread2df as g2d
```

<br>

# Autenticando no _Google Spreadsheet_

Códigos necessários para "entrar" em modo de edição de uma planilha, a partir do _python_.

```python
# Escopo Utilizado
scope = ['https://spreadsheets.google.com/feeds']

api_file = 'python-gspread-credentials.json'

# Lê a Credencial para Autenticação
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    os.path.join('..', 'codes/vault', api_file),
    scope)

# Autenticação, de fato
gc = gspread.authorize(credentials)
```

<br>

Escolhe a planilha e aba a ser editada

```python
# Abre a Planilha
wkb = gc.open_by_key('1bRwjoieInaRkmoyvlisMtDi-2kZ-5CvyKEQ2V_Xk1U8')    # Pelo ID da planilha
#wkb = gc.open_by_url('https://docs.google.com/spreadsheets/d/1bRwjoieInaRkmoyvlisMtDi-2kZ-5CvyKEQ2V_Xk1U8/edit#gid=0')    # Pela URL da planilha
#wkb = gc.open('Teste Python')               # Pelo nome da planilha

# Seleciona a primeira página da planilha
wks = wkb.get_worksheet(0)             # Pela ordem, começando com 0
#wks = wkb.worksheet('January')        # Pelo nome da aba
```

<br>

# Escrevendo Dados

## Célula Individual

```python
# Pela notação padrão do Google Spreadshhet
wks.update_acell('A1', 'Dia e Hora')
```

```python
# Pela notação de coordenadas
wks.update_cell(1, 2, 'Bingo!')
```

```python
%run '~/Documents/SourceCode/codes/files/str_today.py'
wks.update_acell('A2', srt_today())
```

<br>

## Conjunto de Células

```python
# Cabeçalho
wks.update_acell('A1', 'Estado')
wks.update_acell('B1', 'Capital')

# Dicionário com os estados e as capitais
capitais = {'Paraíba': 'João Pessoa', 'Santa Catarina': 'Florianópolis', 'São Paulo': 'São Paulo'}

# Contador de colunas e celulas
column = 1
row = 2

for estado, capital in capitais.items():
    # Atualiza a celula 2 da coluna 1 com o nome do estado
    wks.update_cell(row, column, estado)

    # A coluna agora é a B
    column = 2

    # Atualiza a celula 2 da coluna 2 com o nome da capital
    wks.update_cell(row, column, capital)

    # A coluna agora é a A
    column = 1

    # Acrescenta mais um valor no numero da celula
    row += 1
```

```python
# Atualiza um Conjunto de Células iguais
cell_list = wks.range('A1:C7')

for cell in cell_list:
    cell.value = '00'

# Update in batch
wks.update_cells(cell_list)
```

## Arquivo para _Google Spreadsheet_

```python
# Lendo e filtrando dados
empresas = pd.read_csv('data/empresas.xz')
empresas = empresas[empresas['state'] == 'SP']
empresas = empresas[empresas['city'] == 'SANTOS']

empresas.dtypes
```

```python
from df2gspread import df2gspread as d2g

d2g.upload(empresas,
           gfile='1bRwjoieInaRkmoyvlisMtDi-2kZ-5CvyKEQ2V_Xk1U8',
           wks_name='Página1',
           start_cell='A1',
           credentials=credentials,
           col_names=True,
           row_names=False,
           clean=False)
```

```python
wks.title
```

# Lendo Dados

## Célula Individual

```python
# Pega o valor específico de uma célula
val = wks.cell(1,1).value
print(val)
```

```python
val = wks.acell('A3').value
print(val)
```

```python
# Seleciona todos os dados de uma coluna
val = wks.col_values(1)
print(val)
```

```python
# Seleciona todos os dados de uma linha
val = wks.row_values(1)
print(val)
```

```python
# Procurando uma localização específica
cell = wks.find('CENTRO')
print(f'Encontrado na celula {cell.row} coluna {cell.col}')
```

```python
# Gera uma lista de listas
list_of_lists = wks.get_all_values()
list_of_lists
```

## _Google Spreadsheet_ para arquivo

```python
from df2gspread import gspread2df as g2d

tab = g2d.download(gfile='1bRwjoieInaRkmoyvlisMtDi-2kZ-5CvyKEQ2V_Xk1U8',
                   wks_name='Página1',
                   start_cell='A1',
                   credentials=credentials,
                   col_names=True,
                   row_names=False)

tab.head(2)
```

```python
# Lixo, com o df2gspread passou a ser desnecessário esse código
import pandas as pd

data = wks.get_all_values()
#data = wks.get_all_records(empty2zero=False, head=4, default_blank='',allow_underscores_in_numeric_literals=False)
headers = data.pop(0)

tab = pd.DataFrame(data, columns=headers)

tab.head(2)
```

<br>

# Referências

- Toda introdução está em https://www.linkedin.com/pulse/manipulando-planilhas-do-google-usando-python-renan-pessoa
- Um guia de referências https://gspread.readthedocs.io/en/latest/user-guide.html
- https://df2gspread.readthedocs.io/en/latest/index.html

---

<br>

# Exportando o _Juptyter Notebook_ para outros formatos

O arquivo _.ipynb_ pode ser exportado em formatos diversos. Abaixo carrego uma função que escrevi para facilitar o processo de exportação do arquivo em diferentes locais do PC para, posteriormente, atualizar os repositórios contidos no <a title="Link do GitHub" href="https://github.com/michelmetran" target="_blank">_GitHub_</a>.

```python
# %load '~/Documents/SourceCode/codes/files/export_jupyter.py'
def export_jupyter(path, extensions=['html', 'markdown', 'latex', 'pdf', 'python'], today=True):
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

    # Extensions
    for extension in extensions:
        if today==True:
            os.system('jupyter nbconvert --to {} {} --output {}'.
                      format(extension, get_jupyternotebook_name(),
                             os.path.join(path, srt_today+'-'+get_jupyternotebook_name().split('.')[0])))
            print('Arquivo {} exportado corretamente para o formato {} usando prefixo da data.'.
                  format(get_jupyternotebook_name(), extension))

        else:
            os.system('jupyter nbconvert --to {} {} --output {}'.
                      format(extension, get_jupyternotebook_name(),
                             os.path.join(path, get_jupyternotebook_name().split('.')[0])))
            print('Arquivo {} exportado corretamente para o formato {} sem usar prefixo da data.'.
                  format(get_jupyternotebook_name(), extension))

```

```python
# %load '~/Documents/SourceCode/codes/files/get_jupyternotebook_name.py'
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

Com as funções para exportar o _Jupyter Notebook_ e para obter o nome do arquivo _.ipynb_ carregadas, basta exportar o arquivo, inicialmente para a pasta _docs_ dentro do projeto e também, visando atualizar os _posts_ do site, para a respectiva pasta.

```python
export_jupyter('docs',['pdf'], False)
export_jupyter('/home/michel/Documents/SourceCode/michelmetran.github.io/_posts', ['markdown'], True)
```

<br>

# Atualizando Repositório do Projeto e do _site_

Após as exportações dos arquivos nos formatos necessários, basta atualizar o repositório diretamente pelo _Jupyter Notebook_.
Abaixo é atualizado o repositório desse projeto específico, bem como a derivação desse projeto no <a title="Link do Folium" href="https://michelmetran.github.io/" target="_blank">**_site_**</a>.

```python
%run '~/Documents/SourceCode/codes/git/update_github.py'
```

```python
git_full('/home/michel/Documents/SourceCode/package_gspread', '.', 'Atualizando')
git_full('/home/michel/Documents/SourceCode/michelmetran.github.io', '.', 'Atualizando')
```
