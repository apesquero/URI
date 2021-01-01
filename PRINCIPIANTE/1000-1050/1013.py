# -*- coding: utf-8 -*-

values = input().split(" ")
a, b, c = values

a = int(a)
b = int(b)
c = int(c)

maior_AB = (a + b + abs(a - b)) / 2
maior_BC = (maior_AB + c + abs(maior_AB - c)) / 2

print("%d eh o maior" % maior_BC)
