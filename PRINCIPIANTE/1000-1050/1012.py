# -*- coding: utf-8 -*-
import math


PI = 3.14159

values = input().split(" ")
value_a, value_b, value_c = values

value_a = float(value_a)
value_b = float(value_b)
value_c = float(value_c)

triangle_area = (value_a * value_c) / 2
circle_area = (PI * (math.pow(value_c, 2)))
trapeze_area = value_c * ((value_a + value_b) / 2)
square_area = math.pow(value_b, 2)
rectangle_area = value_a * value_b

print("TRIANGULO: %.3f" % triangle_area)
print("CIRCULO: %.3f" % circle_area)
print("TRAPEZIO: %.3f" % trapeze_area)
print("QUADRADO: %.3f" % square_area)
print("RETANGULO: %.3f" % rectangle_area)
