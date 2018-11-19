# -*- coding: utf-8 -*-

while True:
    test = int(input())
    if 1 <= test <= 100:
        break

valores = []

for x in range(test):
    while True:
        valor = int(input())
        if 1 <= valor <= 10**8:
            break
    valores.append(valor)

for valor in valores:
    suma = 0
    for x in range(valor-1):
        x += 1
        if valor % x == 0:
            suma += x
    if valor == suma:
        print("%d eh perfeito" % valor)
    else:
        print("%d nao eh perfeito" % valor)
