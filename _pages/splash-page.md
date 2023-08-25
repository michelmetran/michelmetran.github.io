---
title: "..."
layout: splash
permalink: /
date: 2023-08-22T08:00:00-03:00
header:
  overlay_color: "#000"
  overlay_filter: "0.5"
  overlay_image: /assets/images/cover/photo-1510519138101-570d1dca3d66.avif
  actions:
    - label: "Download"
      url: "https://github.com/mmistakes/minimal-mistakes/"
  caption: "Photo credit: [**Unsplash**](https://unsplash.com)"
excerpt: "Explorando a sinergia entre a natureza e o código: Bem-vindo ao meu *blog*, onde como biólogo e entusiasta da computação, compartilho *insights* que unem a gestão ambiental e a programação. Descubra o poder do *python*, SQL e ciência de dados na busca por um mundo mais sustentável."

# Centered with `type="center"`
intro:
  - excerpt: "Abaixo são apresentados alguns detaques dos meus projetos, porfolios e <i>trips</i>"

# dddd
feature_row:
  - image_path: assets/images/unsplash-gallery-image-1-th.jpg
    image_caption: "Image courtesy of [Unsplash](https://unsplash.com/)"
    title: "Placeholder 1"
    alt: "placeholder image 1"
    excerpt: "This is some sample content that goes here with **Markdown** formatting."
    btn_label: "Leia Mais"
    btn_class: "btn--primary"
    url: "#test-link"

  - image_path: /assets/images/unsplash-gallery-image-2-th.jpg
    image_caption: "Image courtesy of [Unsplash](https://unsplash.com/)"
    title: "Placeholder 1"
    alt: "placeholder image 1"
    excerpt: "This is some sample content that goes here with **Markdown** formatting."
    btn_label: "Leia Mais"
    btn_class: "btn--primary"
    url: "#test-link"

  - image_path: /assets/images/unsplash-gallery-image-3-th.jpg
    image_caption: "Image courtesy of [Unsplash](https://unsplash.com/)"
    title: "Placeholder 1"
    alt: "placeholder image 1"
    excerpt: "This is some sample content that goes here with **Markdown** formatting."
    btn_label: "Leia Mais"
    btn_class: "btn--primary"
    url: "#test-link"

# dddd
feature_row2:
  - image_path: /assets/images/cover/cover_open_geodata.png
    #image_caption: "Image courtesy of [Unsplash](https://unsplash.com/)"
    title: "Open Geodata"
    alt: "placeholder image 2"
    #excerpt: 'This is some sample content that goes here with **Markdown** formatting. Left aligned with `type="left"`'
    excerpt: Open Geodata surge para criar facilita o acesso a informação geoespacial (e outras), seja por meio de rotinas (*scripts*) para raspagem de dados, seja por meio da disponibilização de dados tratados.
    btn_label: "GitHub"
    btn_class: "btn--primary"
    url: "https://github.com/open-geodata/"
    btn_label2: "Posts"

# dddd
feature_row3:
  - image_path: /assets/images/cover/cover_div.png
    #image_caption: "Image courtesy of [Unsplash](https://unsplash.com/)"
    title: "Divisões Administrativas"
    alt: "placeholder image 2"
    excerpt: 'Divisões Administrativas de instituições públicas estaduais (São Paulo)'
    btn_label: "GitHub"
    btn_class: "btn--primary"
    url: "https://github.com/open-divisoes/"

# dddd
feature_row4:
  - image_path: /assets/images/unsplash-gallery-image-2-th.jpg
    image_caption: "Image courtesy of [Unsplash](https://unsplash.com/)"
    title: "Sistema Cantareira"
    alt: "placeholder image 2"
    excerpt: 'This is some sample content that goes here with **Markdown** formatting. Centered with `type="center"`'
    btn_label: "Read More"
    btn_class: "btn--primary"
    url: "#test-link"
---

{% include feature_row id="intro" type="center" %}

{% include feature_row id="feature_row2" type="left" %}

{% include feature_row id="feature_row3" type="right" %}

{% include feature_row id="feature_row4" type="center" %}

{% include feature_row %}
