---
layout: post
title: "Understanding Value Swapping in Python"
excerpt: "How Python swaps values might surprise you"
tags: [Python]
comments: true
year: 2021
last_modified_at: 2021-08-05T19:22:00
---

## Introduction

[Python](https://www.python.org/) has some very nice [syntax sugars](https://en.wikipedia.org/wiki/Syntactic_sugar) that really come in handy when we program. One such example is swapping values. It is probably one of the first things you learn and this feature is always touted to show Python's convenience and readability. The idea is that, instead of relying on a third variable, you can directly swap two values. Nice and easy!

But **there are caveats**. And that is why I wrote this article to explain what happens under the hood.

Try the following questions and see whether you are already familiar with what I'm going show you. Have fun!

```python
# Level 1: The swap feature that comes in handy
a, b = 1, 2
a, b = b, a
print('a: {}; b: {}'.format(a, b))

# Level 2: Yes. You can do more than just two.
a, b, c, d = 1, 2, 3, 4
a, b, c, d = d, c, b, a
print('a: {}; b: {}; c: {}; d: {}'.format(a, b, c, d))

# Level 3: It also works for lists.
arr = [3, 2, 1, 0]
arr[0], arr[3] = arr[3], arr[0]
print('arr: {}'.format(arr))

# Level 4: Getting fancier
arr = [3, 2, 1, 0]
arr[arr[0]], arr[0] = arr[0], arr[arr[0]]
print('arr: {}'.format(arr))

# Level 5: This might surprise you.
arr = [3, 2, 1, 0]
arr[0], arr[arr[0]] = arr[arr[0]], arr[0]
print('arr: {}'.format(arr))

# Level 6
# Explain how they are different @_@

###########
# Answers #
###########

# 1. a = 2, b = 1
# 2. a = 4, b = 3, c = 2, d = 1
# 3. arr = [0, 2, 1, 3]
# 4. arr = [0, 2, 1, 3]
# 5. arr = [3, 2, 1, 0]
# 6. Please read the rest of the post.
```

## Preparation

I am glad that you decide to read on. It is recommended to have Python `3.x` running. I am using Python `3.9.5`.

We are going to read some [assembly code](https://en.wikipedia.org/wiki/Assembly_language). But **you do not need to have any knowledge in assembly language**. It is simply a way for us to see what exactly Python is doing. To compile Python into assembly, we need the native Python module, `dis`.

[Here](https://docs.python.org/3/library/dis.html#python-bytecode-instructions) is a dictionary of assembly instructions. It contains documentation for all instructions that we are going to see in this post.

## Level 1

<div class="row">
  <div class="col-md-8" markdown="1">
  Some text.
  </div>
  <div class="col-md-4" markdown="1">
  <!-- ![Alt Text](../img/folder/blah.jpg) -->
  <img height="600px" class="center-block" src="../img/folder/blah.jpg">
  </div>
</div>

## References

- [How does swapping of members in tuples (a,b)=(b,a) work internally?](https://stackoverflow.com/a/21047622)
