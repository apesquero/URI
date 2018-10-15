# -*- coding: utf-8 -*-

lista = []

while True:
    valores = [int(x) for x in input().split(" ")]
    valores.sort()
    if valores[0] <= 0:
        break
    lista.append(valores)

for valores in lista:
    suma = 0
    for valor in range(valores[0], valores[1]+1):
        suma += valor
        print("%d" % valor, end=" ")
        if valor == valores[1]:
            print("Sum=%d" % suma)
