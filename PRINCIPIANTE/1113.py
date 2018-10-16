# -*- coding: utf-8 -*-

lista = []

while True:
    valores = [int(x) for x in input().split(" ")]
    if valores[0] == valores[1]:
        break
    lista.append(valores)

for valores in lista:
    x, y = valores
    if x > y:
        print("Decrescente")
    else:
        print("Crescente")
