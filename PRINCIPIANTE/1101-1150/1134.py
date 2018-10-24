# -*- coding: utf-8 -*-

gas = {1: 0, 2: 0, 3: 0}

while True:
    valor = int(input())
    if valor in range(1, 4):
        n = gas[valor]
        gas.update({valor: n+1})
    else:
        if valor == 4:
            break

print("MUITO OBRIGADO")
print("Alcool: %d" % gas[1])
print("Gasolina: %d" % gas[2])
print("Diesel: %d" % gas[3])
