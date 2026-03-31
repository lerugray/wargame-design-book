---
layout: home
title: Home
nav_order: 0
nav_exclude: true
description: "A practical, opinionated guide to designing historical board wargames — from choosing your subject to getting published."
---

## Read the Book

{% assign sorted = site.html_pages | sort: "nav_order" %}

### Part I: Foundations
{% for ch in sorted %}{% if ch.chapter_number and ch.chapter_number >= 1 and ch.chapter_number <= 5 %}
{{ ch.chapter_number }}. [{{ ch.title }}]({{ ch.url | relative_url }})
{% endif %}{% endfor %}

### Part II: Core Systems
{% for ch in sorted %}{% if ch.chapter_number and ch.chapter_number >= 6 and ch.chapter_number <= 12 %}
{{ ch.chapter_number }}. [{{ ch.title }}]({{ ch.url | relative_url }})
{% endif %}{% endfor %}

### Part III: Advanced Topics
{% for ch in sorted %}{% if ch.chapter_number and ch.chapter_number >= 13 and ch.chapter_number <= 14 %}
{{ ch.chapter_number }}. [{{ ch.title }}]({{ ch.url | relative_url }})
{% endif %}{% endfor %}

### Part IV: From Prototype to Publication
{% for ch in sorted %}{% if ch.chapter_number and ch.chapter_number >= 15 and ch.chapter_number <= 20 %}
{{ ch.chapter_number }}. [{{ ch.title }}]({{ ch.url | relative_url }})
{% endif %}{% endfor %}

### Part V: The Bigger Picture
{% for ch in sorted %}{% if ch.chapter_number and ch.chapter_number >= 21 and ch.chapter_number <= 23 %}
{{ ch.chapter_number }}. [{{ ch.title }}]({{ ch.url | relative_url }})
{% endif %}{% endfor %}

### Appendices
{% for ch in sorted %}{% if ch.is_appendix %}
- [{{ ch.title }}]({{ ch.url | relative_url }})
{% endif %}{% endfor %}

<hr class="section-divider">

## About This Book

This book is free to read online. If you find it useful, consider supporting the author by purchasing the paperback or Kindle edition on Amazon (link coming soon).

Have feedback? [Join the discussion on GitHub.](https://github.com/lerugray/wargame-design-book/discussions)
