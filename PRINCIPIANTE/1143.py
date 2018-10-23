# -*- coding: utf-8 -*-


while True:
    valor = int(input())
    if 1 < valor < 1000:
        break

fila = 0

while fila < valor:
    fila += 1
    print("%d %d %d" % (fila, fila**2, (fila**3)))
