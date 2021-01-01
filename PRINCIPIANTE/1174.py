# -*- coding: utf-8 -*-

list = []

for x in range(100):
    valor = float(input())
    list.append(valor)
    if valor <= 10:
        print("A[%d] = %.1f" % (x, list[x]))
