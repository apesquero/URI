# -*- coding: utf-8 -*-

valores = []

while True:
    test = int(input())
    if 1 <= test <= 100:
        break

for x in range(test):
    while True:
        number = int(input())
        if 1 <= number <= 10**7:
            break
    valores.append(number)



for valor in valores:
    primo = True
    for x in range(valor-2):
        x += 2
        if valor % x == 0:
            primo = False
    if valor == 1:
        primo = False
    if primo:
        print("%d eh primo" % valor)
    else:
        print("%d nao eh primo" % valor)
