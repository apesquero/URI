# -*- coding: utf-8 -*-

import math

values = input().split(" ")
a, b, c = values

a = float(a)
b = float(b)
c = float(c)

if a > 0 and b**2-(4*a*c) >= 0:
    x1 = (-b + math.sqrt(b**2-(4*a*c)))/(2*a)
    x2 = (-b - math.sqrt(b**2-(4*a*c)))/(2*a)
    print("R1 = %.5f" % x1)
    print("R2 = %.5f" % x2)
else:
    print("Impossivel calcular")
