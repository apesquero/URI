# -*- coding: utf-8 -*-

values = input().split(" ")
x, y = values

x = str(x)
y = int(y)

db = {"1": 4.00, "2": 4.50, "3": 5.00, "4": 2.00, "5": 1.50}
total = db[x] * y
print("Total: R$ %.2f" % total)
