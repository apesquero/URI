# -*- coding: utf-8 -*-

values = input().split(" ")
a, b = values

a = int(a)
b = int(b)

lista = [a, b]
lista.sort()

division = lista[1] / lista[0]

if division % 1 == 0:
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")

