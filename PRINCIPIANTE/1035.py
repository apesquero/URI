# -*- coding: utf-8 -*-

values = input().split(" ")
a, b, c, d = values

a = int(a)
b = int(b)
c = int(c)
d = int(d)

if b > c and d > a and c + d > a + b and d > 0 and a % 2 == 0:
    print("Valores aceitos")
else:
    print("Valores nao aceitos")
