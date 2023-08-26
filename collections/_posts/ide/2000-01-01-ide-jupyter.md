---
title: "IDE: Jupyter Notebook e Jupyter Lab"
date: 2023-05-04T00:00:00-03:00
last_modified_at: 2023-05-04T00:00:00-03:00
excerpt_separator: "<!--more-->"
categories:
  - IT
tags:
  - python
  - pycharm
  - jupyter
  - package
---

O [**Projeto Jupyter**](https://jupyter.org/) existe para desenvolver _software_ de código aberto, padrões abertos e serviços para computação interativa em dezenas de linguagens de programação.

<!--more-->

Um **<a title="Link do Notebook Jupyter" href="https://hub.gke.mybinder.org/user/ipython-ipython-in-depth-6b7gwnpm/notebooks/binder/Index.ipynb" target="_blank">Notebook Jupyter</a>** é um ambiente computacional web para a internet rica para criação de documentos para a plataforma **Jupyter**. O termo _"notebook"_ pode, dependendo do contexto, fazer referência a entidades distintas como **Jupyter** (aplicativo _Web_), **Jupyter Python** (servidor _Web_) ou ao formato de documento para a plataforma.

Um documento **Jupyter Notebook** é estruturado formato JSON, contendo uma lista ordenada de células de entrada/saída que podem conter código, texto (usando **Markdown**), matemática, gráficos e texto enriquecido, geralmente terminando com a extensão _".ipynb"_.

> **[nb_conda](https://github.com/Anaconda-Platform/nb_conda): _provides Conda environment and package access extension from within Jupyter_**

<br>

---

### Conda

Os procedimentos foram adaptados de um vídeo intitulado [YouTube: Conda Enviroments with Jupyter Notebooks Kernels](https://www.youtube.com/watch?v=Ro9l0eapoJU).

Basta instalar o _package_ **nb_conda**...

```bash
conda install jupyter
conda install nb_conda
```

<br>

... ou ainda, criar um ambiente que contenha eles, **sendo essa opção mais recomendada**!

```bash
# Create Enviroments
conda create --name pablocarreira jupyter nb_conda pandas geopandas
```

<br>

---

### _Jupyter Notebook_

Após isso basta inserir o seguinte comando no terminal que um servidor será iniciado e, por meio do navegador, você poderá editar seus arquivos com extensão _.ipynb_.

```bash
jupyter notebook
```

<br>

---

### _Jupyter Lab_

```bash
jupyter lab
```
