# -*- coding: utf-8 -*-

valor = int(input())

fila = 0
secuencia = 1

while fila < valor:
    fila += 1
    print("%d %d %d PUM" % (secuencia, secuencia+1, secuencia+2))
    secuencia += 4
