# -*- coding: utf-8 -*-

while True:
    valores = [int(x) for x in input().split(" ")]
    valores.sort()

    x, y = valores
    if 1 < x < 20 and y < 100000:
        break

contador = 0

while contador < y:
    contador += 1
    print("%d" % contador, end="")
    if contador%x == 0:
        print()
    else:
        print("", end=" ")
