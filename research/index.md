---
layout: page
title: Research
tags: [research]
date: 2020-11-10
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
}

.mycontainer {
  padding: 2px 16px;
}
</style>
</head>

<img src="https://weiming-hu.github.io/assets/img/logo.jpg" alt="Weiming Hu" style="width:400px !important">

## Table of Content

<!-- vim-markdown-toc GFM -->

* [Research Interest](#research-interest)
* [Ph.D. Dissertation](#phd-dissertation)
* [Curriculum Vitae](#curriculum-vitae)
* [Research Showcase](#research-showcase)
* [Programming](#programming)

<!-- vim-markdown-toc -->

## Research Interest

I'm a Ph.D. Candidate in Geography under the supervision of [Dr. Guido Cervone](https://www.geog.psu.edu/directory/guido-cervone) in the [Geoinformatics and Earth Observation Laboratory](http://geoinf.psu.edu/).

Below is a list of my research keywords:

- Ensemble Weather Forecasting
- Uncertainty Quantification of Renewable Energy
- Artificial Intelligence
- High Performance Computing

## Ph.D. Dissertation

My Ph.D. thesis title is *Uncertainty Quantification for Photovoltaic Energy Production Using Analog Ensemble*. I'm investigating the predictability of photovoltaic solar energy production over the Continental US. The uncertainty of solar energy production not only originates from the variation of solar irradiance, but also other weather conditions, including wind speed and ambient temperature, together with the configuration of the particular energy performance system. I'm using [Analog Ensemble](https://weiming-hu.github.io/AnalogsEnsemble) to study the spatial and temporal predictability of photovoltaic solar energy generation.

There are several key features of the project:

1. The evaluation of uncertainty via ensembles: Analog Ensemble is used to generate ensembles from a deterministic model and then ensembles are used for uncertainty evaluation.
2. Coupled power simulation system: The weather forecast system has been coupled with a solar power performance system to study the predictability of the power generation.
3. High-performance computing: The research domain is the continental US with a 12 km spatial resolution and an hourly temporal resolution. This requires computing capabilities from supercomputers.


## Curriculum Vitae

Please see my [CV](https://weiming-hu.github.io/assets/pdf/Hu-Weiming-CV.pdf) for more information.

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

## Programming

I'm passionate in programming and I'm an active contributor to open-source projects and the community.

I have been actively developing and maintaining the following packages and code repositories. They are developed during my current and previous courses of research. Some of them were converted into packages for a broader research community.

- [Parallel Analog Ensemble](https://weiming-hu.github.io/AnalogsEnsemble/) (C++/R)
- [RAnEnExtra](https://weiming-hu.github.io/RAnEnExtra/) (R)
- [Solar Photovoltaic Energy Simulator](https://github.com/Weiming-Hu/RenewableSimulator) (Python)
- [EITrans: Empirical Inverse Transform Function](https://weiming-hu.github.io/EITrans/) (R)
- [More Parallel R](https://weiming-hu.github.io/MoreParallelR/) (R)

For more about my technical skills, please see [my posts organized by tags](https://weiming-hu.github.io/tags/).

