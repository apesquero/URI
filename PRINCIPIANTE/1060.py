# -*- coding: utf-8 -*-

count = 0

for x in range(6):
    valor = float(input())
    if valor > 0:
        count += 1

print("%d valores positivos" % count)
