# -*- coding: utf-8 -*-

cantidad = int(input())

lista = []

for x in range(cantidad):
    valores = [float(x) for x in input().split(" ")]
    lista.append(valores)

for valores in lista:
    x, y = valores
    try:
        resultado = x / y
        print("%.1f" % resultado)
    except:
        print("divisao impossivel")
