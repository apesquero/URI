# -*- coding: utf-8 -*-

list = []

for x in range(10):
    valor = int(input())
    if valor <= 0:
        valor = 1
    list.append(valor)

for x in range(10):
    print("X[%d] = %d" % (x, list[x]))

