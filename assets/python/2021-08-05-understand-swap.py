# Author: Weiming Hu <weiming@psu.edu>
#
#         Geoinformatics and Earth Observation Laboratory (http://geolab.psu.edu)
#         Department of Geography and Institute for Computational and Data Sciences
#         The Pennsylvania State University
#
# Date of Creation: 2021/08/05
#
# This script is created for the post, understanding value swapping in Python.
#
# The post is available at https://weiming-hu.github.io/understand-swap/
#

import dis

def level_1():
    a, b = 1, 2
    a, b = b, a

def level_2():
    a, b, c, d = 1, 2, 3, 4
    a, b, c, d = d, c, b, a

def level_3():
    arr = [3, 2, 1, 0]
    arr[0], arr[3] = arr[3], arr[0]

def level_4():
    arr = [3, 2, 1, 0]
    arr[arr[0]], arr[0] = arr[0], arr[arr[0]]

def level_5():
    arr = [3, 2, 1, 0]
    arr[0], arr[arr[0]] = arr[arr[0]], arr[0]

dis.dis(level_1)
dis.dis(level_2)
dis.dis(level_3)
dis.dis(level_4)
dis.dis(level_5)

