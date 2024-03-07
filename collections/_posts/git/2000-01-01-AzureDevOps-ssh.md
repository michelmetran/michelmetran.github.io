---
title: "Azure DevOps: ssh"
date: 2023-04-25T00:00:00-03:00
last_modified_at: 2023-10-04T00:00:00-03:00
excerpt_separator: "<!--more-->"
categories:
  - IT
  - Hacks
tags:
  - AzureDevOps
  - git
  - ssh
---

Assim como no GitHub, no Azure DevOps existem dois protocolos possíveis para se manejar (_push_/_pull_) os repositórios:

- SSH
- HTTPs

<br>

No GitHub é possível [usar SSH na porta HTTPS](https://docs.github.com/pt/authentication/troubleshooting-ssh/using-ssh-over-the-https-port), ou seja, através do protocolo SSH (que utiliza a porta 22), alternar para a porta 443! Essa possibilidade é excelente para superar bloqueios de _firewalls_ corporativos.

Contudo, o AzureDevOps não conta com essa possibilidade, sendo necessário usar o SSH na porta 22 ou HTTPs na porta 443 e fim de papo. Considerando que o _firewall_ corporativo me bloqueia na porta 22, não me resta outra opção a não ser usar a porta 443, ou seja, protocolo HTTPS!

Para fins de teste, seguem dois comandos para testar o SSH na porta 22. Veja a diferença de resultados entre o GitHub e o AzureDevOps.

```powershell
# GitHub
ssh -T -p 443 git@ssh.github.com

# AzureDevOps
ssh -T -p 443 git@ssh.dev.azure.com
```

<br>

Quando utilizamos o protocolo HTTPs perdemos a praticidade e segurança proporcionada pelo _ssh-agent_ e faz-se necessário buscar alternativas.

<br>

---

## Senha _versus_ PAT

Importante destacar que ao optar pelo protocolo HTTPs, é necessário o uso de senha. Contudo, a "senha" que o AzureDevOps usa não é a senha do usuário. Trata-se, na realidade, de um _Personal Access Token_ (PAT). Para mais informações sobre a gestão dos PATs, ler o artigo [_Learn:_ **Use personal access tokens**](https://learn.microsoft.com/en-us/azure/devops/organizations/accounts/use-personal-access-tokens-to-authenticate?view=azure-devops&tabs=Windows)

![](https://i.imgur.com/iFKch7Y.png)

<br>

---

## Git Manager Credentials

O Git Manager Credentials é um recurso que permite aos usuários armazenar suas credenciais de _login_ do Git em um local seguro e confiável. Com o [_Git Manager Credentials_](https://github.com/git-ecosystem/git-credential-manager), os usuários não precisam inserir suas credenciais de _login_ toda vez que se conectam a um repositório Git remoto.

Em vez disso, as credenciais são armazenadas em um arquivo de configuração localizado em um diretório específico. Isso torna mais fácil para os usuários gerenciarem suas credenciais de _login_ do Git, ao mesmo tempo em que mantêm suas informações seguras e protegidas.

Para ver se o Git Manager Credentials está instalado basta dar o seguitnte comando:

```powershell
# Avaliar se o programa está instalado
git credential-manager
```

<br>

No artigo [git-credential-manager/credstores](https://github.com/git-ecosystem/git-credential-manager/blob/main/docs/credstores.md) descobri que eu poderia definir onde guardar as chaves.

```powershell
# Define que o password está em um arquivo
git config --global credential.credentialStore plaintext

# Define que o password é cached
git config --global credential.cacheOptions "--timeout 300"
```

<br>

Apesar de interessante, eu não tenho permissão para instalar o _Git Manager Credentials_, para explorar outras possibilidades para armazenamento seguro da senha.

Apenas para complementar, descobri alguns comandos lendo o _post_ [How to fix duplicate account in git credential manager](https://stackoverflow.com/questions/76706515/how-to-fix-duplicate-account-in-git-credential-manager) quando eu passei a ter dois _logins_ habilitados no _git credential-manager_. Curiosamente, um dos _logins_ era um número! e eu desconfiava que tratava-se do _id_ do meu perfil no _github_. Acessando a [API do GitHub](https://api.github.com/users/michelmetran), esclareci que era, de fato, o *id* do meu GitHub.

```shell
# Lista Credenciais que estão no git credential-manager
git credential-manager github list

# Faz logout em um perfil
git credential-manager github logout 10374538
```

<br>

---

## Git Tools Credential Storage

O [Git Tools Credential Storage](https://git-scm.com/book/en/v2/Git-Tools-Credential-Storage) é um conjunto de **ferramentas nativas do Git** que permitem aos usuários gerenciar suas credenciais de _login_ do Git. Essas ferramentas são projetadas para armazenar de forma segura e confiável as informações de autenticação do usuário, incluindo nome de usuário e senha. O Git Tools Credential Storage fornece várias opções de armazenamento, como o armazenamento em cache, que armazena temporariamente as credenciais em memória ou em disco, e o armazenamento em arquivo, que armazena as credenciais em um arquivo seguro no disco.

```powershell
# Define que o password está em um arquivo
git config --global credential.helper 'store --file ~/.my-credentials'

# Define que o password é cached (padrão 15 min)
git config --global credential.helper cache

# Define que o password é cached (um ano)
git config --global credential.helper 'cache --timeout 31536000'
```

<br>

A grande vantagem é que essa opção está no conjunto de ferramentas nativas, não sendo necessário instalar nenhum pacote extra!

<br>

---

## Referências

- [Git Credential Management with Gnome Passwords and Keys (Seahorse) in Fedora Linux](https://kasunc.medium.com/git-credential-management-with-gnome-passwords-and-keys-seahorse-in-linux-e7b59b3b4d3d)
- [FedoraCopr: MatthickFord/git-credential-manager](https://copr.fedorainfracloud.org/coprs/matthickford/git-credential-manager/)
- [What's the best encrypted git credential helper for Linux?](https://stackoverflow.com/questions/53305965/whats-the-best-encrypted-git-credential-helper-for-linux)
