# -*- coding: utf-8 -*-

values = input().split(" ")
a, b, c = values

i = 0

a = int(a)
b = int(b)
c = int(c)

listNumber = [a, b, c]
listNumberSorted = listNumber[:]
listNumberSorted.sort()

while i < 3:
    print("%d" % listNumberSorted[i])
    i = i + 1

print("")
i = 0
while i < 3:
    print("%d" % listNumber[i])
    i = i + 1
