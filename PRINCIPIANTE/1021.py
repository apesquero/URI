# -*- coding: utf-8 -*-

valor = float(input())

notas = [100.00, 50.00, 20.00, 10.00, 5.00, 2.00]
moedas = [1.00, 0.50, 0.25, 0.10, 0.05, 0.01]

print("NOTAS:")
for nota in notas:
    nNota = valor / nota
    valor = round(valor % nota, 2)
    print("%d nota(s) de R$ %.2f" % (nNota, nota))

print("MOEDAS:")
for moeda in moedas:
    nMoeda = valor / moeda
    valor = round(valor % moeda, 2)
    print("%d moeda(s) de R$ %.2f" % (nMoeda, moeda))
