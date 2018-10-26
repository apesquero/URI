# -*- coding: utf-8 -*-

cases = int(input())

for n in range(cases):
    values = [int(x) for x in input().split(" ")]
    value, items = values
    result = 0
    if value % 2 == 0:
        value += 1
    for x in range(items):
        result += value
        value += 2

    print(result)
