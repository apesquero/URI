# -*- coding: utf-8 -*-

test = int(input())

for x in range(test):
    while True:
        valor = int(input())
        if 0 <= valor <= 60:
            y = (1+(5**(1/2)))/2
            fib = ((y**valor)-((1-y)**valor))/(5**(1/2))
            print("Fib(%d) = %d" % (valor, fib))
            break
