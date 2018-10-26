# -*- coding: utf-8 -*-

n = 3
p = 2
s = 1

while n <= 39:
    s += n / p
    n += 2
    p *= 2

print("%.2f" % s)
