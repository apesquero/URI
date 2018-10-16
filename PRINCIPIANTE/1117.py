# -*- coding: utf-8 -*-

count = 0

valores = []

while count < 2:
    valor = float(input())
    if 0.0 <= valor <= 10.0:
        valores.append(valor)
        count += 1
    else:
        print("nota invalida")

nota1, nota2 = valores

resultado = (nota1 + nota2) / 2

print("media = %.2f" % resultado)
