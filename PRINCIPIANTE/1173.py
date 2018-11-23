# -*- coding: utf-8 -*-

list = []

while True:
    valor = int(input())
    if valor < 50:
        break

for x in range(10):
    list.append(valor)
    valor *= 2
    print("N[%d] = %d" % (x, list[x]))


