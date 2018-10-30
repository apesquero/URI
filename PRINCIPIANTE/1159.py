# -*- coding: utf-8 -*-

valores = []

while True:
    valor = int(input())
    if valor == 0:
        break
    valores.append(valor)

for valor in valores:
    if valor % 2 != 0:
        valor += 1
    result = 0
    for x in range(5):
        result += valor
        valor += 2

    print(result)
