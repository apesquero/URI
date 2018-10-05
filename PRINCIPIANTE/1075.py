# -*- coding: utf-8 -*-

valor = int(input())

for x in range(1, 10000):
    if x % valor == 2:
        print("%d" % x)
