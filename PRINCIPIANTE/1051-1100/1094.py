# -*- coding: utf-8 -*-

experimentos = int(input())

cobaias = 0
coelhos = 0
ratos = 0
sapos = 0

for x in range(experimentos):
    valor = input().split(" ")
    numero, tipo = valor

    numero = int(numero)
    cobaias += numero

    if tipo == "C":
        coelhos += numero
    elif tipo == "R":
        ratos += numero
    elif tipo == "S":
        sapos += numero

print("Total: %d cobaias" % cobaias)
print("Total de coelhos: %d" % coelhos)
print("Total de ratos: %d" % ratos)
print("Total de sapos: %d" % sapos)
print("Percentual de coelhos: %.2f" % ((coelhos / cobaias) * 100), "%")
print("Percentual de ratos: %.2f" % ((ratos / cobaias) * 100), "%")
print("Percentual de sapos: %.2f" % ((sapos / cobaias) * 100), "%")
