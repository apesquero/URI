# -*- coding: utf-8 -*-

valor = int(input())

if valor % 2 == 0:
    valor += 1
for x in range(6):
    print("%d" % valor)
    valor += 2
