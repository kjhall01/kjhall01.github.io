---
layout: post
research: true
title: "High Resolution Forecasts of Photovoltaic Energy Production"
excerpt: "Using Analog Ensemble to forecast photovoltaic energy production on a household level"
tags: [Research, Analog Ensemble]
comments: true
last_modified_at: 2018-11-06T15:15:00
---

## Key Points

This poster studies the temporal predictability of the small-scale photovoltaic energy production. The location studies is at State College, PA. The study compares the prediction performance between the Artificial Neural Network (ANN) and the [Analog Ensemble](https://weiming-hu.github.io/AnalogsEnsemble/) (AnEn) technique in forecasting short-term (3-day forecasts) photovoltaic energy production.

- The optimal ANN is trained using a brute-force search with 1-20 hidden nodes, and the best one with 10 nodes is chosen. At this specific location, AnEn outperforms ANN in respect to daily averaged errors. ANN tends to under-predict the peak photovoltaic (PV) energy production while AnEn shows good results during peak PV energy time period.
- AnEn can be used to downscale hourly PV forecasts to every 5-minute which, in this case, is the resolution of PV observations. Results show that the downscaling technique with AnEn is fairly accurate when the original forecasts are accurate.
- Both (ANN and AnEn) model are not able to perform well when the underlying meteorological model is inaccurate.

## Poster

*If it is not displaying normally, you can access the PDF [here](https://weiming-hu.github.io/assets/data-for-posts/2018-11-06-PV-forecasts/PV-forecasts.pdf).*

<object data="https://weiming-hu.github.io/assets/data-for-posts/2018-11-06-PV-forecasts/PV-forecasts.pdf" type="application/pdf" width="100%" height="80%">
<embed src="https://weiming-hu.github.io/assets/data-for-posts/2018-11-06-PV-forecasts/PV-forecasts.pdf">
This browser does not support PDFs. Please download the PDF to view it: <a href="https://weiming-hu.github.io/assets/data-for-posts/2018-11-06-PV-forecasts/PV-forecasts.pdf">Download PDF</a>.</p>
</embed>
</object>

