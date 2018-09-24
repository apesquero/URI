# -*- coding: utf-8 -*-

values = input().split(" ")
a, b, c = values

i = 0

a = int(a)
b = int(b)
c = int(c)

listNumber = [a, b, c]
listNumberSorterd = listNumber[:]
listNumberSorterd.sort()

while i < 3:
    print("%d" % listNumberSorterd[i])
    i = i + 1

print("")
i = 0
while i < 3:
    print("%d" % listNumber[i])
    i = i + 1
