# -*- coding: utf-8 -*-

valores = []

for x in range(2):
    valor = int(input())
    valores.append(valor)
    valores.sort()

suma = 0
for valor in range(valores[0], valores[1]+1):
    if valor % 13 != 0:
        suma += valor

print(suma)
