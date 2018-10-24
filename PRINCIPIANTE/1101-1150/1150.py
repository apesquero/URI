# -*- coding: utf-8 -*-

valor1 = int(input())

while True:
    valor2 = int(input())
    if valor2 > valor1:
        break

contador = 0
sumatorio = 0

for x in range(valor1, valor2+1):
    contador += 1
    sumatorio += x
    if sumatorio > valor2:
        break

print(contador)
