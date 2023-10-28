---
title: "Jupyter over SSH"
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
  - pandas
---

Imaginemos a situação: meu PC tem um sistema operacional Ubuntu, no qual uso o arquivos do Jupyter Notebook (\*_.ipynb_) sem qualquer problema de compatibilidade, correto?! A resposta que dou atualmente seria: quase!

Explico: migrei para o Ubuntu após passar nervoso com o Windows e suas diversas complicações e ajustes necessários para fazer coisas simples usando o _python_. No Ubuntu superei muitos entraves que tive no início do aprendizado dessa linguagem de programação. Contudo, ainda assim, existem algumas bibliotecas do _python_ que só funcionam do Windows, por fazerem a integração com softwares restritos ao Sistema Operacional do Bill Gates.

Cito dois deles: ArcGIS e MetaTrader. O primeiro deles é um _software_ nativo para Windows, para trabalhar com geoprocessamento, e que tem uma biblioteca ArcPy. Em segundo lugar, a plataforma MetaTrader, que faz a negociação de ativos na bosla de valores e também conta com uma biblioteca de integração para python. Ambos só funcionam no Windows (ainda que existam gambiarras para sua instalação no Linux).

Portanto, busquei alternativas para conseguir, a partir do meu Ubuntu, rodar essas bibliotecas.

<br>

---

## Protocolo SSH

### SSH no Linux

### SSH no Windows

1. Instalar o OpenSSH na Máquina Virtual
   https://www.youtube.com/watch?v=KLN2bY0dTtQ

<br>

## Alternativa 1: Virtual Machine

1. Usando o Virtual Box, criar uma máquina virtual do Windows.

2. Nessa máquina virtual, instalar o _conda_, sendo recomendado inserir os _paths_ da instalação nas variáveis de ambiente... ou inserir manualmente.

   ```cmd
   C:\ProgramData\Miniconda3\Library\bin\conda.bat
   C:\ProgramData\Miniconda3\Scripts\conda.exe
   C:\ProgramData\Miniconda3\condabin\conda.bat
   ```

3. Criar ambiente do conda

4. Na Máquina Virtual, fazer o redirecionamento de porta

![](https://i.imgur.com/4XibiF2.png)

6. No Host (Ubuntu), dar o comando:

```bash
ssh -vv michel@127.0.0.1 -p 2222
```

Estando no Ubuntu, logado no Windows via SSH, já com o conda instalado também no Windows, acesso meu ambiente:

```
conda activate trade
```

```
jupyter lab --no-browser --port=8888 --notebook-dir=Y:\SourceCode --ip=0.0.0.0
```

Será criado um link.

Basta trocar a porta 8888 por 8889

PS: Abri o Firewall

<br>

---

## Alternativa 2: Acessando Windows na Rede Local

Tenho dois PCs, sendo um com meu Ubuntu e outro com Windows 10. Ambos ficam ligados constantemente.

Primeiro passo é se conectar, via ssh, com o Windows.

```bash
ssh -vv michel@asus-i5
```

Estando no Ubuntu, logado no Windows via SSH, já com o conda instalado também no Windows, acesso meu ambiente:

```bash
conda activate trade
```

Peço para o Jupter Notebook iniciar na porta 8889, em um diretório específico, porém sem o browser!

```bash
jupyter lab --no-browser --port=8888 --notebook-dir=Z:\
```

Após isso, em um outro terminal, dou um _bind_ entre a conexão da máquina remota com a minha máquina local.

```bash
ssh -N -f -L localhost:8080:localhost:8888 michel@asus-i5
```

Após isso, basta copiar o endereço com o token do Jupyter, ajustar a porta, e mandar abrir.

```
To access the notebook, open this file in a browser:
    file:///C:/Users/Michel/AppData/Roaming/jupyter/runtime/nbserver-5536-open.html
Or copy and paste one of these URLs:
    http://localhost:8888/?token=10c872fca0d941183e20d8067a10d31a07b30c4a70e751cd
 or http://127.0.0.1:8888/?token=10c872fca0d941183e20d8067a10d31a07b30c4a70e751cd
```

<br>

## Utilidades

### _Hosts_

No Ubuntu, caso deseje digitar o _hostname_ ao invés do IP (192.168...), basta incluir o IP seguido do hostname no arquivo abaixo

```bash
sudo gedit /etc/hosts
```




<br>

### Unidade de Rede

Havia tentado com "pushd \\asus-i7\geodata\sourcecode", mas recomendaram

```bash
net use Z: \\asus-i7\Codes
```

<br>

---

### Finalizar Processo na Porta

```
lsof -ti:8080 | xargs kill -9
lsof -ti:8888 | xargs kill -9
lsof -ti:8889 | xargs kill -9
```

<br>

---

<br>

## Referências

- https://ljvmiranda921.github.io/notebook/2018/01/31/running-a-jupyter-notebook/
- https://docs.anaconda.com/anaconda/user-guide/tasks/remote-jupyter-notebook/
- https://www.digitalocean.com/community/tutorials/how-to-install-run-connect-to-jupyter-notebook-on-remote-server
