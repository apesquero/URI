# -*- coding: utf-8 -*-

list = []

for x in range(20):
    valor = int(input())
    list.append(valor)

list.reverse()
for x in range(20):
    print("N[%d] = %d" % (x, list[x]))
