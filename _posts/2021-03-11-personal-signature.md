---
layout: post
title: "Personal Code Signature"
excerpt: "Source code header"
tags: [R]
comments: false
year: 2021
last_modified_at: 2021-03-11T12:00:00
---

<link rel="stylesheet" href="https://formden.com/static/assets/demos/bootstrap-iso/bootstrap-iso/bootstrap-iso.css">

I post below my most recent template for source code header signature for my own convenience.

<script>
function copyText(region_id) {
  /* Get the text field */
  var copyText = document.getElementsByClassName("highlight");

  var $temp = $("<textarea>");
  $("body").append($temp);
  $temp.val(copyText[region_id].innerText).select();
  document.execCommand("copy");
  $temp.remove();

  /* Alert the copied text */
  alert("The content has been copied!");
}  
</script>

<div class="bootstrap-iso">
<button onclick="copyText(0)" type="button" class="btn btn-success">Copy header contents</button>
</div>

```
# "`-''-/").___..--''"`-._
#  (`6_ 6  )   `-.  (     ).`-.__.`)   WE ARE ...
#  (_Y_.)'  ._   )  `._ `. ``-..-'    PENN STATE!
#    _ ..`--'_..-_/  /--'_.' ,'
#  (il),-''  (li),'  ((!.-'
# 
# Author: Weiming Hu <weiming@psu.edu>
#
#         Geoinformatics and Earth Observation Laboratory (http://geolab.psu.edu)
#         Department of Geography and Institute for Computational and Data Sciences
#         The Pennsylvania State University
#
# Date of Creation: 2021/01/01
#
# [Summary of the source code file]
```

