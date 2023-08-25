---
title: "PostGreSQL"
date: 2019-06-13T15:34:30-04:00
last_modified_at: 2021-07-09T16:20:02-05:00
excerpt_separator: "<!--more-->"
categories:
   -IT
  - Database
tags:
  - database
  - postgre
  - sql
---

O [**PostgreSQL**](https://www.postgresql.org/) é o banco de dados tenho mais interesse em aprender devido a extensão [_PostGIS_ (Spatial and Geographic Objects for PostgreSQL)](https://postgis.net/) empregada em análises com dados espaciais.

Aprendi comandos básicos quando estudei Django, e aprendi com mais profundidade durante um curso realizado em junho/2020 com [Daniel Robert Costa](https://github.com/drobcosta), quando então aprofeitei para tomar nota de suas explicações nesse documento.

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

# Comandos Administrativos

Comandos para _PostgreSQL_ instalado via repositórios do Ubuntu

- `pg_lsclusters` lista todos os _clusters PostgreSQL_
- `pg_createcluster {version} {clustername}` lista todos os _clusters PostgreSQL_
- `pg_dropcluster {version} {clustername}` apaga um _cluster PostgreSQL_
- `pg_ctlcluster {version} {clustername} {action}` _Start_, _Stop_, _Status_, _Restart_, _Reload_ do _cluster PostgreSQL_

## Start / Stop

```bash
sudo service postgresql stop
sudo service postgresql start
sudo service postgresql restart
sudo service postgresql status
```

## Inicializar

```bash
sudo -u postgres psql
psql -U postgres
psql -h 127.0.0.1 -p 5432
psql -h 127.0.0.1 -p 5432 -U postgres
psql -h 127.0.0.1 -p 5432 -U {username} {db name}
```

# Comandos para gerenciar _database_

## _Database_

### Cria

```sql
CREATE DATABASE {db name};
CREATE DATABASE django_jobs;
CREATE DATABASE db_escola OWNER univesp;
CREATE DATABASE opentesouro OWNER django;
CREATE DATABASE db_sabesp OWNER postgres;
```

### Deleta

```sql
DROP DATABASE {db name};
DROP DATABASE django_jobs;
DROP DATABASE tesourodireto;
DROP DATABASE db_escola;
```

### Listar

```sql
\l
```

### Conectar

```sql
\c databasename;
\c sabesp;
```

## Schema

### Cria

```sql
CREATE SCHEMA IF NOT EXISTS {schema name}
```

### Deleta

```sql
DROP SCHEMA IF EXISTS {schema name}
```

## Usuários ou Roles

Após a versão 8.1, _users_ e _roles_ são sinônimos e tem as mesmas propriedades.

### Cria

```sql
CREATE USER {username};
CREATE USER django;
CREATE USER michelmetran;
CREATE USER michelmetran WITH PASSWORD '12345';
CREATE USER django WITH PASSWORD '12345';
CREATE ROLE univesp NOCREATEDB NOCREATEROLE INHERIT NOLOGIN NOBYPASSRLS CONNECTION LIMIT 10;
CREATE ROLE univesp SUPERUSER CREATEDB CREATEROLE INHERIT LOGIN BYPASSRLS CONNECTION LIMIT 10;
CREATE ROLE daniel LOGIN PASSWORD '12345' IN ROLE professores;
```

### Deleta

```sql
DROP USER {username};
DROP USER django_user;
DROP ROLE univesp;
```

### Altera

```sql
ALTER USER django_user
ALTER USER univesp WITH PASSWORD null;
ALTER USER django WITH PASSWORD '12345';
ALTER USER postgres SUPERUSER;
ALTER ROLE michelmetran PASSWORD '12345';
```

### Listar Usuários

```sql
\du
```

## _Grant_ e _Revoke_

```sql
GRANT ALL ON DATABASE {db name};
GRANT ALL ON TABLE teste TO professores;
```

```sql
REVOKE ALL ON ALL TABLES IN SCHEMAS {schema name} FROM {username};
REVOKE ALL ON DATABASE {db name} FROM {username};
REVOKE ALL ON SCHEMA {schema name} FROM {username};
```

## Tabelas

### Criar

```sql
CREATE TABLE teste (nome varchar);
```

### Listar

```sql
\dt
```

## Sair

```sql
\q
```

# Tipos de Dados

## Key

- smallkey
- bigkey

## Caracter

- varchar(_n_)
- char(_n_)

## Date

- timestamp (com e sem timezone)
- timestamp (com e sem timezone)
- date
- interval

## Bolleano

- booleano

# DML e DDL

## Data Manipulation Language (DML)

INSERT, UPDATE, DELETE, SELECT

## DLL (Data Definition Language)

```sql
CREATE TABLE
DROP TABLE
ALTER TABLE
```

```sql
CREATE TABLE IF NOT EXIST {db name} (
codigo INTEGER PRIMARY KEY,
nome VARCHAR(50) NOT NULL,
data_criacao TIMESTAMP NOT NULL DEFAULT NOW(),
telefone INTEGER,
PRIMARY KEY (column name),
)
```

```sql
ALTER TABLE {db name} ADD COLUMN tem_poupanca BOOLEAN;
```

```sql
INSERT INTO {db} (codigo, nome, data_criacao)
VALUES (100, 'Itaú', now());
```

```sql
INSERT INTO {db} (codigo, nome, data_criacao)
SELECT 100, 'Itaú', now();
```

```sql
UPDATE {table name} SET
codigo =  1,
nome = 'Itaú',
WHERE data_criacao IS NULL;
```

CREATE TABLE IF NOT EXISTS banco (
numero INTEGER NOT NULL,
nome VARCHAR(50) NOT NULL,
ativo BOOLEAN NOT NULL DEFAULT TRUE,
data_criacao TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
PRIMARY KEY(numero)
)

## Aula

```sql
CREATE TABLE IF NOT EXISTS banco (
	numero INTEGER NOT NULL,
	nome VARCHAR(50) NOT NULL,
	ativo BOOLEAN NOT NULL DEFAULT TRUE,
	data_criacao TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY(numero)
);

CREATE TABLE IF NOT EXISTS agencia (
	banco_numero INTEGER NOT NULL,
	numero INTEGER NOT NULL,
	nome VARCHAR(80) NOT NULL,
	ativo BOOLEAN NOT NULL DEFAULT TRUE,
	data_criacao TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY(banco_numero, numero),
	FOREIGN KEY(banco_numero) REFERENCES banco(numero)
);

CREATE TABLE IF NOT EXISTS cliente (
	numero BIGSERIAL PRIMARY KEY,
	nome VARCHAR(120) NOT NULL,
	email VARCHAR(220) NOT NULL,
	ativo BOOLEAN NOT NULL DEFAULT TRUE,
	data_criacao TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS contacorrente (
	banco_numero INTEGER NOT NULL,
	agencia_numero INTEGER NOT NULL,
	numero BIGINT NOT NULL,
	digito SMALLINT NOT NULL,
	cliente_numero BIGINT NOT NULL,
	ativo BOOLEAN NOT NULL DEFAULT TRUE,
	data_criacao TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY(banco_numero, agencia_numero,numero, digito, cliente_numero),
	FOREIGN KEY(banco_numero, agencia_numero) REFERENCES agencia(banco_numero, numero),
	FOREIGN KEY(cliente_numero) REFERENCES cliente(numero)
);

CREATE TABLE IF NOT EXISTS tipo_transacao (
	id SMALLSERIAL PRIMARY KEY,
	nome VARCHAR(120) NOT NULL,
	ativo BOOLEAN NOT NULL DEFAULT TRUE,
	data_criacao TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS cliente_transacoes (
	id BIGSERIAL PRIMARY KEY,
	banco_numero INTEGER NOT NULL,
	agencia_numero INTEGER NOT NULL,
	conta_corrente_numero INTEGER NOT NULL,
	conta_corrente_digito INTEGER NOT NULL,
	cliente_numero BIGINT NOT NULL,
	tipo_transacao_id SMALLINT NOT NULL,
	valor NUMERIC(15,2) NOT NULL,
	data_criacao TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	FOREIGN KEY(banco_numero, agencia_numero, conta_corrente_numero, conta_corrente_digito, cliente_numero) REFERENCES contacorrente(banco_numero, agencia_numero,numero, digito, cliente_numero)
);
```

```sql
SELECT *
FROM information_schema.columns
WHERE table_name = 'banco'
```

# _Transactions_

BEGIN;

COMMIT;

SAVE POINT

ROLLBACK;

# Funções

# Arquivos de Configurações

## _postgresql.conf_

Arquivo que armazena todas as informações das configurações do banco de dados. A _view_ pg*settings, acessada dentro do banco de dados, guarda todas as configurações atuais, sendo necessário, por vezes, reinicializar o bando de dados para que a \_view* seja atualizada.

Por padrão, o arquivo encontra-se dentro do diretório PGDATA definido no momento da inicialização do _cluster_ do banco de dados. No Ubuntu, quando instalado pelo repositório oficial, o local do arquivo será diferente do diretório de dados:

- /etc/postgresql/{versão}/{nome do cluster}/**_postgresql.conf_**
- /etc/postgresql/12/main/**_postgresql.conf_**

As configurações do arquivo podem ser acessadas também por _querys_, tais como:

```sql
SHOW listen_addresses;                     # Endereços TCP/IP das interfaces que o servidor vai escutar
SHOW port;                                 # Porta TCP que o servidor vai ouvir (Padrão é 5432)
SHOW max_connections;                      # Nº máximo de conexões
SHOW superuser_reserved_connections;       # Nº máximo de conexões de superusuários
SHOW data_directory;                       # Diretório onde os dados são armazenados
SHOW authentication_timeout;               # Tempo máximo para o cliente conseguir conexão
SHOW password_encryption;                  # Algoritmo de criptografia das senhas dos novos usuários
SHOW ssl;                                  # Habilita conexção criptografada
SHOW shared_buffers;                       # Tamanho da memória cache/buffer de tabelas e índices
SHOW work_mem;                             # Tamanho da memória para operações de agrupamento e ordenação
SHOW maintenance_work_mem;                 # Tamanho da memória para operações como vaccum, index

```

## _pg_hba.conf_

Arquivo responsável pelo controle de autenticação dos usuários no servidor _PostGreSQL_

![Exemplo](https://i.imgur.com/iz9JJI8.png)

## _pg_ident.conf_

Arquivo responsável por mapear os usuários do sistema operacional com os usuários do bando de dados. Localizado no diretório de dados PGDATA de sua instalação. A opção _ident_ deve ser utilizada no arquivo _pg_hba.conf_.

# Interface Gráfica

O [pgAdminIV](https://www.pgadmin.org/) é a inferface gráfica do bando de dados. Uma vez instalado corretamente, estará disponível no [_localhost_](http://localhost/pgadmin4)

# Erros

Encerrar o que estiver na porta 5432

```bash
sudo fuser -k 5432/tcp
```

# Referências

- [Getting error: Peer authentication failed for user “postgres”, when trying to get pgsql working with rails](https://stackoverflow.com/questions/18664074/getting-error-peer-authentication-failed-for-user-postgres-when-trying-to-ge), no StackOverflow.
- [Como Instalar e Utilizar o PostgreSQL no Ubuntu 18.04](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-18-04-pt), no DigitalOcean
- [Como instalar o pgAdmin4 no Ubuntu e derivados](https://www.edivaldobrito.com.br/pgadmin4-no-ubuntu/), no Edivaldo Brito.
- [Install pgAdmin 4 on Ubuntu 20.04/18.04/16.04](https://computingforgeeks.com/how-to-install-pgadmin-4-on-ubuntu/), no Computing for Geeks.
- [Skipping acquire of configured file 'main/binary-i386/Packages'](https://stackoverflow.com/questions/61523447/skipping-acquire-of-configured-file-main-binary-i386-packages), no StackOverflow.
- [How to Install PostgreSQL and pgAdmin4 in Ubuntu 20.04](https://www.tecmint.com/install-postgresql-and-pgadmin-in-ubuntu/), usado em outubro de 2020.
