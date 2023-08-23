---
title: 'Oracle Instances'
date: 2019-06-13T15:34:30-04:00
last_modified_at: 2022-06-29T00:00:00-03:00
categories: [jobs]
---

Em maio de 2023 criei uma instância na Oracle Cloud para fazer _deploy_ de aplicações _python_. Minha instância usa Oracle Linux 9, baseada em RHEL.

Tudo começou quando vi o vídeo [Deploying a Flask app to a Virtual Machine - Learning Flask Series Pt. 23](https://www.youtube.com/watch?v=a2g9pDleGQk)

Para fazer _deploy_ das aplicações em _python_ optei por utilizar o [NGINX](https://www.nginx.com/)

Para instalar o NGINX instância, segue os procedimentos descritos em [Installing NGINX Open Source](https://docs.nginx.com/nginx/admin-guide/installing-nginx/installing-nginx-open-source/). Abri as portas da VM conforme descrito em [Chapter 2. Setting up and configuring NGINX](https://access.redhat.com/documentation/pt-br/red_hat_enterprise_linux/9/html/deploying_web_servers_and_reverse_proxies/setting-up-and-configuring-nginx_deploying-web-servers-and-reverse-proxies)

```
sudo su
firewall-cmd --permanent --add-port={80/tcp,443/tcp}
firewall-cmd --reload
```

<br>

Lendo os _posts_ e _blogs_ notei que o NGINX, quando instalado no RHEL (ou Oracle Linux), não vem, por padrão, com algumas configurações padrão que vem no Ubuntu (motivo pelo qual alguns sugerem o Ubuntu).

Dentre essas configurações está a ausência das pastas abaixo. Como elas não vem, por padrão, é necessário cria-las, conforme é mencionado nesse _post_ [StackOverflow: **nginx missing sites-available directory**](https://stackoverflow.com/questions/17413526/nginx-missing-sites-available-directory)

```
sudo mkdir /etc/nginx/sites-available
sudo mkdir /etc/nginx/sites-enabled
```

<br>

> Of course, all the files will be inside sites-available, and you'd create a symlink for them inside sites-enabled for those you want enabled.

<br>

Uma vez criadas, é necessário indicar, nas configurações do NGIX, que é preciso que ele olhe o conteúdo das pastas.

```bash
# Edita as configurações
sudo nano /etc/nginx/nginx.conf

# E coloca essa linha nos includes
include /etc/nginx/sites-enabled/\*;
```

<br>

Tentei iniciar a aplicação...

```
sudo systemctl status nginx
sudo systemctl enable nginx
sudo systemctl start nginx
sudo systemctl stop nginx
sudo systemctl restart nginx
sudo nginx -s reload
```

<br>

Por algum momento não deu certo pois a porta 80 estava em uso. Comandos para avalir o que está em uso. Descobri o que era e fechei.

```
sudo fuser -k 443/tcp
sudo fuser -k 80/tcp
```

<br>

De acordo com o artigo [2.2. Configuring NGINX as a web server that provides different content for different domains](https://access.redhat.com/documentation/pt-br/red_hat_enterprise_linux/9/html/deploying_web_servers_and_reverse_proxies/setting-up-and-configuring-nginx_deploying-web-servers-and-reverse-proxies#configuring-nginx-as-a-web-server-that-provides-different-content-for-different-domains_setting-up-and-configuring-nginx), é indicado que se use o código abaixo para carreegar a página inicial.

```
server {
    listen       80 default_server;
    listen       [::]:80 default_server;
    server_name  _;
    root         /usr/share/nginx/html;
}
```

<br>

Eu customize e inseri esse conteúdo no arquivo _default_:

```
sudo nano /etc/nginx/sites-available/default
```

<br>

E criei um link para

```bash
# Cria link
sudo ln -s /etc/nginx/sites-available/default /etc/nginx/sites-enabled

# Para remover link
sudo unlink /etc/nginx/sites-enabled/default
```

<br>

Edita esse arquivo, conforme

```
server {
listen 80;
listen [::]:80;
server_name localhost;
client_max_body_size 10M;

    #charset koi8-r;

    #access_log  logs/host.access.log  main;

    location / {
        # root   html;
        # index  index.html;
        proxy_pass      http://127.0.0.1:5000;
        proxy_redirect  off;

        proxy_set_header    Host                $host;
        proxy_set_header    X-Real-IP           $remote_addr;
        proxy_set_header    X-Forwarded-For     $proxy_add_x_forwarded_for;
        proxy_set_header    X-Forwarded-Proto   $scheme;
    }
```

<br>

Após bater cabeça, vi que a _Virtual Private Network_, na infra do Oracle, podria estar bloqueando o tráfego... corrigo com auxílio desse artigo [Opening up port 80 and 443 for Oracle Cloud servers](https://cleavr.io/cleavr-slice/opening-port-80-and-443-for-oracle-servers)

<br>

---

## Referências

- [Is is possible to run multiple apps in one VM instance?](https://stackoverflow.com/questions/73388316/is-is-possible-to-run-multiple-apps-in-one-vm-instance)
- [Como instalar e configurar Nginx on CentOS 7](https://serverspace.io/pt/support/help/install-and-configure-nginx-on-centos-7/), comecei a seguir e parei, após criar arquivo html.
- [How To Serve Flask Applications with uWSGI and Nginx on Ubuntu 18.04](https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-uswgi-and-nginx-on-ubuntu-18-04)
