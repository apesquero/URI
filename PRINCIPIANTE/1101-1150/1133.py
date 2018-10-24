# -*- coding: utf-8 -*-

lista = []

while len(lista) < 2:
    valor = int(input())
    lista.append(valor)

lista.sort()

valor1, valor2 = lista

for x in range(valor1+1, valor2):
    if x % 5 == 2 or x % 5 == 3:
        print(x)
