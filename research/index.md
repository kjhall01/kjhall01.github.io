---
layout: page
title: Research
tags: [research]
date: 2022-05-31
comments: false
---

<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
.card {
  box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
  transition: 0.3s;
}

.card:hover {
  box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2);
  cursor: pointer;
}

.mycontainer {
  padding: 2px 16px;
}
</style>
</head>

<img src="https://kjhall01.github.io/assets/img/IMG_4130.jpg" alt="Kyle Hall" style="width:400px !important">

## Research Interest

I am a climate data scientist seeking to increase society’s resilience against climate change and climate variability by contributing to the improvement of quantitative climate forecasting and climate modeling. I received my M.A. in Climate & Society at Columbia University with the International Research Institute for Climate & Society, and my B.S. in Computer Science at the College of William & Mary, specializing in AI/ML and data science methods.

Research Keywords:

- Geospatial Data Science 
- Artificial Intelligence
- High Performance Computing
- Machine Learning 
- Climate Forecasting

## Research Showcase

Here is a curated list of posts that showcase my research and document my research experiences. The summary of the research project is followed by an excerpt. Comments are well welcome.

{% capture this_word %}Research{% endcapture %}
{% for post in site.tags[this_word] %}{% if post.title != null %}
<div class="card" onclick="location.href='{{ site.url }}{{ post.url }}';"><div class="mycontainer">
<h4>[<em>{{ post.year }}</em>] <a href="{{ site.url }}{{ post.url }}" title="{{ post.title }}">{{ post.title }}</a></h4>
<p><em>Excerpt: {{ post.excerpt }}</em></p>
</div></div>
<br>
{% endif %}{% endfor %}




