---
layout: default
title: Home
nav_order: 0
---

# A Contemporary Guide to Wargame Design

**By Ray Weiss**

A practical, opinionated guide to designing historical board wargames — from choosing your subject to getting published. Written by an independent designer who learned by doing, making mistakes, and occasionally getting things right.

---

## Read the Book

{% assign sorted = site.chapters | sort: "nav_order" %}

### Part I: Foundations
{% for ch in sorted %}{% if ch.nav_order >= 1 and ch.nav_order <= 5 %}
{{ ch.nav_order }}. [{{ ch.title }}]({{ ch.url | relative_url }})
{% endif %}{% endfor %}

### Part II: Core Systems
{% for ch in sorted %}{% if ch.nav_order >= 6 and ch.nav_order <= 12 %}
{{ ch.nav_order }}. [{{ ch.title }}]({{ ch.url | relative_url }})
{% endif %}{% endfor %}

### Part III: Advanced Topics
{% for ch in sorted %}{% if ch.nav_order >= 13 and ch.nav_order <= 14 %}
{{ ch.nav_order }}. [{{ ch.title }}]({{ ch.url | relative_url }})
{% endif %}{% endfor %}

### Part IV: From Prototype to Publication
{% for ch in sorted %}{% if ch.nav_order >= 15 and ch.nav_order <= 20 %}
{{ ch.nav_order }}. [{{ ch.title }}]({{ ch.url | relative_url }})
{% endif %}{% endfor %}

### Part V: The Bigger Picture
{% for ch in sorted %}{% if ch.nav_order >= 21 and ch.nav_order <= 23 %}
{{ ch.nav_order }}. [{{ ch.title }}]({{ ch.url | relative_url }})
{% endif %}{% endfor %}

### Appendices
{% for ch in sorted %}{% if ch.nav_order >= 100 %}
- [{{ ch.title }}]({{ ch.url | relative_url }})
{% endif %}{% endfor %}

---

## About This Book

This book is free to read online. If you find it useful, consider supporting the author by purchasing the paperback or Kindle edition on Amazon (link coming soon).

Have feedback? [Join the discussion on GitHub.](https://github.com/lerugray/wargame-design-book/discussions)
