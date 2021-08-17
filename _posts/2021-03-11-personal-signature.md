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
##########################################################
# Author: Weiming Hu <weh012@ucsd.edu>                   #
#                                                        #
#         Center for Western Weather and Water Extremes  #
#         Scripps Institution of Oceanography            #
#         UC San Diego                                   #
#                                                        #
#         https://weiming-hu.github.io/                  #
#         https://cw3e.ucsd.edu/                         #
#                                                        #
# Date of Creation: 2021/01/01                           #
##########################################################
#
# [Summary of the source code file]
```

