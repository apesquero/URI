# -*- coding: utf-8 -*-

test = int(input())

valores = []

for x in range(test):
    valor = [float(x) for x in input().split(" ")]
    valores.append(valor)

for valor in valores:
    cityA = valor[0]
    cityA = int(cityA)
    cityB = valor[1]
    cityB = int(cityB)
    pA = valor[2]
    pB = valor[3]

    anos = 0
    while cityA <= cityB:
        cityA += (pA * cityA) / 100
        cityA = int(cityA)
        cityB += (pB * cityB) / 100
        cityB = int(cityB)
        anos += 1
        if anos > 100:
            break
    if anos <= 100:
        print("%d anos." % anos)
    else:
        print("Mais de 1 seculo.")
