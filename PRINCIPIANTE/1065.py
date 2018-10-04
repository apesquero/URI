# -*- coding: utf-8 -*-

pares = []

for x in range(5):
    valor = int(input())
    if valor % 2 == 0:
        pares.append(valor)

print("%d valores pares" % len(pares))
