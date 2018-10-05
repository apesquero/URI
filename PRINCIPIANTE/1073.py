# -*- coding: utf-8 -*-

valor = int(input())

for x in range(1, valor+1):
    if x % 2 == 0:
        print("%d^2 = %d" % (x, x**2))
