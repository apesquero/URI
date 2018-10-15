# -*- coding: utf-8 -*-

i = 0

while i <= 2:
    for x in range(3):
        print("I={:g} J={:g}" .format(i, x+1+i))
    i += 0.2
