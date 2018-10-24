# -*- coding: utf-8 -*-

valores = []

while True:
    while len(valores) < 2:
        valor = float(input())
        if 0 <= valor <= 10:
            valores.append(valor)
        else:
            print("nota invalida")
    x, y = valores
    resultado = (x + y) / 2
    print("media = %.2f" % resultado)
    valores = []
    print("novo calculo (1-sim 2-nao)")
    option = int(input())
    while 1 != option != 2:
        print("novo calculo (1-sim 2-nao)")
        option = int(input())
    if option == 2:
        break