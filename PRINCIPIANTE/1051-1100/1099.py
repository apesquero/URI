# -*- coding: utf-8 -*-

casos = int(input())
resultados = []

for x in range(casos):
    valores = [int(x) for x in input().split(" ")]
    valores.sort()
    suma = 0
    for valor in range(valores[0]+1, valores[1]):
        if valor % 2 != 0:
           suma += valor
    resultados.append(suma)

for resultado in resultados:
    print("%d" % resultado)
