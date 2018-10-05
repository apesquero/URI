# -*- coding: utf-8 -*-

n = int(input())

valoresIn = 0
valoresOut = 0

for x in range(n):
    valor = int(input())
    if 10 <= valor <= 20:
        valoresIn += 1
    else:
        valoresOut += 1

print("%d in" % valoresIn)
print("%d out" % valoresOut)
