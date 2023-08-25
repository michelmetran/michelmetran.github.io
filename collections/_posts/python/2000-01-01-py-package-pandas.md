---
title: "Pandas"
date: 2023-05-04T00:00:00-03:00
last_modified_at: 2023-05-04T00:00:00-03:00

excerpt_separator: "<!--more-->"
tags:
  - python
  - pycharm
  - jupyter
  - package

---

O <a title="Link do Pandas" href="https://pandas.pydata.org/" target="_blank">**_Pandas_**</a> é um pacote que possibilita o manejo dos dados.

<!--more-->

{: .alert .alert-danger}
**Aviso:** Esse _post_ tem a finalidade de mostrar os comandos básicos e me deixar com uma "cola" rápida para meu uso cotidiano. Todas os códigos são exemplificativos e podem/devem ser alterados, indicando o nome dos arquivos e diretórios corretamente.

{: .box-note}
**Nota:** É possível acessar esse _post_ em formato <a title="Link do Folium" href="https://github.com/michelmetran/package_pandas/raw/master/docs/pandas.pdf" target="_blank">**_pdf_**</a>, diretamente por meio do <a title="Link do Repositório" href="https://github.com/michelmetran/package_pandas" target="_blank">**repositório do GitHub**</a> ou ainda, de maneira interativa, usando o [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/michelmetran/package_pandas/master).

<br>

# Pandas

As bibliotecas básicas, ou _packages_, necessárias para criação do mapa são:

- O **_Pandas_**, que tem a missão de trabalhar com dados, criar _subsets_, selecionar e filtros dados e;
- O **_Geopandas_**, que é a biblioteca lê geojson!

```python
import os
import pandas as pd
```

## Ler CSV

```python
tab = pd.read_csv('data/empresas.xz')
tab = tab[tab['state'] == 'SP']
tab = tab[tab['city'] == 'SANTOS']

tab.dtypes
tab.head(2)
```

<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }

</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>situation</th>
      <th>neighborhood</th>
      <th>address</th>
      <th>number</th>
      <th>zip_code</th>
      <th>city</th>
      <th>state</th>
      <th>cnpj</th>
      <th>status</th>
      <th>additional_address_details</th>
      <th>main_activity</th>
      <th>latitude</th>
      <th>longitude</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1108</th>
      <td>ALMEIDA &amp; RODRIGUES MANUTENCAO EM INFORMATICA ...</td>
      <td>ATIVA</td>
      <td>CENTRO</td>
      <td>R AMADOR BUENO</td>
      <td>171</td>
      <td>11.013-151</td>
      <td>SANTOS</td>
      <td>SP</td>
      <td>13.295.386/0001-58</td>
      <td>OK</td>
      <td>SALA 69</td>
      <td>Reparação e manutenção de computadores e de eq...</td>
      <td>-23.935972</td>
      <td>-46.327216</td>
    </tr>
    <tr>
      <th>1534</th>
      <td>MARCIO CESAR FRANCISQUINE SANTOS - ME</td>
      <td>ATIVA</td>
      <td>MARAPE</td>
      <td>AV SENADOR PINHEIRO MACHADO</td>
      <td>856</td>
      <td>11.075-002</td>
      <td>SANTOS</td>
      <td>SP</td>
      <td>18.950.028/0001-55</td>
      <td>OK</td>
      <td>NaN</td>
      <td>Restaurantes e similares</td>
      <td>-23.961729</td>
      <td>-46.345475</td>
    </tr>
  </tbody>
</table>
</div>

## Ler JSON de um arquivo _.json_

```python
tab = pd.read_json(os.path.join('data', 'tab.json'))
```

```python
tab
```

<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }

</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>nome</th>
      <th>microrregiao</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>3500105</td>
      <td>Adamantina</td>
      <td>{'id': 35035, 'nome': 'Adamantina', 'mesorregi...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>3500204</td>
      <td>Adolfo</td>
      <td>{'id': 35004, 'nome': 'São José do Rio Preto',...</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3500303</td>
      <td>Aguaí</td>
      <td>{'id': 35029, 'nome': 'Pirassununga', 'mesorre...</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3500402</td>
      <td>Águas da Prata</td>
      <td>{'id': 35030, 'nome': 'São João da Boa Vista',...</td>
    </tr>
    <tr>
      <th>4</th>
      <td>3500501</td>
      <td>Águas de Lindóia</td>
      <td>{'id': 35033, 'nome': 'Amparo', 'mesorregiao':...</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>640</th>
      <td>3557006</td>
      <td>Votorantim</td>
      <td>{'id': 35046, 'nome': 'Sorocaba', 'mesorregiao...</td>
    </tr>
    <tr>
      <th>641</th>
      <td>3557105</td>
      <td>Votuporanga</td>
      <td>{'id': 35003, 'nome': 'Votuporanga', 'mesorreg...</td>
    </tr>
    <tr>
      <th>642</th>
      <td>3557154</td>
      <td>Zacarias</td>
      <td>{'id': 35004, 'nome': 'São José do Rio Preto',...</td>
    </tr>
    <tr>
      <th>643</th>
      <td>3557204</td>
      <td>Chavantes</td>
      <td>{'id': 35040, 'nome': 'Ourinhos', 'mesorregiao...</td>
    </tr>
    <tr>
      <th>644</th>
      <td>3557303</td>
      <td>Estiva Gerbi</td>
      <td>{'id': 35031, 'nome': 'Mogi Mirim', 'mesorregi...</td>
    </tr>
  </tbody>
</table>
<p>645 rows × 3 columns</p>
</div>

## Ler JSON de um objeto _.json_

```python
#tab = pd.DataFrame(JSON_object)
#tab
```

## Seleciona Linhas (Filtrar dados)

```python
tab = pd.read_csv('data/empresas.xz')
tab = tab[tab['state'] == 'SP']
tab = tab[tab['city'] == 'SANTOS']

# Seleciona com mais de um argumento
#tab = tab[tab['CNPJ_FUNDO'].isin(['00.017.024/0001-53', '00.068.305/0001-35'])]

tab
```

<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }

</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>situation</th>
      <th>neighborhood</th>
      <th>address</th>
      <th>number</th>
      <th>zip_code</th>
      <th>city</th>
      <th>state</th>
      <th>cnpj</th>
      <th>status</th>
      <th>additional_address_details</th>
      <th>main_activity</th>
      <th>latitude</th>
      <th>longitude</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1108</th>
      <td>ALMEIDA &amp; RODRIGUES MANUTENCAO EM INFORMATICA ...</td>
      <td>ATIVA</td>
      <td>CENTRO</td>
      <td>R AMADOR BUENO</td>
      <td>171</td>
      <td>11.013-151</td>
      <td>SANTOS</td>
      <td>SP</td>
      <td>13.295.386/0001-58</td>
      <td>OK</td>
      <td>SALA 69</td>
      <td>Reparação e manutenção de computadores e de eq...</td>
      <td>-23.935972</td>
      <td>-46.327216</td>
    </tr>
    <tr>
      <th>1534</th>
      <td>MARCIO CESAR FRANCISQUINE SANTOS - ME</td>
      <td>ATIVA</td>
      <td>MARAPE</td>
      <td>AV SENADOR PINHEIRO MACHADO</td>
      <td>856</td>
      <td>11.075-002</td>
      <td>SANTOS</td>
      <td>SP</td>
      <td>18.950.028/0001-55</td>
      <td>OK</td>
      <td>NaN</td>
      <td>Restaurantes e similares</td>
      <td>-23.961729</td>
      <td>-46.345475</td>
    </tr>
    <tr>
      <th>1777</th>
      <td>R P LOPES FONSECA</td>
      <td>ATIVA</td>
      <td>PONTA DA PRAIA</td>
      <td>PC CORACAO DE MARIA</td>
      <td>23</td>
      <td>11.030-280</td>
      <td>SANTOS</td>
      <td>SP</td>
      <td>58.132.036/0001-09</td>
      <td>OK</td>
      <td>NaN</td>
      <td>Comércio varejista de combustíveis para veícul...</td>
      <td>-23.986863</td>
      <td>-46.303085</td>
    </tr>
    <tr>
      <th>2516</th>
      <td>AUTO POSTO NOVO MILENIO LTDA</td>
      <td>ATIVA</td>
      <td>MACUCO</td>
      <td>R CONSELHEIRO RODRIGUES ALVES</td>
      <td>385</td>
      <td>11.015-203</td>
      <td>SANTOS</td>
      <td>SP</td>
      <td>03.542.311/0001-70</td>
      <td>OK</td>
      <td>NaN</td>
      <td>Comércio varejista de combustíveis para veícul...</td>
      <td>-23.956003</td>
      <td>-46.321556</td>
    </tr>
    <tr>
      <th>2914</th>
      <td>CHURRASCARIA E PIZZARIA MAXIM'S LTDA - ME</td>
      <td>ATIVA</td>
      <td>BOQUEIRAO</td>
      <td>AV CONSELHEIRO NEBIAS</td>
      <td>656</td>
      <td>11.045-002</td>
      <td>SANTOS</td>
      <td>SP</td>
      <td>19.396.916/0001-30</td>
      <td>OK</td>
      <td>NaN</td>
      <td>Restaurantes e similares</td>
      <td>-23.962879</td>
      <td>-46.323743</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>54034</th>
      <td>POST &amp; OFFICE - SERVICOS TELEMATICOS LTDA - EPP</td>
      <td>ATIVA</td>
      <td>PONTA DA PRAIA</td>
      <td>R VEREADOR HENRIQUE SOLER</td>
      <td>295</td>
      <td>11.030-011</td>
      <td>SANTOS</td>
      <td>SP</td>
      <td>68.015.478/0001-29</td>
      <td>OK</td>
      <td>NaN</td>
      <td>Atividades de franqueadas do Correio Nacional</td>
      <td>-23.984730</td>
      <td>-46.295672</td>
    </tr>
    <tr>
      <th>54105</th>
      <td>MARE MANSA RESTAURANTE E CHOPERIA LTDA - EPP</td>
      <td>ATIVA</td>
      <td>GONZAGA</td>
      <td>AV PRESIDENTE WILSON</td>
      <td>9</td>
      <td>11.065-200</td>
      <td>SANTOS</td>
      <td>SP</td>
      <td>68.965.946/0001-26</td>
      <td>OK</td>
      <td>NaN</td>
      <td>Restaurantes e similares</td>
      <td>-23.969259</td>
      <td>-46.334143</td>
    </tr>
    <tr>
      <th>54266</th>
      <td>PORTEMAR SERVICOS LTDA.</td>
      <td>ATIVA</td>
      <td>GONZAGA</td>
      <td>AV DONA ANA COSTA</td>
      <td>470</td>
      <td>11.060-002</td>
      <td>SANTOS</td>
      <td>SP</td>
      <td>71.545.305/0001-27</td>
      <td>OK</td>
      <td>NaN</td>
      <td>Atividades de franqueadas do Correio Nacional</td>
      <td>-23.965090</td>
      <td>-46.332675</td>
    </tr>
    <tr>
      <th>54389</th>
      <td>VAN GOGH CHOPERIA &amp; PIZZARIA LTDA</td>
      <td>ATIVA</td>
      <td>JOSE MENINO</td>
      <td>AV MAL FLORIANO PEIXOTO</td>
      <td>314</td>
      <td>11.060-302</td>
      <td>SANTOS</td>
      <td>SP</td>
      <td>72.810.443/0001-59</td>
      <td>OK</td>
      <td>NaN</td>
      <td>Restaurantes e similares</td>
      <td>-23.965837</td>
      <td>-46.345120</td>
    </tr>
    <tr>
      <th>57396</th>
      <td>PARK &amp; WASH COMERCIO E GARAGEM LTDA - ME</td>
      <td>ATIVA</td>
      <td>GONZAGA</td>
      <td>R MARCILIO DIAS</td>
      <td>18/24</td>
      <td>11.060-210</td>
      <td>SANTOS</td>
      <td>SP</td>
      <td>49.189.905/0001-40</td>
      <td>OK</td>
      <td>NaN</td>
      <td>Outras atividades de serviços pessoais não esp...</td>
      <td>-23.967715</td>
      <td>-46.334064</td>
    </tr>
  </tbody>
</table>
<p>145 rows × 14 columns</p>
</div>

## Seleciona Colunas

```python
tab = pd.read_csv('data/empresas.xz')

# Exclui coluna pela posição
#tab.drop(tab.columns[[0, 2]], axis=1, inplace=True)

# Exclui coluna pelo Nome
tab = tab.drop(['state', 'longitude'], axis=1)

# Mantem apenas a que vc quer
#tab = tab[['cnpj','latitude']]

tab
```

<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }

</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>situation</th>
      <th>neighborhood</th>
      <th>address</th>
      <th>number</th>
      <th>zip_code</th>
      <th>city</th>
      <th>cnpj</th>
      <th>status</th>
      <th>additional_address_details</th>
      <th>main_activity</th>
      <th>latitude</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>COMPANHIA DE AGUAS E ESGOTOS DE RORAIMA CAER</td>
      <td>ATIVA</td>
      <td>SAO PEDRO</td>
      <td>R MELVIN JONES</td>
      <td>219</td>
      <td>69.306-610</td>
      <td>BOA VISTA</td>
      <td>05.939.467/0001-15</td>
      <td>OK</td>
      <td>NaN</td>
      <td>Captação, tratamento e distribuição de água</td>
      <td>2.827880</td>
    </tr>
    <tr>
      <th>1</th>
      <td>MG TERMINAIS RODOVIARIOS LTDA.</td>
      <td>ATIVA</td>
      <td>CENTRO</td>
      <td>R ERNESTO ALVES</td>
      <td>1341</td>
      <td>95.020-360</td>
      <td>CAXIAS DO SUL</td>
      <td>16.571.066/0001-71</td>
      <td>OK</td>
      <td>SALA 2 BLOCO 1 SLJ</td>
      <td>Terminais rodoviários e ferroviários</td>
      <td>-29.163731</td>
    </tr>
    <tr>
      <th>2</th>
      <td>POSTO ROTA 116 DERIVADOS DE PETROLEO LTDA</td>
      <td>ATIVA</td>
      <td>PRIMAVERA</td>
      <td>R LATERAL A RODOVIA BR 116</td>
      <td>S/N</td>
      <td>93.950-000</td>
      <td>DOIS IRMAOS</td>
      <td>07.069.926/0001-82</td>
      <td>OK</td>
      <td>KM 222,6</td>
      <td>Comércio varejista de combustíveis para veícul...</td>
      <td>-29.585206</td>
    </tr>
    <tr>
      <th>3</th>
      <td>POSTO VIA ESTRUTURAL COMERCIO DE DERIVADOS DE ...</td>
      <td>ATIVA</td>
      <td>GUARA</td>
      <td>SIA TRECHO</td>
      <td>01</td>
      <td>71.200-010</td>
      <td>BRASILIA</td>
      <td>05.246.123/0001-20</td>
      <td>OK</td>
      <td>LOTES 30 E 40</td>
      <td>Comércio varejista de combustíveis para veícul...</td>
      <td>-15.791097</td>
    </tr>
    <tr>
      <th>4</th>
      <td>FREDERICO DE CARVALHO ALVES GRAFICA - ME</td>
      <td>ATIVA</td>
      <td>VILA MURY</td>
      <td>AV DO COMERCIO</td>
      <td>225</td>
      <td>27.211-130</td>
      <td>VOLTA REDONDA</td>
      <td>04.606.157/0001-16</td>
      <td>OK</td>
      <td>NaN</td>
      <td>Serviços de acabamentos gráficos, exceto encad...</td>
      <td>-22.501202</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>57638</th>
      <td>SILVEIRA COMERCIO DE ALIMENTOS LTDA</td>
      <td>ATIVA</td>
      <td>CAPUAVA</td>
      <td>R OURO PRETO</td>
      <td>1117</td>
      <td>74.450-170</td>
      <td>GOIANIA</td>
      <td>02.575.277/0001-78</td>
      <td>OK</td>
      <td>QUADRA: 53; LOTE: 18;</td>
      <td>Preparação de documentos e serviços especializ...</td>
      <td>-16.655991</td>
    </tr>
    <tr>
      <th>57639</th>
      <td>LOGINEP - LOGISTICA, SERVICOS E COMERCIO DE PE...</td>
      <td>ATIVA</td>
      <td>ZONA RURAL</td>
      <td>ROD FERNAO DIAS - BR 381</td>
      <td>S/N</td>
      <td>37.264-000</td>
      <td>RIBEIRAO VERMELHO</td>
      <td>03.339.368/0002-58</td>
      <td>OK</td>
      <td>KM 674,9</td>
      <td>Comércio varejista de combustíveis para veícul...</td>
      <td>-21.188346</td>
    </tr>
    <tr>
      <th>57640</th>
      <td>INTERNATIONAL MEAL COMPANY ALIMENTACAO S.A.</td>
      <td>ATIVA</td>
      <td>AEROPORTO INTERNACIONAL</td>
      <td>ST AEROPORTO INTERNACIONAL DE BRASILIA PRESIDE...</td>
      <td>SN</td>
      <td>71.608-900</td>
      <td>BRASILIA</td>
      <td>17.314.329/0026-88</td>
      <td>OK</td>
      <td>PISO DE DESEMBARQUE AREA 22</td>
      <td>Restaurantes e similares</td>
      <td>-15.799765</td>
    </tr>
    <tr>
      <th>57641</th>
      <td>JOSE MARCOS MOREIRA - ME</td>
      <td>ATIVA</td>
      <td>CENTRO</td>
      <td>R GERALDO SANTOS</td>
      <td>107</td>
      <td>98.130-000</td>
      <td>JULIO DE CASTILHOS</td>
      <td>22.103.490/0001-94</td>
      <td>OK</td>
      <td>NaN</td>
      <td>Restaurantes e similares</td>
      <td>-29.231695</td>
    </tr>
    <tr>
      <th>57642</th>
      <td>SINDICATO DOS CONDUTORES AUTONOMOS DE TAXI DE ...</td>
      <td>ATIVA</td>
      <td>SAO JOAO</td>
      <td>R AUSTERGILIO ANGELINO</td>
      <td>100</td>
      <td>88.305-040</td>
      <td>ITAJAI</td>
      <td>72.337.371/0001-74</td>
      <td>OK</td>
      <td>NaN</td>
      <td>Atividades de organizações sindicais</td>
      <td>-26.898554</td>
    </tr>
  </tbody>
</table>
<p>57643 rows × 12 columns</p>
</div>

## Renomeia Colunas

```python
tab.columns = [x.lower() for x in tab.columns]                # Para tudo para Minúsculas
tab.columns = [x.upper() for x in tab.columns]                # Para tudo para Maiúscula
tab = tab.rename(columns=lambda x: x.replace('nome', 'zzz'))  # Renomear de uma coisa por outra

# Remove espaços em branco de uma determinada coluna
tab['neighborhood'] = tab['neighborhood'].str.strip()
```

    ---------------------------------------------------------------------------

    KeyError                                  Traceback (most recent call last)

    ~/miniconda/envs/pablocarreira-py36/lib/python3.6/site-packages/pandas/core/indexes/base.py in get_loc(self, key, method, tolerance)
       2896             try:
    -> 2897                 return self._engine.get_loc(key)
       2898             except KeyError:


    pandas/_libs/index.pyx in pandas._libs.index.IndexEngine.get_loc()


    pandas/_libs/index.pyx in pandas._libs.index.IndexEngine.get_loc()


    pandas/_libs/hashtable_class_helper.pxi in pandas._libs.hashtable.PyObjectHashTable.get_item()


    pandas/_libs/hashtable_class_helper.pxi in pandas._libs.hashtable.PyObjectHashTable.get_item()


    KeyError: 'neighborhood'

During handling of the above exception, another exception occurred:

    KeyError                                  Traceback (most recent call last)

    <ipython-input-19-6cc4e27805a5> in <module>
          4
          5 # Remove espaços em branco de uma determinada coluna
    ----> 6 tab['neighborhood'] = tab['neighborhood'].str.strip()


    ~/miniconda/envs/pablocarreira-py36/lib/python3.6/site-packages/pandas/core/frame.py in __getitem__(self, key)
       2993             if self.columns.nlevels > 1:
       2994                 return self._getitem_multilevel(key)
    -> 2995             indexer = self.columns.get_loc(key)
       2996             if is_integer(indexer):
       2997                 indexer = [indexer]


    ~/miniconda/envs/pablocarreira-py36/lib/python3.6/site-packages/pandas/core/indexes/base.py in get_loc(self, key, method, tolerance)
       2897                 return self._engine.get_loc(key)
       2898             except KeyError:
    -> 2899                 return self._engine.get_loc(self._maybe_cast_indexer(key))
       2900         indexer = self.get_indexer([key], method=method, tolerance=tolerance)
       2901         if indexer.ndim > 1 or indexer.size > 1:


    pandas/_libs/index.pyx in pandas._libs.index.IndexEngine.get_loc()


    pandas/_libs/index.pyx in pandas._libs.index.IndexEngine.get_loc()


    pandas/_libs/hashtable_class_helper.pxi in pandas._libs.hashtable.PyObjectHashTable.get_item()


    pandas/_libs/hashtable_class_helper.pxi in pandas._libs.hashtable.PyObjectHashTable.get_item()


    KeyError: 'neighborhood'

## Cria Colunas

```python
tab['cosunt'] = 'a'
tab
```

## Descritivo da Tabela

```python
tab = pd.read_csv('data/empresas.xz')
tab = tab[tab['state'] == 'SP']
tab = tab[tab['city'] == 'SANTOS']
```

```python
# Quantos registros tem por coluna
tab.count()
```

```python
# Tipos das colunas
tab.dtypes
```

```python
# Início da Tabela
tab.head(3)
```

```python
# Descrição de parâmetros básicos apenas dos campos numéricos
tab.describe()
```

# GeoPandas

```python
import geopandas as gpd
#https://rsandstroem.github.io/GeoMapsFoliumDemo.html
#https://michelleful.github.io/code-blog/2015/04/29/geopandas-manipulation/
```

# OS

Ainda segue uns comandas básicos para 'andar' entre pastas e arquivos.

```python
import os

# Pasta Atual
print(os.getcwd())

# Altera a pasta para um nível acima
os.chdir('/home/michel/Documents/SourceCode/michelmetran.github.io')
os.chdir('/home/michel/Documents/SourceCode/package_pandas')

# dd
print(os.path.expanduser('~'))

# Confere a pasta
print(os.getcwd())

#from importlib import reload
#reload(os)
```

```python
os.path.dirname('/home/michel/Documents/SourceCode/package_pandas/pandas.ipynb')
```

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

# Atualizando Repositórios

Após as exportações dos arquivos nos formatos necessários, basta atualizar o repositório diretamente pelo _Jupyter Notebook_.
Abaixo é atualizado o repositório desse projeto específico, bem como a derivação desse projeto no <a title="Link do Folium" href="https://michelmetran.github.io/" target="_blank">**_site_**</a>.

```python
%run '~/Documents/SourceCode/codes/git/update_github.py'
```

```python
git_full('/home/michel/Documents/SourceCode/package_pandas', '.', 'Atualizando')
git_full('/home/michel/Documents/SourceCode/michelmetran.github.io', '.', 'Atualizando')
```

# _Requirements_

Abaixo é criado o arquivo _requirements.txt_ na raiz do projeto para possibilitar o correto funcionamento do _Jupyter Notebook_ no <a title="Link do My Binder" href="https://mybinder.org/" target="_blank">**_My Binder_**</a>. Após a criação do arquivo, sugere-se a edição manual, visando manter apenas os _packages_ realmente essenciais, listados com o comando _import_ no início do _script_.

```python
#pip freeze > requirements.txt
```
