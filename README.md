# Minimal Mistakes remote theme starter

[GitHub](https://github.com/michelmetran/michelmetran.github.io) |
[GitPage](https://michelmetran.github.io/)

O **_Ruby on Rails_**, comumente conhecido como **_Rails_**, é um _framework_ de desenvolvimento de aplicações web de código aberto escrito em _Ruby_, uma linguagem de programação dinâmica e orientada a objetos. Foi criado por David Heinemeier Hansson e lançado em 2004, ganhando rapidamente popularidade devido à sua abordagem inovadora para desenvolvimento web.

O **_Rails_** é projetado para simplificar e agilizar o processo de construção de aplicações _web_, seguindo o princípio de Convenção sobre Configuração (Convention over Configuration) e o princípio de _Don't Repeat Yourself (DRY)_. Isso significa que o _framework_ fornece uma estrutura pré-definida com muitas convenções e automatizações, o que permite que os desenvolvedores se concentrem mais na lógica específica da aplicação do que na configuração repetitiva.

Alguns conceitos-chave do **_Ruby on Rails_** incluem:

- **Model-View-Controller (MVC)**: O Rails segue a arquitetura MVC, que separa os componentes da aplicação em três partes: o Modelo (_Model_), que gerencia os dados e a lógica de negócios; a Visualização (_View_), que lida com a apresentação e a interface do usuário; e o Controlador (_Controller_), que gerencia as interações entre o modelo e a visualização.
- **Active Record**: O Active Record é uma parte crucial do _Rails_ que trata do mapeamento objeto-relacional (ORM). Ele permite que os desenvolvedores manipulem os dados do banco de dados usando classes Ruby, abstraindo a complexidade das consultas SQL e fornecendo uma interface mais orientada a objetos para interagir com o banco de dados.
- **Scaffolding**: O _Rails_ oferece o recurso de geração de scaffolding, que cria automaticamente o código básico para um modelo, visualização e controlador. Isso é útil para iniciar rapidamente o desenvolvimento, mas os desenvolvedores geralmente personalizam e expandem esses componentes conforme a necessidade.
- **Gemas (Gems)**: As gems são pacotes reutilizáveis de código Ruby que podem ser facilmente integrados em um projeto _Rails_ para adicionar funcionalidades extras. A vasta comunidade do _Rails_ contribuiu para uma grande variedade de gems que cobrem desde autenticação e autorização até integração com APIs externas.
  **Convenções**: O _Rails_ enfatiza a importância das convenções ao nomear pastas, arquivos e componentes da aplicação. Isso facilita a colaboração entre desenvolvedores e torna o código mais previsível.

<br>

Em resumo, o **_Ruby on Rails_** é um _framework_ que oferece uma abordagem ágil e eficiente para o desenvolvimento de aplicações web, permitindo aos desenvolvedores criar rapidamente aplicações robustas e escaláveis com menos esforço em tarefas repetitivas.

<br>

---

### Desenvolvimento Local

```shell
# Regenerate Gemfile.lock
bundle install

# Roda
bundle exec jekyll serve

# Corrige erro de ausencia de webrick
bundle add webrick

# Atualiza
bundle update

# Update
bundle exec jekyll serve --open-url --livereload --incremental
```

rubyinstaller-devkit-3.1.3-1-x64
