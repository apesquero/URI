# -*- coding: utf-8 -*-

i = 1
j = 7

for x in range(5):
    for y in range(3):
        print("I=%d J=%d" % (i, j))
        j -= 1
    i += 2
    j += 5
