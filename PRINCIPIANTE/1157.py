# -*- coding: utf-8 -*-

value = int(input())

for n in range(1, value+1):
    if value % n == 0:
        print(n)
