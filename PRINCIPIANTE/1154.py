# -*- coding: utf-8 -*-

values = []

while True:
    value = int(input())
    if value < 0:
        break
    values.append(value)

result = 0

for value in values:
    result += float(value)

print("%.2f" % (result/(len(values))))
