# -*- coding: utf-8 -*-

while True:
    valor = int(input())
    if 0 <= valor < 46:
        break

fibonacci = {0: 0, 1: 1}

for n in range(valor):
    if n >= 2:
        f = fibonacci[n-1] + fibonacci[n-2]
        fibonacci.update({n: f})
    f = fibonacci[n]
    print("%d" % f, end="")
    if n < valor-1:
        print(" ", end="")
print()