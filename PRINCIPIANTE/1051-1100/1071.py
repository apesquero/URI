# -*- coding: utf-8 -*-

valor = []

for x in range(2):
    v = int(input())
    valor.append(v)

valor.sort()

suma = 0

for x in range(valor[0]+1, valor[1]):
    if x % 2 != 0:
        suma += x

print("%d" % suma)
