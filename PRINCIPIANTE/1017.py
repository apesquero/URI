# -*- coding: utf-8 -*-

CONSUMO = 12

tiempo = int(input())
velocidad = int(input())

litros = float((velocidad * tiempo) / CONSUMO)

print("%.3f" % litros)
