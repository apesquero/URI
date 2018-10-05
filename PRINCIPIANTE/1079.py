# -*- coding: utf-8 -*-

n = int(input())
notas = []

for x in range(n):
    valores = [float(x) for x in input().split(" ")]
    resultado = ((valores[0]*2) + (valores[1]*3) + (valores[2]*5)) / 10

    notas.append(resultado)

for x in notas:
    print("%.1f" % x)
