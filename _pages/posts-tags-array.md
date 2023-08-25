---
title: <i>Posts</i> por Array
layout: archive
permalink: /posts/tags/array/
author_profile: false
sidebar:
  nav: posts_nav
---

{% include group-by-array.html collection=site.posts field='tags' %}

<ul>
  {% for tag in group_names %}
    {% assign posts = group_items[forloop.index0] %}

    <li>
      <h2>{{ tag }}</h2>
      <ul>
        {% for post in posts %}
        <li>
          <a href='{{ site.baseurl }}{{ post.url }}'>{{ post.title }}</a>
        </li>
        {% endfor %}
      </ul>
    </li>

{% endfor %}

</ul>