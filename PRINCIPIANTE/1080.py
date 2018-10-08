# -*- coding: utf-8 -*-
import operator

valores = {}

for x in range(100):
    valor = int(input())
    valores.update({x+1: valor})

resultado = sorted(valores.items(), key=operator.itemgetter(1), reverse=True)

print("%d" % resultado[0][1])
print("%d" % resultado[0][0])
