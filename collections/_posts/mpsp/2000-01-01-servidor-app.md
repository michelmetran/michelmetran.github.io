---
title: 'Servidor de Aplicação'
excerpt_separator: '<!--more-->'
date: 2023-04-26T00:00:00-03:00
last_modified_at: 2023-04-26T00:00:00-03:00
categories:
  - Hacks
tags:
  - ssh
---

Um servidor de aplicação é um software que fornece um ambiente de execução para aplicativos de negócios baseados em servidor. Ele é responsável por gerenciar e disponibilizar recursos para as aplicações, como memória, processamento e conexões de rede. O servidor de aplicação também gerencia a comunicação entre as aplicações e outras partes do sistema, como bancos de dados e servidores de arquivos.

Um servidor de aplicação pode ser executado em uma variedade de plataformas, incluindo sistemas operacionais como Windows, Linux e macOS. Eles são usados em ambientes corporativos para hospedar aplicativos web, aplicativos de negócios, serviços de mensagens, entre outros. Com a crescente demanda por aplicações de alta qualidade e alta disponibilidade, os servidores de aplicação têm se tornado uma peça fundamental da infraestrutura de TI de muitas empresas.

<br>

---

Para se conectar ao servidor de aplicação utilizei, inicialmente, usuário e senha. A cada operação era necessário digitar a senha, o que causava um trantorno. **Para contornar isso, decidi fazer o acesso por meio de par de chaves.** Abaixo apresento os passos para fazer isso.

<br>

1. Inicialmente eu crio o par de chaves no PC local.

```powershell
ssh-keygen -t rsa -C "{email@domain.com}"
```

<br>

2. Usando o protocolo **SCP** (_Secure Copy Protocol_), copio a chave pública que acabei de criar para o servidor de aplicação. Será solicitada a senha.

```powershell
scp .ssh/id_rsa.pub {username@domain.com}:
```

<br>

3. Uma vez logado no servidor de aplicação, ainda usando usuário e senha, criar o arquivo _authorized_keys_.

```powershell
# Logar no Servidor de Aplicação
ssh {username@domain.com}

# Criar arquivo "authorized_keys"
touch ~/.ssh/authorized_keys
```

<br>

4. E, considerando que a chave pública recem copiada está na raiz do usuário, copie o conteudo da chave pública para o arquivo _authorized_keys_.

```powershell
# Copia Conteúdo
cat ~/id_rsa.pub >> ~/.ssh/authorized_keys

# Exclui Chave
rm ~/id_rsa.pub
```

<br>

... e, é isso...\
... ou, deveria ser...

<br>

5. Na tentativa de acesso ao servidor de aplicação usando o par de chaves, passei a receber a seguinte mensagem

```powershell
debug1: Remote: Ignored authorized keys: bad ownership or modes for file /home/{username}/.ssh/authorized_keys
```

<br>

Sabia que o problema estava relacionado às permissões do arquivo. Lendo o artigo [SSH Authentication Refused: Bad Ownership or Modes for Directory](https://chemicloud.com/kb/article/ssh-authentication-refused-bad-ownership-or-modes-for-directory/) consegui corrigir o problema com os comandos abaixo

```powershell
# Ajustei os erros
chmod 700 /home/{username}/.ssh
chmod 600 /home/{username}/.ssh/authorized_keys
```

<br>

6. Por fim consegui me logar ao servidor de aplicação com sucesso, usando o par de chaves!

<br>

---

### Referências

- [Set up SSH public key authentication to connect to a remote system](https://kb.iu.edu/d/aews)
