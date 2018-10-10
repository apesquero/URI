# -*- coding: utf-8 -*-

i = 1

for x in range(5):
    j = 7
    for y in range(3):
        print("I=%d J=%d" % (i, j))
        j -= 1
    i += 2
