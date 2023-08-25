---
title: 'Oracle Linux'
date: 2023-05-21T15:00:00-03:00
last_modified_at: 2023-05-21T15:00:00-03:00
excerpt_separator: '<!--more-->'
categories:
  - IT

tags:
  - python
  - pycharm
  - jupyter
  - package
  - pandas
---

Em 20.05.2023 criei instâncias na oracle Cloud, gratuitamente. Uma das instâncias que criei utiliza como Sistema Operacional o [Oracle Linux](https://www.oracle.com/linux/).

Toda a documentação pode ser encontrada [aqui](https://docs.oracle.com/en/operating-systems/oracle-linux/9/)

As distribuições do Fedora, RHEL e Oracle Linux tem dois gerenciadores de pacote:

1. yum
2. dnf

<br>

Pelo que vi na publicação [Diferenças entre DNF e o YUM (Gerenciador de pacotes do Fedora) ](https://marcomapa.com/artigos/?p=1009), o `yum` é mais atual e, portanto, dar preferência a ele.

```bash
# Atualiza aplicativos
sudo yum upgrade
sudo dnf upgrade

# Instala o git
sudo yum install git
sudo dnf install git
```

<br>

---

## SSH Agent

Ao tentar adicionar chaves do _git_ na instância, recebia a seguinte mensagem

> Could not open a connection to your authentication agent

<br>

Lendo a dúvida [Could not open a connection to your authentication agent](https://stackoverflow.com/questions/17846529/could-not-open-a-connection-to-your-authentication-agent), resolvi. Basta dar o comando:

```bash
# Para iniciar o Agent
eval `ssh-agent -s`

# Para adicionar chaves
ssh-add
```
