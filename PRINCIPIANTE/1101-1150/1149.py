# -*- coding: utf-8 -*-

validos = []

valores = [int(x) for x in input().split(" ")]


for valor in valores:
    if valor > 0:
        validos.append(valor)

resultado = 0

for valor in range(validos[1]):
    calculo = validos[0]+valor
    resultado += calculo

print(resultado)