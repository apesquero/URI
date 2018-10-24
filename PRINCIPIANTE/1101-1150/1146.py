# -*- coding: utf-8 -*-

valores = []

while True:
    valor = int(input())
    if valor == 0:
        break
    valores.append(valor)

for valor in valores:
    for sequence in range(valor):
        sequence += 1
        print("%d" % sequence, end="")
        if sequence == valor:
            print()
        else:
            print(" ", end="")
