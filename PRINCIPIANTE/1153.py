# -*- coding: utf-8 -*-

while True:
    value = int(input())
    if 0 < value < 13:
        break

resultado = 1

for n in range(value):
    n += 1
    resultado *= n

print(resultado)

