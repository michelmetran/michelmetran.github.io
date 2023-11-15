---
title: "Conda: Problemas"
date: 2019-06-13T15:34:30-04:00
last_modified_at: 2022-06-28T00:00:00-03:00
excerpt_separator: "<!--more-->"
categories:
  - IT
tags:
  - python
  - anaconda
  - miniconda
---

## SSL

Ao tentar criar um enviroment no conda, na rede institucional, recebia o seguinte erro:

> CondaHTTPError: HTTP 000 CONNECTION FAILED for url <https://repo.anaconda.com/pkgs/main/win-64/current_repodata.json>

<br>

Estudando o problema, encontrei uma solução preliminar no [StackOverflow](https://stackoverflow.com/questions/42563757/conda-update-condahttperror-http-none), que sugere que seja removido a verificação do ssl.

```bash
conda config --set ssl_verify false
conda config --set ssl_verify no
```

<br>

Sabemos das implicações de fazer isso, porém é a única alternativa encontrada no momento.

<br>

---

Lendo a documentação, vi que é possível contornar a questão do SSL, [_using non-standard certificates_](https://docs.conda.io/projects/conda/en/latest/user-guide/configuration/non-standard-certs.html). Inicialmente faz-se necessário obter o certificado e converte-lo no formato _.pem_.

```bash
openssl x509 -inform der -in Documents/certificado.cer -out Documents/certificado.pem
```

<br>

Após isso é necessário definir a variável de ambiente `REQUESTS_CA_BUNDLE` (ou `CURL_CA_BUNDLE`)apontando para o certificado.

```bash
# PEM
%USERPROFILE%\Documents\Certificate\certificado.
pem

# PEM
%USERPROFILE%\OneDrive\MPSP\TI\certificado\2022.10.14 - mpsp.pem
```

<br>

Fiz em meados de outubro de 2022, porém não obtive êxito.

<br>

---

Analisando o artigo [Conda update fails with SSL error CERTIFICATE_VERIFY_FAILED](https://stackoverflow.com/questions/33699577/conda-update-fails-with-ssl-error-certificate-verify-failed), vejo possibilidade de contornar...

```bash
conda config --set ssl_verify "%USERPROFILE%\OneDrive\MPSP\TI\certificado\2022.10.14 - mpsp.crt"

/home/michel/Documents/Conda/condabin/conda
```
