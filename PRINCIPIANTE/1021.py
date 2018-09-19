# -*- coding: utf-8 -*-

valor = float(input())

notas = [100.00, 50.00, 20.00, 10.00, 5.00, 2.00]
moedas = [1.00, 0.50, 0.25, 0.10, 0.05, 0.01]

counter = 0

print("NOTAS:")
while counter <= 5:
    nota = valor / notas[counter]
    valor = round(valor % notas[counter], 2)
    print("%d nota(s) de R$ %.2f" % (nota,  notas[counter]))
    counter = counter + 1

counter = 0
print("MOEDAS:")
while counter <= 5:
    moeda = valor / moedas[counter]
    valor = round(valor % moedas[counter], 2)
    print("%d moeda(s) de R$ %.2f" % (moeda,  moedas[counter]))
    counter = counter + 1

