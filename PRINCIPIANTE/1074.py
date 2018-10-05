# -*- coding: utf-8 -*-

nValores = int(input())
valores = []
description = ""

for x in range(nValores):
    valor = int(input())
    valores.append(valor)

for valor in valores:
    if valor % 2 == 0:
        description = "EVEN "
    else:
        description = "ODD "
    if valor > 0:
        description += "POSITIVE"
    else:
        description += "NEGATIVE"
    if valor == 0:
        description = "NULL"
    print(description)
