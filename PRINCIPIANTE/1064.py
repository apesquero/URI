# -*- coding: utf-8 -*-

valores = []
positivos = 0
promedio = 0

for x in range(6):
    valor = float(input())
    valores.append(valor)

for v in valores:
    if v > 0:
        positivos += 1
        promedio += v

promedio = promedio / positivos

print("%d valores positivos" % positivos)
print("%.1f" % promedio)
