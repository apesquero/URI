# -*- coding: utf-8 -*-

values = input().split(" ")
a, b, c = values

a = float(a)
b = float(b)
c = float(c)

if a + b > c and a + c > b and b + c > a:
    perimetro = a + b + c
    print("Perimetro = %.1f" % perimetro)
else:
    area = ((a + b) * c) / 2
    print("Area = %.1f" % area)
