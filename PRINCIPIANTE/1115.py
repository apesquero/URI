# -*- coding: utf-8 -*-

lista = []

while True:
    valores = [int(x) for x in input().split(" ")]
    if valores[0] == 0 or valores[1] == 0:
        break
    lista.append(valores)

for valores in lista:
    x, y = valores
    if x > 0:
        if y > 0:
            print("primeiro")
        else:
            print("quarto")
    else:
        if y > 0:
            print("segundo")
        else:
            print("terceiro")
